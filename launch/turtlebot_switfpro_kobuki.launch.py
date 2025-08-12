import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Declare launch arguments
    robot_name_arg = DeclareLaunchArgument(
        'robot_name',
        default_value='bluerov',
        description='Name of the robot'
    )

    # Group action with namespace
    namespace_action = GroupAction(
        actions=[
            # Include the simulator launch file
            IncludeLaunchDescription(
                PathJoinSubstitution([
                    FindPackageShare('stonefish_ros2'), 'launch', 'stonefish_simulator.launch.py'
                ]),
                launch_arguments={
                    'simulation_data': PathJoinSubstitution([
                        FindPackageShare('stonefish_resources'), 'data'
                    ]),
                    'scenario_desc': PathJoinSubstitution([
                        FindPackageShare('stonefish_resources'), 'scenarios', 'turtlebot_integration.scn'
                    ]),
                    'simulation_rate': '100.0',
                    'window_res_x': '1200',
                    'window_res_y': '800',
                    'rendering_quality': 'high'
                }.items()
            ),
        ]
    )

    # Static transforms
    world_to_ned_transform = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='world2ned',
        output='screen',
        arguments=['0', '0', '0', '0', '0', '3.1415', 'world', 'world_ned']
    )


    # Define and return the LaunchDescription
    return LaunchDescription([
        robot_name_arg,
        namespace_action,
        # Additional nodes for teleoperation and transforms
        #Node(
        #    package='joy',
        #    executable='joy_node',
        #    output='screen',
        #),
        #Node(
        #    package='stonefish_resources',
        #    executable='bluerov2_logitechF310teleop.py',
        #    output='screen',
        #),
        #Node(
        #    package='stonefish_resources',
        #    executable='odom2tf.py',
        #    output='screen',
        #),
        # Static transforms
        world_to_ned_transform,
    ])

