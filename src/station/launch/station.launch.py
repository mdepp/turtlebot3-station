from launch_ros.actions import Node

from launch import LaunchDescription


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="image_transport",
                executable="republish",
                arguments=["theora"],
                namespace="station/camera/rgb",
                remappings=[("in/theora", "/camera/rgb/image_raw/theora")],
            ),
            Node(
                package="image_transport",
                executable="republish",
                arguments=["theora"],
                namespace="station/camera/depth",
                remappings=[("in/theora", "/camera/depth/image_raw/theora")],
            ),
        ]
    )
