# Stonefish Resources
This repository contains scenarios, data and launch files useful for simulations in Stonefish (actually based on v 1.3.0)
There are some python scripts useful for starting practicing with the simulator, used to control the robot through joystick, propagating the odometry to the tfs .... 
> [!IMPORTANT] 
> Use this in combination with stonefish_ros2 from https://github.com/Michele1996/hw_stonefish_ros2

## Instructions
To launch bluerov sim :
```bash
ros2 launch stonefish_resources bluerov_simulation.launch 
```
To launch blueboat and bluerov sim :
```bash
ros2 launch stonefish_resources asv_usv_sim.launch 
```
To move the bluerov use thrusters:
```bash
ros2 topic pub /bluerov/controller/thruster_setpoints_sim std_msgs/Float64MultiArray '{data:[0.01, 0.01, 0.01, 0.01, 0.4, 0.4]}'
```
To move the blueboat use thrusters:
```bash
ros2 topic pub /blueboat/controller/thruster_setpoints_sim std_msgs/Float64MultiArray '{data:[0.01, 0.01]}'
```
Thrusters order is the same as in the scenario file

## Examples

### Examples : BlueROV
To go down:
```bash
ros2 topic pub /bluerov/controller/thruster_setpoints_sim std_msgs/Float64MultiArray '{data:[0.0, 0.0, 0.0, 0.0, 0.7, 0.7]}'
```
Stay at a stable depth:
```bash
ros2 topic pub /bluerov/controller/thruster_setpoints_sim std_msgs/Float64MultiArray '{data:[0.0, 0.0, 0.0, 0.0, 0.4, 0.4]}'
```
### Examples : BlueROV Stereo
To use the StereoCamera config, launch
```bash
ros2 launch stonefish_resources bluerov_stereo_simulation.launch
```
### Examples : BlueROV FLS
To use the FLS config, launch
```bash
ros2 launch stonefish_resources bluerov_fls_sim.launch
```
### Instructions OpenGym
To launch bluerov opengym :
```bash
ros2 launch stonefish_resources bluerov_simulation_opengym.launch 
```
To launch bluerov opengym headless mode :
```bash
ros 2launch stonefish_resources bluerov_simulation_opengym_nogui.launch
```

### Turtlebot Example
To use the turtlebot with the arm launch: 
```bash
ros2 launch stonefish_resources turtlebot_switfpro_kobuki.launch.py 
```
To move the robot use: 
```bash
ros2 topic pub /turtlebot/controller/servo_setpoints_sim sensor_msgs/msg/JointState "header:
  stamp:
    sec: 0
    nanosec: 0
  frame_id: 'turtlebot'
name: ['turtlebot/kobuki/wheel_left_joint', 'turtlebot/kobuki/wheel_right_joint']
position: []
velocity: [1.5, 1.5]
effort: []"   
```
