#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__('py_test') # Create a node with the name 'py_test'
        self.counter_ = 0
        self.get_logger().info('Halum, ROS2!!')
        self.create_timer(1.0, self.timer_callback)  # Create a timer with a period of 1 second

    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info(f'Halum, {self.counter_}')

def main(args=None):
    rclpy.init(args=args)  # Initialize the rclpy library
    node = MyNode()  # Create a node using the MyNode class
    rclpy.spin(node)  # Keep the node running until it is shutdown
    rclpy.shutdown()  # Shutdown the rclpy library

if __name__ == '__main__':
    main()