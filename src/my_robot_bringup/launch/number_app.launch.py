from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    number_publisher_node = Node(
        package='my_py_pkg',
        executable='number_publisher',
        name='my_number_publisher_node',
        output='screen',
        parameters=[
            {'number_to_publish': 40},
            {'publish frequence': 5.0}
        ],
        remappings=[
            ('number', 'my_number')
        ]
    )

    number_counter_node = Node(
        package='my_py_pkg',
        executable='number_counter',
        name='my_number_counter_node',
        output='screen',
        parameters=[
            {'param_name': 'param_value'}
        ],
        remappings=[
            ('number', 'my_number'),
            ('number_count', 'my_number_count')
        ]
    )


    ld.add_action(number_counter_node)
    ld.add_action(number_publisher_node)
    return ld







# def generate_launch_description():
#     return LaunchDescription([
#         Node(
#             package='my_robot_bringup',
#             executable='number_app',
#             name='number_app_node',
#             output='screen',
#             parameters=[
#                 {'param_name': 'param_value'}
#             ],
#             remappings=[
#                 ('/old_topic', '/new_topic')
#             ]
#         )
#     ])