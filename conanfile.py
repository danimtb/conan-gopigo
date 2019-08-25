import os
import shutil
from conans import ConanFile, tools, CMake
from conans.errors import ConanInvalidConfiguration


class GoPiGo(ConanFile):
    name = "gopigo"
    version = "2.4.2"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "CMakeLists.txt"

    def configure(self):
        if self.settings.os != "Linux":
            raise ConanInvalidConfiguration("This library is only supported in Linux systems")

    def source(self):
        filename = "dexteros_%s" % self.version
        tools.get("https://github.com/DexterInd/GoPiGo3/archive/%s.zip" % filename)
        os.rename("GoPiGo3-%s" % filename, "sources")
        cmakelists_path = os.path.join(self.source_folder, "sources", "Software", "C", "CMakeLists.txt")
        print(cmakelists_path)
        os.unlink(cmakelists_path)
        shutil.copy2(os.path.join(self.source_folder, "CMakeLists.txt"), cmakelists_path)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=os.path.join(self.source_folder, "sources", "Software", "C"))
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["gopigo3"]

    def package_id(self):
        del self.info.settings.arch_build