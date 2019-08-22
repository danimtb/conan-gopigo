cmake_minimum_required(VERSION 3.0)
project(gopigo VERSION 2.4.1)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(gopigo gopigo.c)