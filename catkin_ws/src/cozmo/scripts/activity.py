#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Int8
from tkinter import *

window = Tk()
action = ""

window.title("Select an Activity")

window.geometry('500x300')

lbl = Label(window, text="Select")

lbl.grid(column=0, row=0)

def activity():
    pub = rospy.Publisher('inputactivity', String, queue_size=10)
    rospy.init_node('activity', anonymous=True)

    def clicked(act):
        action = act
        lbl.configure(text=action)
        rospy.loginfo(action)
        pub.publish(action)

    btn1 = Button(window, text="Studying", height=4, width=12, command=lambda *args: clicked("Studying"))
    btn2 = Button(window, text="Relaxing", height=4, width=12, command=lambda *args: clicked("Relaxing"))
    btn3 = Button(window, text="Eating", height=4, width=12, command=lambda *args: clicked("Eating"))
    btn4 = Button(window, text="Do Not Disturb", height=4, width=12, command=lambda *args: clicked("Do Not Disturb"))


    btn1.grid(column=1, row=0, padx=10, pady=10)
    btn2.grid(column=2, row=0, padx=10, pady=10)
    btn3.grid(column=1, row=1, padx=10, pady=10)
    btn4.grid(column=2, row=1, padx=10, pady=10)

    while not rospy.is_shutdown():
        window.mainloop()

if __name__ == '__main__':
    try:
        activity()
    except rospy.ROSInterruptException:
        pass
