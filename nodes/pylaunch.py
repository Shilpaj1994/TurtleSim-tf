#!/usr/bin/env python
import roslaunch
import time


class Node:
    def __init__(self, name, package, executable, output):
        self.name = name
        self.package = package
        self.executable = executable
        self.output = output
        self.process = None

        self._launch = roslaunch.scriptapi.ROSLaunch()

        self._node = roslaunch.core.Node(package=self.package, node_type=self.executable, name=self.name, namespace='/',
                                         machine_name=None, args='',
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


def main():
    package = 'turtlesim-tf'
    executable = 'add_frame.py'
    output = 'screen'
    name = 'Turtle'

    node1 = Node(name, package, executable, output)

    node1.launch()
    print(node1.status())
    time.sleep(10)
    node1.kill()
    print("END")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
