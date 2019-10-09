from conans import python_requires

base = python_requires("conanbase/[*]@grifcj/stable")

class LoggerConan(base.get_conanfile()):
    name = "logger"
    version = base.get_version()
    scm = {
        "type": "git",
        "url": "https://github.com/grifcj/cmake-logger",
        "revision": "auto"
    }
    build_requires = "gtest/1.8.1@bincrafters/stable"

    def package_info(self):
        self.cpp_info.libs = ["logger"]

