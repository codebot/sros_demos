#!/usr/bin/env python
import cv2
import sys
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bridge = CvBridge()

def image_cb(ros_image):
    global bridge
    cv_image = bridge.imgmsg_to_cv2(ros_image, 'bgr8')
    cv2.imshow('rospy_image_view', cv_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        rospy.signal_shutdown('q pressed in image_view window')

if __name__ == '__main__':
    rospy.init_node('rospy_image_view')
    image_sub = rospy.Subscriber('image', Image, image_cb)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('bye')
