cmake_minimum_required(VERSION 3.13)
project(logger)

add_executable(logger logger.cpp)
target_include_directories(
	logger
	PUBLIC
		$<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}/include>
		$<INSTALL_INTERFACE:include>
	)
