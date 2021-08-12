from __future__ import print_function
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, BatchNormalization
from keras.layers import Conv2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
import os
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.advanced_activations import ELU
from keras.layers.core import Activation, Flatten, Dropout, Dense
from keras.optimizers import RMSprop, SGD, Adam
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from keras import regularizers
from keras.regularizers import l1

from keras.models import load_model

# classifier = load_model('./emotion_detector_models/model_v6_23.hdf5')
classifier = load_model('catkin_ws/src/cozmo/scripts/emotion_detector_models/model_v6_23.hdf5')

import cv2
import time
import numpy as np
from time import sleep
from keras.preprocessing.image import img_to_array
import rospy
from std_msgs.msg import String, Int8

class_labels = ["Angry","Disgust","Fear","Happy","Neutral","Sad","Surprise"]

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def webcammooddetector():
    pub = rospy.Publisher('cammood', String, queue_size=10)
    gaze = rospy.Publisher('camgaze', Int8, queue_size=10)
    rospy.init_node('webcammooddetector', anonymous=True)


    def face_detector(img):
        # Convert image to grayscale
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        if faces is ():
            return (0,0,0,0), np.zeros((48,48), np.uint8), img

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]

        try:
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation = cv2.INTER_AREA)
        except:
            return (x,w,y,h), np.zeros((48,48), np.uint8), img
        return (x,w,y,h), roi_gray, img

    cap = cv2.VideoCapture(0)

    while not rospy.is_shutdown():
        looking = 0

        ret, frame = cap.read()
        rect, face, image = face_detector(frame)
        if np.sum([face]) != 0.0:
            roi = face.astype("float") / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            # make a prediction on the ROI, then lookup the class
            preds = classifier.predict(roi)[0]
            label = class_labels[preds.argmax()]
            label_position = (rect[0] + int((rect[1]/2)), rect[2] + 25)
            cv2.putText(image, label, label_position , cv2.FONT_HERSHEY_SIMPLEX,2, (0,255,0), 3)
            # print("Label: ", label)
            # time.sleep(5)
            if label != "Neutral" and label != "Sad" and label != "Happy" and label != "Surprise":
                rospy.loginfo("Neutral")
                pub.publish("Neutral")
            else:
                rospy.loginfo(label)
                pub.publish(label)
            looking = 1
            rospy.loginfo(looking)
            gaze.publish(looking)
            if label != "Neutral" and label != "Sad":
                time.sleep(60)
            if label == "Sad":
                time.sleep(30)
        else:
            cv2.putText(image, "No Face Found", (20, 60) , cv2.FONT_HERSHEY_SIMPLEX,2, (0,255,0), 3)
            # label = "None detected"
            label = "Neutral"
            rospy.loginfo(label)
            pub.publish(label)
            looking = 0
            rospy.loginfo(looking)
            gaze.publish(looking)
            # print("Label: None")

        cv2.imshow('All', image)
        if cv2.waitKey(1) == 13: #13 is the Enter Key
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        webcammooddetector()
    except rospy.ROSInterruptException:
        pass
