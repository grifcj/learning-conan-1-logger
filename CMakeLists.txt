cmake_minimum_required(VERSION 3.13)
project(logger)

enable_testing()

if (${PROJECT_NAME} STREQUAL ${CMAKE_PROJECT_NAME})
   include(FetchContent)
   FetchContent_Declare(googletest
      URL https://github.com/google/googletest/archive/release-1.8.0.zip
      )
   FetchContent_GetProperties(googletest)
   if (NOT googletest_POPULATED)
      FetchContent_Populate(googletest)
      add_subdirectory(${googletest_SOURCE_DIR} ${googletest_BINARY_DIR} EXCLUDE_FROM_ALL)
   endif()
endif()

add_library(${PROJECT_NAME} logger.cpp)

set(testName ${PROJECT_NAME}_unittest)
add_executable(${testName} logger-test.cpp)
target_link_libraries(${testName} PUBLIC gmock gmock_main)
add_test(${testName} ${testName})
