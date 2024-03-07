from ultralytics import YOLO
import torch

model = YOLO('yolov8n-cls.pt')


results = model.train(data='Dataset-Cancer', epochs=2, imgsz=64)


pred_results = model(['3.jpg','4.jpg','7.jpg','69.jpg','71.jpg','75.jpg'])
#
pred_results = model(['3.jpg','75.jpg'])
for result in pred_results:
    boxes = result.boxes  # Boxes object for bbox outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    print(probs)

    print("-------")

    argmax = torch.argmax(probs.data).item()
    value = probs.data[argmax].item()

    print(argmax,value)

#this is how yolo saves the model, i just copied to best.pt in the project here for ease of use
# model_for_export = YOLO(r'C:\Users\Bozo\PycharmProjects\runs\classify\train6\weights\best.pt')
