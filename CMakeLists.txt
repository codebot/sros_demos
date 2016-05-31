cmake_minimum_required(VERSION 2.8.3)
project(sros_demos)

find_package(catkin REQUIRED COMPONENTS message_generation std_msgs sensor_msgs)

catkin_package(CATKIN_DEPENDS message_runtime std_msgs sensor_msgs)

catkin_install_python(PROGRAMS
  rospy_webcam.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/rospy_webcam
)

catkin_install_python(PROGRAMS
  rospy_image_view.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/rospy_image_view
)
