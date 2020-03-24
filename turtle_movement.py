#! /usr/bin/env python
# run "roscore" in a new terminal
# run"rosrun turtlesim turtlesim_node" in a new terminal
# run (rosservice call/spawn 10 10 0 "abhiyaan") to create a new turtle
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import numpy as np

global a,b,a1,b1
a1=b1=10
a=b=5


def callback(data):
	global a,b
	a=round(float(data.x),2) 
	b=round(float(data.y),2)

def callback1(data1):
        global a1,b1
        a1=round(float(data1.x),2)
        b1=round(float(data1.y),2)


def movement():
	rospy.init_node("turtle_exercise",anonymous=True)
	pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
	
	sub = rospy.Subscriber("turtle1/pose", Pose, callback)
	sub1 = rospy.Subscriber("abhiyaan/pose", Pose, callback1)
	vel=Twist()
	
	vel.linear.x=2
	vel.linear.y=0
	vel.linear.z=0
	vel.angular.x=0
	vel.angular.y=0
	vel.angular.z=0
	while not rospy.is_shutdown():
                while(((a1-a)**2)+((b1-b)**2)>=4):
			vel.angular.z=5*(np.arctan((b1-b)/(a1-a))-np.arctan(b1/a1))
			pub.publish(vel)
			
                vel.angular.z=0
		vel.linear.x=0
		pub.publish(vel)
		exit()

if __name__=="__main__":
	try:
		movement()
	except rospy.ROSInterruptException:
		pass
