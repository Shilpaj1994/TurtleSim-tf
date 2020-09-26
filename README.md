# Project: TurtleSim-tf



## Overview

- In this project, multiple turtles are spawned in `turtlesim`
- Each turtle is broadcasting it's transform i.e. it's position and orientation to a centralized node
- The centralized node will calculate the relative distances and guide these turtles as they move from their source to destination



​                                                      [![tf-tree](./docs/tf-tree.gif)](https://www.youtube.com/watch?v=SILjfX5E-HQ&ab_channel=ShilpajBhalerao)



---



## Concepts Used

Following are the concepts used for this project:

- **ROSlaunch API**
  - To import  the image using path
  - To import the image using camera
  - To set thresholds for Canny edge detection 
- **ROS tf**
  - To set the values of threshold parameters
  - To fetch the  values of threshold parameters



---



## Directory Structure

- Following is the directory structure of the package
  ```txt
  .
  ├── CMakeLists.txt
├── docs                             # README dependencies
  │   ├── tf.png
  │   └── tree.txt
  ├── include
  │   └── TurtleSim-tf
  ├── launch                           # Launch files
  │   ├── dynamic.launch                 # Launch - Multiple instance of same node using launch file
  │   └── spawn.launch                   # Launch - Multiple turtles in a turtlesim using launch file
  |
  ├── nodes                            # ROS Nodes
  │   ├── add_frame.py                   # Blueprint of a node - spawn random turtles and broadcast transform
  │   ├── pylaunch.py                    # Launch multiple instances using ROSlaunch API
  │   └── Turtle.py                      # Turtle class to control turtle activities
  ├── package.xml
  ├── README.md
  └── src
  ```
  



---



## Coding Style Guide - PEP8



---



## Dependencies

- `ROS-tf2`  package
- `turtlesim` package



---



## Setup and Run

To run the project on your local system, follow the procedure:

- Download the packages - `turtlesim-tf`

- Copy these packages to your ROS workspace i.e. `~/ROS_ws/src/`

- Build the work-space
  - `$ cd ~/ROS_ws/` 
  - `$ catkin_make`

- Open new terminal and source the ROS workspace - `source ~/ROS_ws/devel/setup.bash`

- Run the command - `$ roslaunch turtlesim-tf xxxxxx.launch 5`

  - where 5 = number of turtle in a turtlesim

    > You can configure this number

- In a new terminal, run the command - `$ rqt_tf_tree` to display the `tf-tree`

  ![](./docs/tf.png)

  



---



## Article

[<img src="https://cdn.mos.cms.futurecdn.net/xJGh6cXvC69an86AdrLD98-320-80.jpg" style="zoom: 70%;">]()



---



## Contact

[<img src="https://github.com/Shilpaj1994/TurtleSim-Sketch/blob/master/docs/linkedin_logo.png?raw=true" alt="LinkedIn Logo" style="zoom: 25%;" />](https://www.linkedin.com/in/shilpaj-bhalerao/)[<img src="https://github.com/Shilpaj1994/TurtleSim-Sketch/blob/master/docs/github_logo.png?raw=true" style="zoom: 15%;">](https://github.com/Shilpaj1994) [<img src="https://github.com/Shilpaj1994/TurtleSim-Sketch/blob/master/docs/youtube_logo.png?raw=true" style="zoom: 35%;">](https://www.youtube.com/channel/UCucf49_Iau18mG5YFFCSpmw?view_as=subscriber)