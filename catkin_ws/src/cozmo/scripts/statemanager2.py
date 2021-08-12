#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Int8
import cozmo
import random
import cv2
import numpy as np
import asyncio
import math
from cozmo.util import distance_mm, speed_mmps, degrees
import csv
import time
import datetime
import pytz
import pandas as pd
import os
import pickle
from pandas.api.types import CategoricalDtype
# source catkin_ws/devel/setup.bash

do_not_disturb = 1
last_action = 17
charge_performed = 0
variableaction = None
variablewebcammood = "Neutral"
variablewebcamgaze = 0
variablemicrophonevolume = "None"
variableinputmood = "Neutral"
variableinputactivity = "Relaxing"   #Change depending on starting activity

oldtime = datetime.datetime.now()

oldtimecharge = datetime.datetime.now()

begintime = datetime.datetime.now()

def funcwebcammood(data):
    # rospy.loginfo(rospy.get_caller_id() + ' Camera mood I heard %s', data.data)
    global variablewebcammood
    variablewebcammood = data.data

def funcwebcamgaze(data):
    # rospy.loginfo(rospy.get_caller_id() + ' Gaze I heard %s', data.data)
    global variablewebcamgaze
    variablewebcamgaze = data.data

def funcmicrophonevolume(data):
    # rospy.loginfo(rospy.get_caller_id() + ' Volume I heard %s', data.data)
    global variablemicrophonevolume
    variablemicrophonevolume = data.data

def funcinputmood(data):
    # rospy.loginfo(rospy.get_caller_id() + ' Input mood I heard %s', data.data)
    global variableinputmood
    variableinputmood = data.data

def funcinputactivity(data):
    # rospy.loginfo(rospy.get_caller_id() + ' Activity I heard %s', data.data)
    global variableinputactivity
    global do_not_disturb
    global oldtimecharge
    global last_action

    if data.data == "Do Not Disturb":
        do_not_disturb = 1
    else:
        if do_not_disturb == 1:
            normaltime = datetime.datetime.now()
            oldtimecharge = normaltime
            last_action = 17
            variableinputactivity = data.data
            do_not_disturb = 0

        else:
            variableinputactivity = data.data
            do_not_disturb = 0

def funcaction(action_to_perform, action_save_list):
    # rospy.loginfo(rospy.get_caller_id() + ' Action I heard %s', data.data)
    global variableaction
    global oldtime
    global oldtimecharge
    global charge_performed
    global last_action
    variableaction = action_to_perform
    rospytime = rospy.Time.now()
    normaltime = datetime.datetime.now()

    if charge_performed == 1:
        oldtimecharge = normaltime
        charge_performed = 0

    if variableaction == 17:
        charge_performed = 1

    oldtime = normaltime

    action_save_list[0] = variableaction
    #action_save_list = [variableaction, last_action, rospytime, normaltime, elapsedsessiontime, timesincelastcharge, timesincelastaction, variablewebcammood, variablewebcamgaze, variablemicrophonevolume, variableinputmood, variableinputactivity]
    print("actionsavelist",action_save_list)

    with open('catkin_ws/src/cozmo/scripts/Bharat2_action.csv', mode='a') as recorded_action:   #newline=''
        write = csv.writer(recorded_action)      #, delimiter=','
        write.writerow(action_save_list)

    last_action = variableaction
    variableaction = None


