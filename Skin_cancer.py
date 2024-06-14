from keras.preprocessing import image
import numpy as np
from keras.models import load_model
import cv2


def preprocessing(img_path):
    img_arr = cv2.imread( img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img_arr,(128,128))
    norm_img = image.img_to_array(img) / 255

        # Converting Image to Numpy Arrayp
    input_arr_img = np.array([norm_img])
    return input_arr_img


def predict(img_path):
    model = load_model('./models/skin_cancer.h5')
    img = preprocessing(img_path)
    pred = np.argmax(model.predict(img))
    return pred

def skin(img_path):
    labels = ["benign","malignant"]
    prediction = predict(img_path)
    return labels[prediction]
