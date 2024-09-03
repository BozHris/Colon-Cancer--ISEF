I've created this project for a US student that entered the ISEF competition in the medical sector. Update as of 5th of March, this project placed 3rd in the regional competition, sadly this result didn't qualify it for the internationals.
This project consist of two parts, one regression and one classification. 
For the regression I reverse engineered this calculator : https://ccrisktool.cancer.gov/calculator.html since there was no similar datasets online for these requirements. 
I've scraped and preprocessed the data, then built a 4 layer nn regressor in Tensorflow trained it on 150 epochs and at the end got a  MSE loss: 0.0078 - val_loss: 0.0258
For the classification model i used YOLO v8 and trained it on the kaggle dataset this achieved an accuracy of 91.24%

Final Look of the App: 

Landing Page: 
![image](https://github.com/user-attachments/assets/b2fe5972-324f-450c-8816-e00b9be5b143)


Survey: 
![image](https://github.com/user-attachments/assets/a2abc403-6a6c-4a46-aac4-33ed9a5b01bf)
![image](https://github.com/user-attachments/assets/9e58dc0d-20e6-4028-b5df-cd409362886b)

Survey Example Result: 
![image](https://github.com/user-attachments/assets/d70d0ac3-7f47-41df-9e20-7ecb1eafb64d)


Colonoscopy Image: 
![image](https://github.com/user-attachments/assets/6b424bc1-17ab-47e9-bc2a-9ec6e17d39c6)
![image](https://github.com/user-attachments/assets/dbc3a68e-f63f-43b9-9ce2-ad486a35b9b4)
Image Result: 
![image](https://github.com/user-attachments/assets/6e01a09b-4b8e-419d-8577-1a9a3cec807f)
