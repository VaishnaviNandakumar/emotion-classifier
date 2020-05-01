## Emotion Detection Classifier
Submission for HackerEarth Challenge 
https://www.hackerearth.com/challenges/competitive/hackerearth-deep-learning-challenge-emotion-detection-tom-jerry-cartoon/

### Problem
A Tom and Jerry cartoon was provided along with a CSV file labelling their expressions for 298 frames. The developed model had to predict the emotions of 175 frames as given in another MP4 file.

### Data Preprocessing
* Created an encoder and a decoder for the available labels
* Took in the input image and transformed it into an optimal crop size image (400, 700)
* Resized image to dimensions (224x224)

### Data Augmentation
* Utilized albumentation library with features like -  CLAHE(), RandomRotate90(), ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.50, rotate_limit=45, p=.75), Blur(blur_limit=3), OpticalDistortion(), GridDistortion(), HueSaturationValue()
* Added more images with flipped images, random noise and rotation.

### Model
* Used VGG16 model with 5 output features.
* Achieved accuracy of 93% on training set.
