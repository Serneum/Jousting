from pybuilder.core import Author, init, use_plugin

use_plugin("python.core")
use_plugin("python.distutils")
use_plugin("source_distribution")
use_plugin("python.install_dependencies")

use_plugin("python.coverage")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.frosted")

default_task = ["clean", "publish", "build_source_distribution"]

summary = "A game based on To Cry a Joust. Written in Python using PyGame."
authors = [Author("Chris Rees", "serneum@gmail.com")]
url = "https://github.com/Serneum/Jousting"
license = "Apache License, Version 2.0"

@init
def initialize(project):
    project.build_depends_on("coveralls")
    project.build_depends_on("mockito")

    project.set_property("verbose", True)

    project.set_property("coverage_threshold_warn", 90)

    project.set_property("flake8_include_test_sources", True)
    project.set_property("flake8_break_build", True)
    project.set_property("flake8_include_test_sources", True)

    project.set_property('frosted_include_test_sources', True)