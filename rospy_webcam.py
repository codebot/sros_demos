#!/usr/bin/env python
import cv2
import sys
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

if __name__ == '__main__':
    rospy.init_node('rospy_webcam')
    cap = cv2.VideoCapture(0)
    image_pub = rospy.Publisher('image', Image, queue_size=1)
    bridge = CvBridge()
    while not rospy.is_shutdown():
        ret, cv_image = cap.read()
        image_pub.publish(bridge.cv2_to_imgmsg(cv_image, 'bgr8'))
    cap.release()
