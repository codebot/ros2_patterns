#!/usr/bin/env python3
from test_msgs.srv import Empty

import rclpy

def service_cb(request, response):
    print("service_cb()")
    return response

if __name__ == '__main__':
    rclpy.init()
    node = rclpy.create_node('test_service')
    srv = node.create_service(Empty, 'my_service', service_cb)
    rclpy.spin(node)
