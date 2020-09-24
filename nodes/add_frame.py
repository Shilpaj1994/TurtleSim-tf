#!/usr/bin/env python

import roslib
import rospy
import tf
import math
import random
import rosnode
from Turtle import *
from std_msgs.msg import Int64


number = '0'


class Frame:
    def __init__(self):
        global number
        rospy.init_node('turtle', anonymous=False)
        rospy.loginfo("Node Initialized")

        self.br = tf.TransformBroadcaster()
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.rate = rospy.Rate(10.0)
        self.turtle = None

        # Spawn turtles randomly
        self.random_spawn_test()

        # Initiate topic for each node
        topic_name = '/Turtle' + str(number) + '/tf'
        self.pub = rospy.Publisher(topic_name, Int64, queue_size=1)

        while not rospy.is_shutdown():
            self.dynamic_frame()
            # self.pub.publish(1)
            self.rate.sleep()

    def random_spawn(self):
        global number
        self.turtle = Turtle(number)

        self.rand_pos()

        self.turtle.spawn(self.x, self.y, self.theta)
        print(self.turtle.get_name())

    def random_spawn_test(self):
        global number
        num = int(number)
        collection = []
        for i in range(num):
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
                              "turtle1", # self.turtle.get_name()
                              "world")


def main(value):
    global number
    number = value
    print(number)
    Frame()


if __name__ == '__main__':
    try:
        reset_sim()
        print("Here I am")
        main(int(sys.argv[1]))
        rospy.spin()
    except KeyboardInterrupt:
        exit()
