#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class SquareDrawerNode(Node):
    def __init__(self):
        super().__init__("square_drawer")
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.draw_square()

    def draw_square(self):
        cmd = Twist()
        side_length = 2.0  
        turn_duration = 1.0  

        for _ in range(4):
            
            cmd.linear.x = 1.0
            cmd.angular.z = 0.0
            self.publisher_.publish(cmd)
            time.sleep(side_length)

            cmd.linear.x = 0.0
            self.publisher_.publish(cmd)
            time.sleep(0.5)

            cmd.angular.z = 1.57
            self.publisher_.publish(cmd)
            time.sleep(turn_duration)

            cmd.angular.z = 0.0
            self.publisher_.publish(cmd)
            time.sleep(0.5)

        cmd.linear.x = 0.0
        cmd.angular.z = 0.0
        self.publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = SquareDrawerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
