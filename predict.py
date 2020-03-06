import numpy as np
import cv2
from keras.preprocessing import image
from keras.models import load_model


#Eye Detection Haar-cascade
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

#Keras model loader
model_load = load_model('./model/pinky_only_CNN_02_14_2020.h5')

# image pre-processing
def img_input(img):

    #Preprocess the image and resize it to 150*150 and normalize it
    img_process = image.load_img(img, target_size=(150, 150))
    img_process = image.img_to_array(img_process)
    img_process = np.expand_dims(img_process, axis=0)
    img_process = img_process/255

    #return the image
    return img_process

# eye-Detection
def detect_eyes(img):
    img = cv2.imread(img,0)
    try:
        face_img = img.copy()
        SF = 1.35
        mN = 7
        eyes = eye_cascade.detectMultiScale(face_img,scaleFactor=SF,minNeighbors=mN)

        for (x,y,w,h) in eyes:
            cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 5)
        val = [x,y,w,h]

    except UnboundLocalError:
        return "Invalid image"
    else:
        #print(np.sum(val))
        return "Valid image"
        #return face_img

        #print(x,y,w,h)


# Model - Prediction
def classfication_result(img):
    return (type(model_load))
    result = model_load.predict_classes(img)
    return result


# Pink Eye Detection
def pink_eye_new(input_raw_img,itching,discharge,pain_blur_eye):
    validation_image = "Valid image"
    return classfication_result(input_image_preprocessed)
    #print(validation_image)
    if validation_image == "Valid image":
        #return "Valid image"
        input_image_preprocessed = img_input(input_raw_img)
        eye_prediction = classfication_result(input_image_preprocessed)
        #print(eye_prediction[0][0])
        #return eye_prediction
        if eye_prediction[0][0] == 1 and (itching == 0 and discharge == 0 and pain_blur_eye == 0):
            return ["Not a pink eye"]

        elif eye_prediction[0][0] == 1 and (itching == 0 and discharge == 0 and pain_blur_eye == 1):
            return ["Not a pink eye"]

        elif eye_prediction[0][0] == 1 and (itching == 0 and discharge == 1 and (pain_blur_eye == 1 or pain_blur_eye == 0)):
            return ["Pink eye", "Bacterial or Viral Conjunctivitis"]

        elif eye_prediction[0][0] == 1 and (itching == 1 and discharge == 0 and (pain_blur_eye == 1 or pain_blur_eye == 0)):
            return ["Pink eye", "Allergic Conjunctivitis"]

        elif eye_prediction[0][0] == 1 and (itching == 1 and discharge == 1 and (pain_blur_eye == 1 or pain_blur_eye == 0)):
            return ["Pink eye", "Allergic Conjunctivitis"]


        else:
            return ["Not a Pink Eye"]
    else:
        return ["Invalid image"]


def prediction(file, itch, disch, pain_blur):
    #input raw image file
    #print("\n\n\n",file)
    
    input_raw_img = './static/temp/'+file

    display_img = cv2.imread(input_raw_img)
    display_img = cv2.cvtColor(display_img,cv2.COLOR_BGR2RGB)
    #plt.imshow(display_img)

    itching = itch
    discharge = disch
    pain_blur_eye = pain_blur

    return pink_eye_new(input_raw_img,itching,discharge,pain_blur_eye)
