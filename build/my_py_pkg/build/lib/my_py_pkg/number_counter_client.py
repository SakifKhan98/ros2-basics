#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64


class NumberCounterClientNode(Node):
    def __init__(self):
        super().__init__("number_counter_client")

        self.subscriber_ = self.create_subscription(
            Int64, "number_count", self.callback_number_count, 10
        )
        self.get_logger().info("Number Counter Client has been started.")

    def callback_number_count(self, msg):
        self.get_logger().info(
            f"Received Number Count on Client: {msg.data} & Counting..."
        )


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterClientNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
