#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyCustomNode(Node): # Create a custom node class that inherits from rclpy.node.Node
    def __init__(self):
        super().__init__('node_name')
        self.get_logger().info('Template node has been started.')

    def timer_callback(self):
        self.get_logger().info('Timer callback triggered.')

def main(args=None):
    rclpy.init(args=args)
    node = MyCustomNode() # Create an instance of the custom node class
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()