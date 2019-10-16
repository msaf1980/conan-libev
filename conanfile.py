from conans import ConanFile, tools
from conans.tools import download, untargz, check_sha1
import os
#import shutil

class LibevConan(ConanFile):
    name = "libev"
    libname = "ev"
    version = "4.43"
    branch = "master"
    scn = "069619bc7159803e664753cee7112089dd7cea7f"
    description = "A full-featured and high-performance (see benchmark) event loop that is loosely modelled after libevent, but without its limitations and bugs. It is used in GNU Virtual Private Ethernet, rxvt-unicode, auditd, the Deliantra MORPG Server and Client, and many other programs."
    url = "https://github.com/msaf1980/libev"
    license = "http://cvs.schmorp.de/libev/LICENSE?revision=1.11&view=markup&pathrev=rel-4_27"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
               "disable_threads": [True, False]}
    default_options = "shared=False", "disable_threads=False"

    def run_bash(self, cmd):
        if self.settings.os == "Windows":
            tools.run_in_windows_bash(self, cmd)
        else:
            self.run(cmd)

    def source(self):
        print("git clone %s -b %s" % (self.url, self.branch))
        self.run("git clone %s -b %s" % (self.url, self.branch))
        self.run("cd %s && git reset --hard %s" % (self.name, self.scn))

    def build(self):
        with tools.chdir(self.name) :
            configure_cmd = "chmod +x autogen.sh ; ./autogen.sh && ./configure "
            if not self.options.shared:
                configure_cmd += " --disable-shared "
            if self.options.disable_threads:
                configure_cmd += "--disable-thread-support "
            if self.settings.os=="Windows":
                configure_cmd += " --toolchain=msvc"
            print(configure_cmd)
            self.run_bash(configure_cmd)
            self.run_bash("make")

    def package(self):
        self.copy("ev.h", dst="include", src=self.libname)
        self.copy("ev++.h", dst="include", src=self.libname)
        if self.options.shared:
            if self.settings.os == "Macos":
                self.copy(pattern="*.dylib", dst="lib", keep_path=False)
            else:
                self.copy(pattern="*.so*", dst="lib", keep_path=False)
        else:
            self.copy(pattern="*.a", dst="lib", keep_path=False)

    def package_info(self):
        if self.settings.os == "Linux" or self.settings.os == "Macos":
            self.cpp_info.libs = ['ev']

