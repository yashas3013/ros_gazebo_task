# Simulation test bench for Pratham


## Build
1. clone this [repo](https://github.com/pratham-reloaded/igvc_simulation.git).
1. copy the  contents meshes file to ~/.gazebo/models
2. colcon build
3. source workspace

## Run
```bash
ros2 launch igvc_world world.launch.py
```
---
![image](https://github.com/yashas3013/ros_gazebo_task/assets/40001795/283d2503-ce10-46e1-a4b1-04ee24ff9612)

## Task :
1. Add lidar sensor to the bot.
2. Add diffrential drive to the bot.
3. Make to move using cmd_vel.
