cmake_minimum_required(VERSION 3.13)
project(logger-test)

find_package(logger REQUIRED)
find_package(gtest REQUIRED)

add_executable(logger_unittest unittest.cpp)
target_link_libraries(logger_unittest PUBLIC logger::logger gtest::gtest)
add_test(NAME logger::unittest COMMAND $<TARGET_FILE:logger_unittest>)



