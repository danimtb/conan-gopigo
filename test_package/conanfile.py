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
        if platform.system () != self.settings.os:
            assert os.path.exists("bin/basic_test_all")
        else:
            os.chdir("bin")
            self.run(".%sbasic_test_all" % os.sep)
