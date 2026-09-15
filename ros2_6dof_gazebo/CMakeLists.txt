cmake_minimum_required(VERSION 3.8)
project(ros2_6dof_gazebo)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

# Đăng ký copy các thư mục cấu hình khi build code
install(
  DIRECTORY launch worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
