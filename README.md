(Main) 

Adaptive Speed Control- Adjust speed based on terrain complexity.

STEP 1: Place the robot in the middle bottom facing the middle of the town.

STEP 2: Open the Terminal. 
Run this code:

git clone https://github.com/juxzpc/my-ros-project

chmod +x ./packages/my_package/src/my_publisher_node.py

dts devel build -f

Change the name of the robot (myroko) [to the robot you are using currently] inside of this file (packages -> my-packages -> src -> adaptive_speed_node.py)

dts devel run -H [Robot] -L my-publisher


(Optional) (If "Main" doesn't work)

Path following with Error Correction.

dts duckiebot demo --demo_name lane_following --duckiebot_name [Robot] --package_name duckietown_demos

dts duckiebot keyboard_control [Robot]

and press A to start and S to finish

Finish.
