cmake_minimum_required(VERSION 3.13)
project(logger-super)

include(FindSourcePackage)
declare_source_package(logger)

add_subdirectory(src)

include(CTest)
if (BUILD_TESTING)
	add_subdirectory(test)
endif()

