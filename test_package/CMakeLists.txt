cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

find_package(logger REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example logger::logger)

enable_testing()
add_test(NAME example
         COMMAND $<TARGET_FILE:example>)
set_tests_properties(
	example
	PROPERTIES
	PASS_REGULAR_EXPRESSION "Hello!")
