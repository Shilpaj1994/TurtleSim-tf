#!/usr/bin/env python
import roslaunch
import rospy
import sys


class Node:
    def __init__(self, name_arg, package_arg, executable_arg, instance_arg):
        self._name = name_arg
        self._package = package_arg
        self._executable = executable_arg
        self._instance_num = instance_arg

        self._launch = roslaunch.scriptapi.ROSLaunch()
        self._process = None
        self._node = None

    def define_node(self):
        self._node = roslaunch.core.Node(package=self._package, node_type=self._executable, name=self._name, namespace='/',
                                         machine_name=None, args=str(self._instance_num),
                                         respawn=False, respawn_delay=0.0,
                                         remap_args=None, env_args=None, output='screen', cwd=None,
                                         launch_prefix=None, required=False, filename='<unknown>')

    def launch(self):
        self._launch.start()
        self._process = self._launch.launch(self._node)

    def kill(self):
        self._process.stop()

    def status(self):
        if self._process.is_alive():
            return "Alive"
        else:
            return "Dead"
    # def set_name(self, name):
    #     self.name = name


def launch_sim():
    package = 'turtlesim'
    executable = 'turtlesim_node'
    node = roslaunch.core.Node(package, executable)

    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()

    launch.launch(node)


def main(number_of_nodes):
    rospy.init_node("Launcher")
    rate = rospy.Rate(15.0)

    node_collections = []
    try:
        launch_sim()

        package = 'turtlesim-tf'
        executable = 'add_frame.py'

        for i in range(1, number_of_nodes+1):
            name = 'Turtle' + str(i)
            node_collections.append(Node(name_arg=name,
                                         package_arg=package,
                                         executable_arg=executable,
                                         instance_arg=i))
            node_collections[-1].define_node()
            node_collections[-1].launch()

        while not rospy.is_shutdown():
            rate.sleep()

        print("Exiting the process ....")

    except KeyboardInterrupt:
        for j in range(len(node_collections)):
            node_collections[-1].kill()
        exit()


if __name__ == '__main__':
    main(int(sys.argv[1]))
