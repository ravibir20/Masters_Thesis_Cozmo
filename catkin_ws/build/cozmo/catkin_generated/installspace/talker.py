#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Int8
from tkinter import *
import time
import datetime
import pytz
import csv

window = Tk()
action = 0

window.title("Choose an Action for Cozmo")

window.geometry('500x500')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

def talker():
    pub = rospy.Publisher('chatter', Int8, queue_size=10)
    rospy.init_node('talker', anonymous=True)

    def clicked(act):
        action = act
        lbl.configure(text=action)
        rospy.loginfo(action)
        pub.publish(action)

        # check = datetime.datetime.now()
        # print(check)

        # save_list = ['Name7', 'Branch', 'Year', 'CGPA']
        # with open('catkin_ws/src/cozmo/scripts/saved_actions.csv', mode='a') as recorded_action:   #newline=''
        #     print("here")
        #     write = csv.writer(recorded_action)      #, delimiter=','
        #     write.writerow(save_list)

        # rate.sleep()

        # action = 0

    btn1 = Button(window, text="Happy", height=4, width=12, command=lambda *args: clicked(1))
    btn2 = Button(window, text="Sad", height=4, width=12, command=lambda *args: clicked(2))
    btn3 = Button(window, text="Angry", height=4, width=12, command=lambda *args: clicked(3))
    btn4 = Button(window, text="Shocked", height=4, width=12, command=lambda *args: clicked(4))
    btn5 = Button(window, text="Monster", height=4, width=12, command=lambda *args: clicked(5))
    btn6 = Button(window, text="Animal", height=4, width=12, command=lambda *args: clicked(6))
    btn7 = Button(window, text="Hyperactive", height=4, width=12, command=lambda *args: clicked(7))
    btn8 = Button(window, text="Ill", height=4, width=12, command=lambda *args: clicked(8))
    btn9 = Button(window, text="Sing", height=4, width=12, command=lambda *args: clicked(9))
    btn10 = Button(window, text="Say Joke", height=4, width=12, command=lambda *args: clicked(10))
    btn11 = Button(window, text="Say Reminder", height=4, width=12, command=lambda *args: clicked(11))
    btn12 = Button(window, text="Hand Interaction", height=4, width=12, command=lambda *args: clicked(12))
    btn13 = Button(window, text="Game- Quick Tap", height=4, width=12, command=lambda *args: clicked(13))
    btn14 = Button(window, text="Short Bricks", height=4, width=12, command=lambda *args: clicked(14))
    btn15 = Button(window, text="Long Bricks", height=4, width=12, command=lambda *args: clicked(15))
    btn16 = Button(window, text="Background", height=4, width=12, command=lambda *args: clicked(16))
    btn17 = Button(window, text="Charger", height=4, width=12, command=lambda *args: clicked(17))


    btn1.grid(column=1, row=0, padx=10, pady=10)
    btn2.grid(column=2, row=0, padx=10, pady=10)
    btn3.grid(column=3, row=0, padx=10, pady=10)
    btn4.grid(column=4, row=0, padx=10, pady=10)
    btn5.grid(column=1, row=1, padx=10, pady=10)
    btn6.grid(column=2, row=1, padx=10, pady=10)
    btn7.grid(column=3, row=1, padx=10, pady=10)
    btn8.grid(column=4, row=1, padx=10, pady=10)
    btn9.grid(column=1, row=2, padx=10, pady=10)
    btn10.grid(column=2, row=2, padx=10, pady=10)
    btn11.grid(column=3, row=2, padx=10, pady=10)
    btn12.grid(column=1, row=3, padx=10, pady=10)
    btn13.grid(column=2, row=3, padx=10, pady=10)
    btn14.grid(column=1, row=4, padx=10, pady=10)
    btn15.grid(column=2, row=4, padx=10, pady=10)
    btn16.grid(column=3, row=4, padx=10, pady=10)
    btn17.grid(column=4, row=4, padx=10, pady=10)
    # rate = rospy.Rate(0.1) # 10hz
    while not rospy.is_shutdown():
        window.mainloop()
        # selected_action = action
        # hello_str = "hello world %s" % rospy.get_time()
        # rospy.loginfo(action)
        # pub.publish(action)
        # rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
