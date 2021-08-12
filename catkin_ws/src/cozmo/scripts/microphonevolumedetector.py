#!/usr/bin/env python3
import aubio
import numpy as num
import pyaudio
import sys
import numpy as np
import rospy
from std_msgs.msg import String, Int8

# Some constants for setting the PyAudio and the
# Aubio.
BUFFER_SIZE             = 2048
CHANNELS                = 1
FORMAT                  = pyaudio.paFloat32
METHOD                  = "default"
SAMPLE_RATE             = 44100
HOP_SIZE                = BUFFER_SIZE//2
PERIOD_SIZE_IN_FRAME    = HOP_SIZE

def microphonevolumedetector():
    pub = rospy.Publisher('microvolume', String, queue_size=10)
    rospy.init_node('microphonevolumedetector', anonymous=True)

    # Initiating PyAudio object.
    pA = pyaudio.PyAudio()
    # Open the microphone stream.
    mic = pA.open(format=FORMAT, channels=CHANNELS,
        rate=SAMPLE_RATE, input=True,
        frames_per_buffer=PERIOD_SIZE_IN_FRAME)

    # Initiating Aubio's pitch detection object.
    pDetection = aubio.pitch(METHOD, BUFFER_SIZE,
        HOP_SIZE, SAMPLE_RATE)
    # Set unit.
    pDetection.set_unit("Hz")
    # Frequency under -40 dB will considered
    # as a silence.
    pDetection.set_silence(-40)

    while not rospy.is_shutdown():

        # Always listening to the microphone.
        data = mic.read(PERIOD_SIZE_IN_FRAME)
        # Convert into number that Aubio understand.
        samples = num.fromstring(data,
            dtype=aubio.float_type)
        # Finally get the pitch.
        pitch = pDetection(samples)[0]
        # Compute the energy (volume)
        # of the current frame.
        volume = num.sum(samples**2)/len(samples)

        # Format the volume output so it only
        # displays at most six numbers behind 0.
        volume = "{:6f}".format(volume)
        volume = float(volume)

        if volume == 0:
            # print("None")
            label = "None"
        elif volume > 0 and volume <= 0.0008:
            # print("Low")
            label = "Low"
        else:
            # print("High")
            label = "High"

        rospy.loginfo(label)
        pub.publish(label)

if __name__ == '__main__':
    try:
        microphonevolumedetector()
    except rospy.ROSInterruptException:
        pass
