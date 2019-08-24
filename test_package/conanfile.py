import os
import platform
from conans import ConanFile, tools, CMake


class GoPiGo(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        # handle this better in the future
        if "arm" in self.settings.arch and "arm" not in platform.machine():
            print("checking the existence of binary")
            assert os.path.exists("bin/basic_test_all")
        else:
            os.chdir("bin")
            self.run(".%sbasic_test_all" % os.sep)
