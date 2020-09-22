#!/usr/bin/env python

import roslib
import rospy
import tf
import math
import random
from Turtle import *


class Frame:
    def __init__(self):
        rospy.init_node('Spawn')
        reset_sim()

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        self.br = tf.TransformBroadcaster()

        collection = []
        for i in range(5):
            collection.append(Turtle(i))

            self.rand_pos()

            collection[i].spawn(self.x, self.y, self.theta)
            print(collection[i].get_name())

        self.rate = rospy.Rate(10.0)

    def rand_pos(self):
        self.x = random.randint(0, 11)
        self.y = random.randint(0, 11)
        self.theta = random.random()

    # def static_frame(self):
    #     rospy.init_node('fixed_tf_broadcaster')
    #     br = tf.TransformBroadcaster()
    #     rate = rospy.Rate(10.0)
    #     while not rospy.is_shutdown():
    #         br.sendTransform((0.0, 2.0, 0.0),
    #                          (0.0, 0.0, 0.0, 1.0),
    #                          rospy.Time.now(),
    #                          "carrot1",
    #                          "turtle1")
    #         rate.sleep()
    #
    # def dynamic_frame(self):
    #     rospy.init_node('dynamic_tf_broadcaster')
    #     br = tf.TransformBroadcaster()
    #     rate = rospy.Rate(10.0)
    #     while not rospy.is_shutdown():
    #         t = rospy.Time.now().to_sec() * math.pi
    #         br.sendTransform((2.0 * math.sin(t), 2.0 * math.cos(t), 0.0),
    #                          (0.0, 0.0, 0.0, 1.0),
    #                          rospy.Time.now(),
    #                          "carrot1",
    #                          "turtle1")
    #         rate.sleep()


if __name__ == '__main__':
    try:
        Frame()
    except Exception as e:
        print(e)
