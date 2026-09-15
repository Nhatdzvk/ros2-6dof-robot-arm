from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    # Tìm đường dẫn đến package gazebo_ros mặc định của hệ thống
    gazebo_ros_pkg = FindPackageShare('gazebo_ros').find('gazebo_ros')
    
    # Khởi chạy môi trường Gazebo trống
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(gazebo_ros_pkg, 'launch', 'gazebo.launch.py')),
    )

    return LaunchDescription([
        gazebo_launch
    ])
