cmake_minimum_required(VERSION 3.8)
project(ros2_6dof_bringup)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

# Đăng ký copy thư mục launch khi build
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
