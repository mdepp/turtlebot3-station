from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="rviz2",
                executable="rviz2",
                arguments=[
                    "--display-config",
                    PathJoinSubstitution(
                        [FindPackageShare("station"), "rviz", "station.rviz"]
                    ),
                ],
            ),
        ]
    )
