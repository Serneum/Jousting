from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.flake8")
# use_plugin("python.distutils")
use_plugin("python.install_dependencies")

default_task = ["install_dependencies", "publish"]

@init
def initialize(project):
    # project.build.depends_on("coverage")
    project.build_depends_on("mockito")

    project.set_property("verbose", True)

    project.set_property("flake8_include_test_sources", True)
    project.set_property("flake8_break_build", True)
    project.set_property("flake8_include_test_sources", True)