from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
import os
import time
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
import numpy as np
import joblib
import torch
from ultralytics import YOLO
from keras.preprocessing import image

survey_model = tf.keras.models.load_model('cancer_March.h5')
image_model = YOLO('best.pt')

scaler = joblib.load('March_scaler.save')

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}


@app.route('/survey')
def survey():
    return render_template('survey.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    about_text = (
        "<br>"
        "ColoDetect v1.0<br>"
        "<br>"
        "Creator: N/A<br>"
        "<br>"
        "Description:<br>"
        "<br>"
        "ColoDetect is an application designed to make the process of colorectal health assessment more "
        "accessible. It helps individuals assess their risk of colorectal cancer by providing a user-friendly "
        "survey that takes various risk factors into account.<br>"
        "The application aims to raise awareness and promote early detection of colorectal cancer, ultimately "
        "contributing to better colorectal health outcomes.<br>"
    )
    return render_template('about.html', about_text=about_text)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/imaging', methods=['GET','POST'])
def imaging():
    return render_template('imaging.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400


    file = request.files['file']

    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # test_image = image.load_img(f'uploads/{file.filename}', target_size=(64, 64))
        img = image_model([f'uploads/{file.filename}'])


        for im in img:
            boxes = im.boxes  # Boxes object for bbox outputs
            masks = im.masks  # Masks object for segmentation masks outputs
            keypoints = im.keypoints  # Keypoints object for pose outputs
            probs = im.probs
            cancer_category = torch.argmax(probs.data).item()
            value = probs.data[cancer_category].item()
        if cancer_category==0:
            message = f"You may have colon cancer with a probablilty of {round(value,2)}"
        else:
            message = f"You are cancer free with a probablilty of {round(value,2)}"

        return render_template('result.html', message=message, risk_range=value)






@app.route('/calculate_risk', methods=['POST'])
def calculate_risk():
    age = request.form.get('age', 0, type=int)
    bmi = request.form.get('bmi', 0, type=int)
    diet = request.form.get('diet', 0, type=int)
    diet_servings = request.form.get('diet_servings', 0, type=int)
    activity = request.form.get('activity', 0, type=int)
    activity_daily = request.form.get('activity_daily', 0, type=int)
    smoking = request.form.get('smoking', 0, type=int)
    colonoscopy = request.form.get('colonoscopy', 'no')
    genetics = request.form.get('genetics', 'zero')
    if colonoscopy == 'yes':
        temp_colonoscopy = 1
    elif colonoscopy == 'no':
        temp_colonoscopy = 0

    if genetics == 'zero':
        temp_gen = 0
    elif genetics == 'one':
        temp_gen = 1

    elif genetics == 'two':
        temp_gen = 2

    prediction_set = [age, bmi, diet, diet_servings, activity, activity_daily, temp_gen, smoking, temp_colonoscopy]

    prediction = survey_model.predict(scaler.transform([prediction_set]))
    risk = np.exp(prediction) - 1



    message = f"Based on your responses, your estimated risk of colorectal cancer is {risk[0][0]}%."

    # return jsonify({
    #     'risk_range': risk,
    #     'message': f"Based on your responses, your estimated risk of colorectal cancer is {risk}%."
    # })
    return render_template('result.html', message=message, risk_range=risk)


if __name__ == '__main__':
    app.run(debug=True)