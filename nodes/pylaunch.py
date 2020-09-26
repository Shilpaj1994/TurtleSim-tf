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
        """
        Method to define a ROS node
        """
        self._node = roslaunch.core.Node(package=self._package, node_type=self._executable, name=self._name, namespace='/',
                                         machine_name=None, args=str(self._instance_num),
                                         respawn=False, respawn_delay=0.0,
                                         remap_args=None, env_args=None, output='screen', cwd=None,
                                         launch_prefix=None, required=False, filename='<unknown>')

    def launch(self):
        """
        Method to launch a ROS Node
        """
        self._launch.start()
        self._process = self._launch.launch(self._node)

    def kill(self):
        """
        Method to kill a node
        """
        self._process.stop()

    def status(self):
        """
        Method to check activity status of the node
        """
        if self._process.is_alive():
            return "Alive"
        else:
            return "Dead"
    # def set_name(self, name):
    #     self.name = name


def launch_sim():
    """
    Function to launch a turtle-sim node
    """
    package = 'turtlesim'
    executable = 'turtlesim_node'
    node = roslaunch.core.Node(package, executable)

    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()

    launch.launch(node)


def main(number_of_nodes):
    """
    Main function to launch multiple instance of a single node
    """
    # Initialize a ROS node to launch other nodes
    rospy.init_node("Launcher")

    # Rate of execution
    rate = rospy.Rate(15.0)

    # List to perform operations on a node
    node_collections = []

    try:
        launch_sim()

        package = 'turtlesim-tf'
        executable = 'add_frame.py'

        # For given number of instances
        for i in range(1, number_of_nodes+1):
            name = 'Turtle' + str(i)
            node_collections.append(Node(name_arg=name,
                                         package_arg=package,
                                         executable_arg=executable,
                                         instance_arg=i))

            # Define Nodes
            node_collections[-1].define_node()

            # Launch Nodes
            node_collections[-1].launch()

        while not rospy.is_shutdown():
            rate.sleep()

        print("Exiting the process ....")

    except KeyboardInterrupt:
        # Kill nodes on exit
        for j in range(len(node_collections)):
            node_collections[-1].kill()
        exit()


if __name__ == '__main__':
    main(int(sys.argv[1]))
