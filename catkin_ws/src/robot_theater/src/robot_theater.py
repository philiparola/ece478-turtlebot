#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
from std_msgs.msg import Float64
import time
import os

def ourDelay(time_sleep):
    time.sleep(time_sleep)

def waitForCat(time_sleep):
    if time_sleep is 0:
        time_sleep = 5
	time.sleep(time_sleep)

def shakeHead():
    NeckHori = rospy.Publisher('NeckHori_09/command', Float64, queue_size=10)
    NeckHori.publish(0.95)
    time.sleep(.5)
    NeckHori.publish(-0.94)
    time.sleep(.5)
    NeckHori.publish(0.95)
    time.sleep(.5)
    NeckHori.publish(0)
    
def nodHead():
    NeckVert = rospy.Publisher('NeckVert_10/command', Float64, queue_size=10)
    NeckVert.publish(0.8)
    time.sleep(.5)
    NeckVert.publish(-0.8)
    time.sleep(.5)
    NeckVert.publish(0)

def leftWave():
    RArmShoulderVert = rospy.Publisher('RArmShoulderVert_01/command', Float64, queue_size=10)
    RArmShoulderHori = rospy.Publisher('RArmShoulderHori_02/command', Float64, queue_size=10)
    RArmElbowVert = rospy.Publisher('RArmElbowVert_03/command', Float64, queue_size=10)
    RArmElbowHori = rospy.Publisher('RArmElbowHori_04/command', Float64, queue_size=10)
    LArmShoulderVert = rospy.Publisher('LArmShoulderVert_05/command', Float64, queue_size=10)
    LArmShoulderHori = rospy.Publisher('LArmShoulderHori_06/command', Float64, queue_size=10)
    LArmElbowVert = rospy.Publisher('LArmElbowVert_07/command', Float64, queue_size=10)
    LArmElbowHori = rospy.Publisher('LArmElbowHori_08/command', Float64, queue_size=10)
    NeckHori = rospy.Publisher('NeckHori_09/command', Float64, queue_size=10)
    NeckVert = rospy.Publisher('NeckVert_10/command', Float64, queue_size=10)
    RArmShoulderVert.publish(0)
    RArmShoulderHori.publish(0)
    RArmElbowVert.publish(1.05)
    RArmElbowHori.publish(1.89)
    LArmShoulderVert.publish(0)
    LArmShoulderHori.publish(0.84)
    LArmElbowVert.publish(1.05)
    LArmElbowHori.publish(0)
    NeckHori.publish(0.95)
    NeckVert.publish(0.8)	
    time.sleep(1)
    LArmElbowHori.publish(1.05)
    time.sleep(1)


def rightWave():
    RArmShoulderVert = rospy.Publisher('RArmShoulderVert_01/command', Float64, queue_size=10)
    RArmShoulderHori = rospy.Publisher('RArmShoulderHori_02/command', Float64, queue_size=10)
    RArmElbowVert = rospy.Publisher('RArmElbowVert_03/command', Float64, queue_size=10)
    RArmElbowHori = rospy.Publisher('RArmElbowHori_04/command', Float64, queue_size=10)
    LArmShoulderVert = rospy.Publisher('LArmShoulderVert_05/command', Float64, queue_size=10)
    LArmShoulderHori = rospy.Publisher('LArmShoulderHori_06/command', Float64, queue_size=10)
    LArmElbowVert = rospy.Publisher('LArmElbowVert_07/command', Float64, queue_size=10)
    LArmElbowHori = rospy.Publisher('LArmElbowHori_08/command', Float64, queue_size=10)
    NeckHori = rospy.Publisher('NeckHori_09/command', Float64, queue_size=10)
    NeckVert = rospy.Publisher('NeckVert_10/command', Float64, queue_size=10)
    RArmShoulderVert.publish(2.52)
    RArmShoulderHori.publish(0.95)
    RArmElbowVert.publish(1.05)
    RArmElbowHori.publish(1.89)
    LArmShoulderVert.publish(2.52)
    LArmShoulderHori.publish(1.89)
    LArmElbowVert.publish(1.05)
    LArmElbowHori.publish(0)
    NeckHori.publish(-0.94)
    NeckVert.publish(0.8)	
    time.sleep(1)
    RArmElbowHori.publish(0)
    time.sleep(1)

def bothWave():
    RArmShoulderVert = rospy.Publisher('RArmShoulderVert_01/command', Float64, queue_size=10)
    RArmShoulderHori = rospy.Publisher('RArmShoulderHori_02/command', Float64, queue_size=10)
    RArmElbowVert = rospy.Publisher('RArmElbowVert_03/command', Float64, queue_size=10)
    RArmElbowHori = rospy.Publisher('RArmElbowHori_04/command', Float64, queue_size=10)
    LArmShoulderVert = rospy.Publisher('LArmShoulderVert_05/command', Float64, queue_size=10)
    LArmShoulderHori = rospy.Publisher('LArmShoulderHori_06/command', Float64, queue_size=10)
    LArmElbowVert = rospy.Publisher('LArmElbowVert_07/command', Float64, queue_size=10)
    LArmElbowHori = rospy.Publisher('LArmElbowHori_08/command', Float64, queue_size=10)
    NeckHori = rospy.Publisher('NeckHori_09/command', Float64, queue_size=10)
    NeckVert = rospy.Publisher('NeckVert_10/command', Float64, queue_size=10)
    RArmShoulderVert.publish(2.52)
    RArmShoulderHori.publish(0.95)
    RArmElbowVert.publish(1.05)
    RArmElbowHori.publish(1.89)
    LArmShoulderVert.publish(0)
    LArmShoulderHori.publish(0.84)
    LArmElbowVert.publish(1.05)
    LArmElbowHori.publish(0)	
    time.sleep(1)
    RArmElbowHori.publish(0)
    LArmElbowHori.publish(1.05)
    time.sleep(1)



