#to create a catkin workspace: run these in terminal
#mkdir -p ~/catkin_ws/src
#cd ~/catkin_ws/
#catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
#source devel/setup.bash
# run "roscore" in a new terminal
# create the file in catkin workspace only, by "cd ~/catkin_ws/src"
# nano publisher.py
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher("/welcome_message",String,queue_size=10)
	rospy.init_node("publisher")
	rate= rospy.Rate(2)
	while not rospy.is_shutdown():
		str="Welcome to Abhiyaan"
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
#make sure to source your env by"source ./catkin_ws/devel/setup.sh
