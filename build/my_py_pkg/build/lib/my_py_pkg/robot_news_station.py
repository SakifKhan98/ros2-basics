#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class RobotNewsStationNode(Node): # Create a custom node class that inherits from rclpy.node.Node
    def __init__(self):
        super().__init__('robot_news_station')

        self.robot_name = 'C3PO'
        self.publisher_ = self.create_publisher(String, 'robot_news', 10)
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info('Robot News Station has been started.')

    def publish_news(self):
        msg = String()
        msg.data = f'Hi, this is {self.robot_name} from the robot news station'
        self.publisher_.publish(msg)
        # self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode() # Create an instance of the custom node class
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()