#!/usr/bin/env python3
import sys

import rclpy
from rclpy.node import Node
from test_msgs.srv import Empty

class TestClient(Node):
    def __init__(self):
        super().__init__('test_client')
        self.client = self.create_client(Empty, 'my_service')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('my_service not available, waiting...')

    def spin(self):
        self.future = self.client.call_async(Empty.Request())
        while rclpy.ok():
            print("spinning...")
            rclpy.spin_once(self)
            if self.future.done():
                if self.future.result() is not None:
                    self.get_logger().info('hooray got service result')
                else:
                    self.get_logger.info('oh noes, service failed')
                break

if __name__ == '__main__':
    rclpy.init()
    node = TestClient()
    node.spin()
