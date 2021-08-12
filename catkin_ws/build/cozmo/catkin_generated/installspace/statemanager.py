#!/usr/bin/env python3

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
# variableactiontime = None
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

# def funcactiontime(data):
#     rospy.loginfo(rospy.get_caller_id() + ' ActionTime I heard %s', data.data)
#     global variableactiontime
#     variableactiontime = data.data

def funcaction(data):
    # rospy.loginfo(rospy.get_caller_id() + ' Action I heard %s', data.data)
    global variableaction
    global oldtime
    # print("1",variableaction)
    variableaction = data.data
    # print("2",variableaction)
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

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('statemanager', anonymous=True)
    rospy.Subscriber('cammood', String, funcwebcammood)
    rospy.Subscriber('camgaze', Int8, funcwebcamgaze)
    rospy.Subscriber('microvolume', String, funcmicrophonevolume)
    rospy.Subscriber('inputmood', String, funcinputmood)
    rospy.Subscriber('inputactivity', String, funcinputactivity)
    rospy.Subscriber('chatter', Int8, funcaction)
    rospy.Subscriber('normalstatesaver', String, funcnormalstatesaver)

    pub = rospy.Publisher('normalstatespacepublisher', String, queue_size=10)

    # rospy.Subscriber('actiontime', Int8, funcactiontime)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()



if __name__ == '__main__':
    # statemanager()
    try:
        statemanager()

    except rospy.ROSInterruptException:
        pass
