import rospy
from duckietown_msgs.msg import Twist2DStamped

class AdaptiveSpeedNode:
    def __init__(self):
        self.robot_name = "myroko" 

        # Subscribe to lane-following command output
        input_topic = f"/{self.robot_name}/lane_controller_node/car_cmd"
        rospy.Subscriber(input_topic, Twist2DStamped, self.cmd_callback)

        # Publish modified command to the robot's wheels
        output_topic = f"/{self.robot_name}/car_cmd_switch_node/cmd"
        self.pub = rospy.Publisher(output_topic, Twist2DStamped, queue_size=1)

        rospy.loginfo(f"[AdaptiveSpeedNode] Subscribed to {input_topic}, publishing to {output_topic}")

    def cmd_callback(self, msg):
        new_msg = Twist2DStamped()
        new_msg.header = msg.header
        new_msg.omega = msg.omega

        # Adjust speed: speed up when straight, slow down when turning
        if abs(msg.omega) < 0.3:
            new_msg.v = min(msg.v + 0.1, 0.6)
        else:

            new_msg.v = max(msg.v - 0.1, 0.1)

        self.pub.publish(new_msg)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('adaptive_speed_node')
    node = AdaptiveSpeedNode()
    node.run()
