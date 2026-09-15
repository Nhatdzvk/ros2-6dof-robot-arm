import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Lấy đường dẫn đến module gazebo của chúng ta
    gazebo_pkg_dir = FindPackageShare('ros2_6dof_gazebo').find('ros2_6dof_gazebo')
    
    # Kịch bản gọi Gazebo
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_pkg_dir, 'launch', 'gazebo.launch.py')
        )
    )

    return LaunchDescription([
        gazebo_launch,
        # (Sau này sẽ thêm các kịch bản gọi RViz2 và Controller tại đây)
    ])
