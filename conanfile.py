from conans import CMake, python_requires

base = python_requires("conanbase/[*]@grifcj/stable")

class LoggerConan(base.get_conanfile()):
    name = "logger"
    version = base.get_version()
    scm = {
        "type": "git",
        "url": "https://github.com/grifcj/cmake-logger",
        "revision": "auto"
    }
    build_requires = (
            "cmake-modules/[*]@grifcj/stable",
            "gtest/1.8.1@bincrafters/stable")
    keep_imports = True

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def imports(self):
        self.copy("*.cmake", dst="", src="", folder=True)

    def package_info(self):
        self.cpp_info.libs = ["logger"]

