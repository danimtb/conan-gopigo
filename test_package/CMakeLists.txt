cmake_minimum_required(VERSION 3.0)
project(gopigo VERSION 2.4.2)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(basic_test_all basic_test_all.cpp)
target_link_libraries(basic_test_all ${CONAN_LIBS})