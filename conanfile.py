import os
from conans import CMake, python_requires

base = python_requires("conanbase/1.0.0-nightly@grifcj/dev")

class LoggerConan(base.get_conanfile()):
    name = "logger"
    version = "1.0.0-nightly"
    scm = {
        "type": "git",
        "url": "https://github.com/grifcj/cmake-logger",
        "revision": "auto"
    }
    build_requires = (
            "cmake_extensions/1.0.0-nightly@grifcj/dev",
            "gtest/1.8.1@bincrafters/stable")

