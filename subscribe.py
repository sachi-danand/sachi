#change directory to catkin_ws/src
#cd ~/catkin_ws/src
#!/usr/bin/env python
import rospy 
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "   %s",data.data)

def listener():
	rospy.init_node("receivedmsg")
	rospy.Subscriber("/welcome_message",String,callback)
	rospy.spin()

if __name__=="__main__":
	listener()

# make the file executable 
#chmod +x subscribe.py
