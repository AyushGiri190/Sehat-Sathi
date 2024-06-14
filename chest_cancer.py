from keras.preprocessing import image
import numpy as np
from keras.models import load_model
import cv2

def preprocessing(img_path):
        # Normalizing Image
        img = image.load_img(img_path, target_size=(350, 350))

        norm_img = image.img_to_array(img) / 255

        # Converting Image to Numpy Arrayp
        input_arr_img = np.array([norm_img])
        return input_arr_img
        # Getting Predictions
        #pred = np.argmax(_model.predict(input_arr_img))


def predict(img_path):
    model = load_model('./models/lung cancer.h5')
    img = preprocessing(img_path)
    pred = np.argmax(model.predict(img))
    return pred


def chest(img_path):
    labels = ["Adenocarcinoma", "Large cell carcinoma", "Normal", "Squamous cell carcinoma"]
    prediction = predict(img_path)
    return labels[prediction]




