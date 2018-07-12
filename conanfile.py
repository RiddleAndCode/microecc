from conans import ConanFile, CMake, tools


class MicroeccConan(ConanFile):
    name = "microecc"
    version = "1.0"
    license = "<Put the package license here>"
    url = "https://github.com/RiddleAndCode/microecc"
    description = "Check git."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "src/*", "include/*", "*"

    def build(self):
        tools.replace_in_file("CMakeLists.txt", "project (microecc)",
                '''project(microecc)
                include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
                conan_basic_setup()''')
        self.run('cmake .')
        self.run('cmake --build .')

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["microecc"]

