from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMake


class ConanTutorialRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires(
            "opencv/4.8.1"
        )

    def layout(self):
        cmake_layout(self)
    
    def build_requirements(self):
        self.tool_requires("cmake/3.28.1")

    def configure(self):
        self.options["opencv"].with_v4l = True
        self.options["opencv"].with_gtk = True
        self.options["opencv"].with_qt = False
        self.options["opencv"].with_wayland = False
