cmake_minimum_required(VERSION 3.13)
project(logger VERSION ${CONAN_PACKAGE_VERSION})

add_library(logger logger.cpp)
target_include_directories(
   logger
   PUBLIC
      $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}/include>
      $<INSTALL_INTERFACE:include>
)
add_library(logger::logger ALIAS logger)

include(CMakeExtensions)
install_project()