def raiseArms():
    RArmShoulderVert = rospy.Publisher('RArmShoulderVert_01/command', Float64, queue_size=10)
    RArmShoulderHori = rospy.Publisher('RArmShoulderHori_02/command', Float64, queue_size=10)
    RArmElbowVert = rospy.Publisher('RArmElbowVert_03/command', Float64, queue_size=10)
    RArmElbowHori = rospy.Publisher('RArmElbowHori_04/command', Float64, queue_size=10)
    LArmShoulderVert = rospy.Publisher('LArmShoulderVert_05/command', Float64, queue_size=10)
    LArmShoulderHori = rospy.Publisher('LArmShoulderHori_06/command', Float64, queue_size=10)
    LArmElbowVert = rospy.Publisher('LArmElbowVert_07/command', Float64, queue_size=10)
    LArmElbowHori = rospy.Publisher('LArmElbowHori_08/command', Float64, queue_size=10)
    NeckHori = rospy.Publisher('NeckHori_09/command', Float64, queue_size=10)
    NeckVert = rospy.Publisher('NeckVert_10/command', Float64, queue_size=10)
    RArmShoulderVert.publish(2.52)
    RArmShoulderHori.publish(0.95)
    RArmElbowVert.publish(1.05)
    RArmElbowHori.publish(1.89)
    LArmShoulderVert.publish(0)
    LArmShoulderHori.publish(0.84)
    LArmElbowVert.publish(1.05)
    LArmElbowHori.publish(0)


def lowerArms():
    RArmShoulderVert = rospy.Publisher('RArmShoulderVert_01/command', Float64, queue_size=10)
    RArmShoulderHori = rospy.Publisher('RArmShoulderHori_02/command', Float64, queue_size=10)
    RArmElbowVert = rospy.Publisher('RArmElbowVert_03/command', Float64, queue_size=10)
    RArmElbowHori = rospy.Publisher('RArmElbowHori_04/command', Float64, queue_size=10)
    LArmShoulderVert = rospy.Publisher('LArmShoulderVert_05/command', Float64, queue_size=10)
    LArmShoulderHori = rospy.Publisher('LArmShoulderHori_06/command', Float64, queue_size=10)
    LArmElbowVert = rospy.Publisher('LArmElbowVert_07/command', Float64, queue_size=10)
    LArmElbowHori = rospy.Publisher('LArmElbowHori_08/command', Float64, queue_size=10)
    NeckHori = rospy.Publisher('NeckHori_09/command', Float64, queue_size=10)
    NeckVert = rospy.Publisher('NeckVert_10/command', Float64, queue_size=10)
    RArmShoulderVert.publish(0)
    RArmShoulderHori.publish(0)
    RArmElbowVert.publish(1.05)
    RArmElbowHori.publish(1.89)
    LArmShoulderVert.publish(2.52)
    LArmShoulderHori.publish(1.89)
    LArmElbowVert.publish(1.05)
    LArmElbowHori.publish(0)
    pass

def faceAudience():
    pass

def faceCat():
    pass

rospy.init_node('robot_theater_einstein', anonymous=True)
rate = rospy.Rate(10) # 10hz

raiseArms()
time.sleep(5)
bothWave()
time.sleep(5)
lowerArms()
time.sleep(5)
nodHead()
time.sleep(5)
shakeHead()


'''
waitForCat(13)
waitForCat(10)
waitForCat(3)
waitForCat(9)
waitForCat(8)
faceAudience()
bothWave()
lowerArms()
faceCat()
ourDelay(8)
ourDelay(3)
waitForCat(8)
bothWave()
ourDelay(4)
waitForCat(6)
bothWave()
ourDelay(2)
waitForCat(6)
faceAudience()
ourDelay(3)
waitForCat(6)
lowerArms()
ourDelay(1)
waitForCat(9)
raiseArms()
ourDelay(2)
waitForCat(13)
nodHead()
ourDelay(4)
waitForCat(15)
waitForCat(2)
raiseArms()
lowerArms()
faceAudience()
ourDelay(1)
ourDelay(14)
waitForCat(5)
time.sleep(9) #aint doing anything
waitForCat(6)
faceCat()
ourDelay(6)
waitForCat(8)
faceAudience()
ourDelay(2)
waitForCat(7)
nodHead()
ourDelay(4)
waitForCat(6)
leftWave()
ourDelay(2)
waitForCat(0)
lowerArms()
'''
