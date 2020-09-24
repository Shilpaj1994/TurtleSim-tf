#!/usr/bin/env python
import roslaunch
import rospy
import time
import sys


class Node:
    def __init__(self, name_arg, package_arg, executable_arg, output_arg, args_arg=''):
        self.name = name_arg
        self.package = package_arg
        self.executable = executable_arg
        self.output = output_arg
        self.args = args_arg
        self.process = None

        self._launch = roslaunch.scriptapi.ROSLaunch()

        self._node = roslaunch.core.Node(package=self.package, node_type=self.executable, name=self.name, namespace='/',
                                         machine_name=None, args=self.args,
                                         respawn=False, respawn_delay=0.0,
                                         remap_args=None, env_args=None, output=None, cwd=None,
                                         launch_prefix=None, required=False, filename=self.executable)

    def launch(self):
        self._launch.start()
        self.process = self._launch.launch(self._node)

    def kill(self):
        self.process.stop()

    def status(self):
        if self.process.is_alive():
            return "Alive"
        else:
            return "Dead"
    # def set_name(self, name):
    #     self.name = name


def main(number):
    rospy.init_node("Starter")

    package = 'turtlesim-tf'
    executable = 'add_frame.py'
    output = "screen"

    nodes = []

    for i in range(number):
        name = 'Turtle' + str(i)
        nodes.append(Node(name_arg=name,
                          package_arg=package,
                          executable_arg=executable,
                          output_arg=output))
        nodes[-1].launch()

    # for j in range(len(nodes)):
    #     nodes[j].launch()

    # node1.launch()
    # print(node1.status())
    time.sleep(10)
    # node1.kill()
    print("END")


if __name__ == '__main__':
    try:
        main(int(sys.argv[1]))
    except KeyboardInterrupt:
        exit()
