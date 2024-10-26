from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    robot_names = ['Giskard', 'R2D2', 'C3PO', 'Wall_E', 'Baymax']
    robot_news_station_nodes = []

    for name in robot_names:
        station = Node(
            package='my_py_pkg',
            executable='robot_news_station',
            name='robot_news_station_' + name.lower(),
            output='screen',
            parameters=[
                {'robot_name': name},
            ]
        )
        robot_news_station_nodes.append(station)

    smartphone = Node(
        package='my_py_pkg',
        executable='smartphone',
        name='smartphone_node',
        output='screen',
    )

    for node in robot_news_station_nodes:
        ld.add_action(node)
    ld.add_action(smartphone)
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