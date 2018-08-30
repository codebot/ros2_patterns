#!/usr/bin/env python3
import sys

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from test_msgs.srv import Empty

class SubscriberClientAsync(Node):

    def __init__(self):
        super().__init__('sub_client_node')
        self.client = self.create_client(Empty, 'service')
        self.sub = self.create_subscription(String, 'topic', self.topic_cb)
        self.client_futures = []

    def topic_cb(self, msg):
        print("sub_cb({})".format(msg.data))
        self.client_futures.append(self.client.call_async(Empty.Request()))

    def spin(self):
        while rclpy.ok():
            rclpy.spin_once(self)
            incomplete_futures = []
            for f in self.client_futures:
                if f.done():
                    res = f.result()
                    print("received service result: {}".format(res))
                else:
                    incomplete_futures.append(f)
            self.client_futures = incomplete_futures

if __name__ == '__main__':
    rclpy.init()
    node = SubscriberClientAsync()
    node.spin()
