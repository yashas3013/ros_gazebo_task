import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
def generate_launch_description():

    package_dir=get_package_share_directory('igvc_world')
    world_file = os.path.join(package_dir,'worlds','gaz.world')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    urdf_file_name = os.path.join(package_dir,'urdf','husky.urdf.xacro')


    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose',world_file, '-s', 'libgazebo_ros_factory.so'],
            output='screen'),
        ExecuteProcess(
            cmd=['ros2', 'param', 'set', '/gazebo', 'use_sim_time', 'True'],
            output='screen'),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': True}],
            arguments=[urdf_file_name]),
        
        
    ])