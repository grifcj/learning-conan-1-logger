cmake_minimum_required(VERSION 3.13)
project(logger)

enable_testing()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(libName ${PROJECT_NAME})
add_library(${libName} logger.cpp)
target_include_directories(${libName} PUBLIC ${CMAKE_CURRENT_LIST_DIR})

set(testName ${PROJECT_NAME}_unittest)
add_executable(${testName} logger-test.cpp)
target_link_libraries(${testName} PUBLIC CONAN_PKG::gtest)
add_test(NAME ${testName} COMMAND $<TARGET_FILE:${testName}>)

