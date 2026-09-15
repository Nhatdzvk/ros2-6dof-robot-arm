# ros2-6dof-robot-arm

Dự án phát triển, mô phỏng và điều khiển cánh tay robot 6 bậc tự do (6-DOF) sử dụng nền tảng ROS 2 (Humble).

## Kiến trúc hệ thống (Packages)

Dự án được chia thành các package sau để đảm bảo tính module hóa:

* **`ros2_6dof_description`**: Chứa mô hình URDF/Xacro, định nghĩa ma trận DH và thông số vật lý của robot.
* **`ros2_6dof_gazebo`**: Cấu hình môi trường và các plugin mô phỏng trên Gazebo.
* **`ros2_6dof_control`**: Các node xử lý động học (Kinematics) và điều khiển joint.
* **`ros2_6dof_moveit_config`**: Tích hợp MoveIt 2 để lập kế hoạch quỹ đạo (Motion Planning).
* **`ros2_6dof_bringup`**: Các file launch để khởi chạy toàn bộ hệ thống (RViz2, Gazebo, Controllers).

## Yêu cầu hệ thống
* Hệ điều hành: Ubuntu 22.04
* Framework: ROS 2 Humble
* Các công cụ khác: Gazebo, RViz2, MoveIt 2

## Hướng dẫn cài đặt (Sẽ cập nhật)
Đang trong quá trình phát triển. Quá trình clone và build bằng `colcon` sẽ được bổ sung sau khi hoàn thiện cấu trúc base.
