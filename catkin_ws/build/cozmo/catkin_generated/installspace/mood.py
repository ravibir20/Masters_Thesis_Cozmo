#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Int8
from tkinter import *

window = Tk()
action = "Neutral"

window.title("Select a Mood")

window.geometry('500x300')

lbl = Label(window, text="Select")

lbl.grid(column=0, row=0)

def mood():
    pub = rospy.Publisher('inputmood', String, queue_size=10)
    rospy.init_node('mood', anonymous=True)

    def clicked(act):
        action = act
        lbl.configure(text=action)
        rospy.loginfo(action)
        pub.publish(action)
        # rate.sleep()

        # action = 0

    btn1 = Button(window, text="Positive", height=4, width=12, command=lambda *args: clicked("Positive"))
    btn2 = Button(window, text="Neutral", height=4, width=12, command=lambda *args: clicked("Neutral"))
    btn3 = Button(window, text="Negative", height=4, width=12, command=lambda *args: clicked("Neutral"))


    btn1.grid(column=1, row=0, padx=10, pady=10)
    btn2.grid(column=2, row=0, padx=10, pady=10)
    btn3.grid(column=3, row=0, padx=10, pady=10)

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
        mood()
    except rospy.ROSInterruptException:
        pass
