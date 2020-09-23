#!/usr/bin/env python
import roslaunch

package = 'turtlesim-tf'
executable = 'add_frame.py'
node = roslaunch.core.Node(package, executable)

launch = roslaunch.scriptapi.ROSLaunch()
launch.start()

process = launch.launch(node)
print(process.is_alive())
process.stop()
