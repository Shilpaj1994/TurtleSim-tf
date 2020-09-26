#!/usr/bin/env python

import roslib
import rospy
import tf
import math
import random
from Turtle import *
from std_msgs.msg import Int64


class Frame:
    def __init__(self, value):
        rospy.init_node('turtle', anonymous=False)
        rospy.loginfo("Node Initialized")
        rospy.loginfo(str(value))

        self._instance_number = value

        self.br = tf.TransformBroadcaster()
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.rate = rospy.Rate(10.0)
        self.turtle = None

        # Spawn turtles randomly
        self.random_spawn_test()

        # Initiate topic for each node
        topic_name = '/Turtle' + str(self._instance_number) + '/tf'
        self.pub = rospy.Publisher(topic_name, Int64, queue_size=1)

        while not rospy.is_shutdown():
            self.dynamic_frame()
            self.pub.publish(1)
            self.rate.sleep()

    def random_spawn(self):
        self.turtle = Turtle(self._instance_number)

        self.rand_pos()

        self.turtle.spawn(self.x, self.y, self.theta)
        print(self.turtle.get_name())

    def random_spawn_test(self):
        collection = []
        for i in range(self._instance_number):
            collection.append(Turtle(i))

            self.rand_pos()

            collection[i].spawn(self.x, self.y, self.theta)
            print(collection[i].get_name())

    def rand_pos(self):
        self.x = random.randint(0, 11)
        self.y = random.randint(0, 11)
        self.theta = random.random()

    def dynamic_frame(self):
        t = rospy.Time.now().to_sec() * math.pi
        self.br.sendTransform((2.0 * math.sin(t), 2.0 * math.cos(t), 0.0),
                              (0.0, 0.0, 0.0, 1.0),
                              rospy.Time.now(),
                              "turtle"+str(self._instance_number),
                              "world")


def main(value):
    try:
        # reset_sim()
        Frame(value)
    except KeyboardInterrupt:
        exit()


if __name__ == '__main__':
    main(int(sys.argv[1]))
