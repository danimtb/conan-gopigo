cmake_minimum_required(VERSION 3.0)
project(gopigo VERSION 2.4.2)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include_directories(.)
add_library(gopigo3 GoPiGo3.cpp)