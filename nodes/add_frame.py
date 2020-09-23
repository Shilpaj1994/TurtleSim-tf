#!/usr/bin/env python

import roslib
import rospy
import tf
import math
import random
import rosnode
from Turtle import *
from std_msgs.msg import Int64


class Frame:
    def __init__(self):
        rospy.init_node('spawner', anonymous=False)

        names = rosnode.get_node_names()
        print(names)
        # rospy.loginfo("Node Created: ", name)

        self.pub = rospy.Publisher('/data', Int64, queue_size=1)

        # self.br = tf.TransformBroadcaster()
        #
        # self.x = 0.0
        # self.y = 0.0
        # self.theta = 0.0
        #
        # self.random_spawn()
        #
        # self.br = tf.TransformBroadcaster()

        param = rospy.get_param('/par')
        rospy.loginfo("Parameter Name: " + str(param))
        self.rate = rospy.Rate(10.0)

        while not rospy.is_shutdown():
            # self.dynamic_frame()
            self.pub.publish(1)
            self.rate.sleep()

    def random_spawn(self):
        collection = []
        for i in range(5):
            collection.append(Turtle(i))

            self.rand_pos()

            collection[i].spawn(self.x, self.y, self.theta)
            print(collection[i].get_name())

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

    def dynamic_frame(self):
        t = rospy.Time.now().to_sec() * math.pi
        self.br.sendTransform((2.0 * math.sin(t), 2.0 * math.cos(t), 0.0),
                              (0.0, 0.0, 0.0, 1.0),
                              rospy.Time.now(),
                              "carrot1",
                              "turtle1")


if __name__ == '__main__':
    try:
        turtle = Frame()
    except KeyboardInterrupt:
        exit()
