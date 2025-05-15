#!/usr/bin/env python3
import rospy
from duckietown_msgs.msg import Twist2DStamped
import time

def move_robot():
    rospy.init_node('duckiebot_controller', anonymous=True)
    
    # Change 'duckiebot' to your actual bot name
    pub = rospy.Publisher('/duckiebot/car_cmd_switch_node/cmd', Twist2DStamped, queue_size=10)
    cmd = Twist2DStamped()

    # --- Step 1: Move straight fast for 10 seconds ---
    cmd.v = 0.6  # linear velocity (forward)
    cmd.omega = 0.0  # angular velocity (no turn)
    start_time = time.time()
    while time.time() - start_time < 3.2:
        pub.publish(cmd)
        rospy.sleep(0.1)

    # --- Step 2: Turn right 90 degrees slowly ---
    cmd.v = 0.2  # slower linear speed
    cmd.omega = -2.0  # negative for right turn
    start_time = time.time()
    while time.time() - start_time < 3.8:  # adjust timing to match 90° turn
        pub.publish(cmd)
        rospy.sleep(0.1)

    # --- Step 3: Move straight fast for 4 seconds ---
    cmd.v = 0.6
    cmd.omega = 0.0
    start_time = time.time()
    while time.time() - start_time < 4:
        pub.publish(cmd)
        rospy.sleep(0.1)


    cmd.v = 0.2  # slower linear speed
    cmd.omega = -2.0  # negative for right turn
    start_time = time.time()
    while time.time() - start_time < 3.8:  # adjust timing to match 90° turn
        pub.publish(cmd)
        rospy.sleep(0.1)


    # --- Stop the robot ---
    cmd.v = 0.0
    cmd.omega = 0.0
    pub.publish(cmd)

if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass
