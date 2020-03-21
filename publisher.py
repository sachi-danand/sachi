#!/usr/bin/env python
# run roscore in a new terminal
# create the file in catkin workspace only by "cd ~/catkin_ws/src
# nano publisher.py
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher("/welcome_message",String,queue_size=10)
	rospy.init_node("publisher")
	rate= rospy.Rate(2)
	while not rospy.is_shutdown():
		str="Welcome to Abhiyaan %s" %rospy.get_time()
		rospy.loginfo(str)
		pub.publish(str)
		rate.sleep()


if __name__=='__main__':
	try:
		talker()

	except rospy.ROSInerruptException:
		pass

#make the file executable by
#$chmod +x publisher.py
