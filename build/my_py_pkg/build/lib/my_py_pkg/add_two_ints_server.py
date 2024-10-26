#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class AddTwoIntsServerNode(Node):
    def __init__(self):
        super().__init__('add_two_ints_server') # Create a node with the name 'py_test'
        self.server_ = self.create_service(AddTwoInts, 'add_two_ints', self.callback_add_two_ints)

    def callback_add_two_ints(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'Request: {request.a} + {request.b}')
        self.get_logger().info(f'Response: {response.sum}')
        return response

def main(args=None):
    rclpy.init(args=args)  # Initialize the rclpy library
    node = AddTwoIntsServerNode()  # Create a node using the MyNode class
    rclpy.spin(node)  # Keep the node running until it is shutdown
    rclpy.shutdown()  # Shutdown the rclpy library

if __name__ == '__main__':
    main()