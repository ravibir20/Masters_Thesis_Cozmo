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

# source catkin_ws/devel/setup.bash

variableaction = None
variablewebcammood = "Neutral"
variablewebcamgaze = 0
variablemicrophonevolume = "None"
variableinputmood = "Neutral"
variableinputactivity = "Relaxing"   #Change depending on starting activity

oldtime = datetime.datetime.now()
oldtime -= oldtime

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
    variableinputactivity = data.data

def funcaction(data):
    # rospy.loginfo(rospy.get_caller_id() + ' Action I heard %s', data.data)
    global variableaction
    global oldtime
    variableaction = data.data
    rospytime = rospy.Time.now()
    normaltime = datetime.datetime.now()

    elapsedsessiontime = normaltime - begintime

    timesincelastaction = normaltime - oldtime
    oldtime = normaltime

    action_save_list = [variableaction, rospytime, normaltime, elapsedsessiontime, timesincelastaction, variablewebcammood, variablewebcamgaze, variablemicrophonevolume, variableinputmood, variableinputactivity]
    print("actionsavelist",action_save_list)

    with open('catkin_ws/src/cozmo/scripts/test.csv', mode='a') as recorded_action:   #newline=''
        write = csv.writer(recorded_action)      #, delimiter=','
        write.writerow(action_save_list)

    variableaction = None

def funcnormalstatesaver(data):
    #save the action space to a csv
    rospytime = rospy.Time.now()
    normaltime = datetime.datetime.now()

    elapsedsessiontime = normaltime - begintime

    timesincelastaction = normaltime - oldtime

    normal_save_list = [variableaction, rospytime, normaltime, elapsedsessiontime, timesincelastaction, variablewebcammood, variablewebcamgaze, variablemicrophonevolume, variableinputmood, variableinputactivity]
    print("normalsavelist",normal_save_list)

    with open('catkin_ws/src/cozmo/scripts/test.csv', mode='a') as recorded_state:   #newline=''
        write = csv.writer(recorded_state)      #, delimiter=','
        write.writerow(normal_save_list)

def statemanager():

    rospy.init_node('statemanager', anonymous=True)
    rospy.Subscriber('cammood', String, funcwebcammood)
    rospy.Subscriber('camgaze', Int8, funcwebcamgaze)
    rospy.Subscriber('microvolume', String, funcmicrophonevolume)
    rospy.Subscriber('inputmood', String, funcinputmood)
    rospy.Subscriber('inputactivity', String, funcinputactivity)
    rospy.Subscriber('chatter', Int8, funcaction)
    rospy.Subscriber('normalstatesaver', String, funcnormalstatesaver)

    pub = rospy.Publisher('normalstatespacepublisher', String, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    try:
        statemanager()

    except rospy.ROSInterruptException:
        pass
