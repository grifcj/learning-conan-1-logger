cmake_minimum_required(VERSION 3.13)
project(logger)

find_package(gtest REQUIRED)

add_library(logger logger.cpp)
target_include_directories(logger PUBLIC ${CMAKE_CURRENT_LIST_DIR})

enable_testing()
add_executable(unittest logger-test.cpp)
target_link_libraries(unittest PUBLIC gtest::gtest)
add_test(NAME unittest COMMAND $<TARGET_FILE:unittest>)

