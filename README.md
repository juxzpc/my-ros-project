(Main) 
Adaptive Speed Control- Adjust speed based on terrain complexity.
The project was supposed to be autonomous however it was decided to be manual.

STEP 1:
Open the Terminal. 
Run this code:

chmod +x ./packages/my_package/src/my_publisher_node.py

dts devel build -f

dts devel run -H myroko -L my-publisher

dts duckiebot demo --demo_name lane_following --duckiebot_name myroko --package_name duckietown_demos

dts duckiebot keyboard_control myroko

and press A to start and S to finish

Then, Proceed with


STEP 2: 
You will get a demo control on the screen. The speed is adjusted and increased.
Go ahead and control it around the town.

STEP 3:
In case of any errors restart the laptop.

(Optional) (If "Main" doesn't work)
Path following with Error Correction.

STEP 1:
Open the Terminal. Run this code:
dts duckiebot demo --demo_name lane_following --duckiebot_name myroko --package_name duckietown_demos

STEP 2:
The duckiebot will move and follow the lane.
