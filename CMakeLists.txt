cmake_minimum_required(VERSION 3.13)
project(logger)

if (NOT TARGET gtest::gtest)
   find_package(gtest REQUIRED)
endif()

add_library(logger logger.cpp)
target_include_directories(logger
   PUBLIC
      $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}>
      # Install interface must match package directory in conanfile.py
      $<INSTALL_INTERFACE:include>)
add_library(logger::logger ALIAS logger)

get_property(exclude DIRECTORY ${PROJECT_SOURCE_DIR} PROPERTY EXCLUDE_FROM_ALL SET)
if (NOT exclude)
   enable_testing()
   add_executable(logger_unittest logger-test.cpp)
   target_link_libraries(logger_unittest PUBLIC logger gtest::gtest)
   add_test(NAME logger::unittest COMMAND $<TARGET_FILE:logger_unittest>)
endif()

