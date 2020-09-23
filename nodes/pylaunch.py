#!/usr/bin/env python
import roslaunch
import time

package = 'turtlesim-tf'
executable = 'add_frame.py'
# node = roslaunch.core.Node(package, executable, name="PyNode")

nodes = []

for i in range(5):
    nodes.append(roslaunch.core.Node(package, node_type=executable, name='Py'+str(i), namespace='/',
                                     machine_name=None, args='',
                                     respawn=False, respawn_delay=0.0,
                                     remap_args=None, env_args=None, output=None, cwd=None,
                                     launch_prefix=None, required=False, filename=executable))

launch = roslaunch.scriptapi.ROSLaunch()
launch.start()

for i in range(5):
    process = launch.launch(nodes[i])
time.sleep(15)
print("Exit")
exit()
# print(process.is_alive())
# process.stop()