def funcnormalstatesaver(data):
    pub = rospy.Publisher('chatter', Int8, queue_size=10)
    if do_not_disturb == 1:
        return
    else:
        #save the action space to a csv
        rospytime = rospy.Time.now()
        normaltime = datetime.datetime.now()

        timesincelastcharge = normaltime - oldtimecharge

        elapsedsessiontime = normaltime - begintime

        timesincelastaction = normaltime - oldtime

        normal_save_list = [variableaction, last_action, rospytime, normaltime, elapsedsessiontime, timesincelastcharge, timesincelastaction, variablewebcammood, variablewebcamgaze, variablemicrophonevolume, variableinputmood, variableinputactivity]

        with open('catkin_ws/src/cozmo/scripts/Bharat2_normal.csv', mode='a') as recorded_state:   #newline=''
            write = csv.writer(recorded_state)      #, delimiter=','
            write.writerow(normal_save_list)

        #Get statespace into correct format
        df = pd.DataFrame([normal_save_list])
        df.columns =['Drop1', 'Last Action', 'Drop2', 'Drop3', 'Drop4', 'Time Since Last Charge Old', 'Time Since Last Action', 'Camera Mood', 'Gaze', 'Noise', 'Input Mood', 'Activity']
        df.drop("Drop1", axis=1, inplace=True)
        df.drop("Drop2", axis=1, inplace=True)
        df.drop("Drop3", axis=1, inplace=True)
        df.drop("Drop4", axis=1, inplace=True)


        df['Time Since Last Action Formatted'] = [0]
        pd.set_option('display.max_columns', None)

        value = str(df.iloc[0]['Time Since Last Action'])
        value1 = value[10:]
        value2 = value1[:5]
        value3 = value2[:2] + "."
        value4 = int(value2[3:])
        value5 = str((round((value4/60)*100,0))/100)
        value6 = value3 + value5[2:]

        df['Time Since Last Action Formatted'][0] = value6
        df.drop("Time Since Last Action", axis=1, inplace=True)

        ###############################################################################
        df['Time Since Last Charge'] = [0]

        value_0 = str(df.iloc[0]['Time Since Last Charge Old'])
        value1_0 = value_0[10:]
        value2_0 = value1_0[:5]
        value3_0 = value2_0[:2] + "."
        value4_0 = int(value2_0[3:])
        value5_0 = str((round((value4_0/60)*100,0))/100)
        value6_0 = value3_0 + value5_0[2:]

        df['Time Since Last Charge'][0] = value6_0
        df.drop("Time Since Last Charge Old", axis=1, inplace=True)
        ###############################################################################
        df["Activity"] = df["Activity"].astype(CategoricalDtype(["Relaxing","Studying","Resting"]))
        df = pd.get_dummies(df, columns=["Activity"], prefix=["Activity"])
        df["Camera Mood"] = df["Camera Mood"].astype(CategoricalDtype(["Happy","Neutral","Sad","Surprise"]))
        df = pd.get_dummies(df, columns=["Camera Mood"], prefix=["Camera_Mood"])
        df["Input Mood"] = df["Input Mood"].astype(CategoricalDtype(["Neutral","Positive"]))
        df = pd.get_dummies(df, columns=["Input Mood"], prefix=["Input Mood"])
        df["Noise"] = df["Noise"].astype(CategoricalDtype(["High","Low","None"]))
        df = pd.get_dummies(df, columns=["Noise"], prefix=["Noise"])
        df["Last Action"] = df["Last Action"].astype(CategoricalDtype(["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17"]))
        df = pd.get_dummies(df, columns=["Last Action"], prefix=["Last Action"])

        #Normalize data, Load model 1, see if an action should be performed
        filename = 'catkin_ws/src/cozmo/scripts/TBharatUMomo_scaler1.sav'
        scaler1 = pickle.load(open(filename, 'rb'))

        df_scaled1 = df.copy()
        col_names = ['Time Since Last Charge', 'Time Since Last Action Formatted']

        features = df_scaled1[col_names]
        features = scaler1.transform(features.values)
        df_scaled1[col_names] = features


        filename = 'catkin_ws/src/cozmo/scripts/TBharatUMomo_model1.sav'
        loaded_model1 = pickle.load(open(filename, 'rb'))
        pred = loaded_model1.predict(df_scaled1)
        perform_action = pred[0]

        #If an action should be performed, Normalize data, Load model 2, see which action it should be
        if perform_action == 1:
            print(df)
            ###########################################################################may need to add stuff below
            filename = 'catkin_ws/src/cozmo/scripts/TBharatUMomo_scaler2.sav'
            scaler2 = pickle.load(open(filename, 'rb'))

            df_scaled2 = df.copy()
            col_names = ['Time Since Last Charge', 'Time Since Last Action Formatted']

            features = df_scaled2[col_names]
            features = scaler2.transform(features.values)
            df_scaled2[col_names] = features

            #Load model 1, see if an action should be performed
            filename = 'catkin_ws/src/cozmo/scripts/TBharatUMomo_model2.sav'
            loaded_model2 = pickle.load(open(filename, 'rb'))
            pred = loaded_model2.predict(df_scaled2)
            action_to_perform = int(pred[0])
            pub.publish(action_to_perform)
            funcaction(action_to_perform, normal_save_list)

            if action_to_perform == 1 or action_to_perform == 2 or action_to_perform == 3 or action_to_perform == 4 or action_to_perform == 5 or action_to_perform == 6 or action_to_perform == 8:
                rospy.sleep(10)
            if action_to_perform == 7 or action_to_perform == 9 or action_to_perform == 10 or action_to_perform == 11:
                rospy.sleep(20)
            if action_to_perform == 12:
                rospy.sleep(35)
            if action_to_perform == 13:
                rospy.sleep(60)
            if action_to_perform == 14:
                rospy.sleep(75)
            if action_to_perform == 15  or action_to_perform == 16:
                rospy.sleep(90)
            if action_to_perform == 17:
                rospy.sleep(900)


def statemanager():

    rospy.init_node('statemanager', anonymous=True)
    rospy.Subscriber('cammood', String, funcwebcammood)
    rospy.Subscriber('camgaze', Int8, funcwebcamgaze)
    rospy.Subscriber('microvolume', String, funcmicrophonevolume)
    rospy.Subscriber('inputmood', String, funcinputmood)
    rospy.Subscriber('inputactivity', String, funcinputactivity)
    rospy.Subscriber('normalstatesaver', String, funcnormalstatesaver)

    rospy.spin()

if __name__ == '__main__':
    try:
        statemanager()

    except rospy.ROSInterruptException:
        pass
