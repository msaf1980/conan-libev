## This repository holds a conan recipe for libev.

[![Build Status](https://travis-ci.org/spielhuus/conan-libev.svg?branch=master)](https://travis-ci.org/spielhuus/conan-libev)
[ ![Download](https://api.bintray.com/packages/squawkcpp/conan-cpp/Libev%3Aconan-cpp/images/download.svg) ](https://bintray.com/squawkcpp/conan-cpp/Libev%3Aconan-cpp)

[Conan.io](https://conan.io) package for [libev](http://software.schmorp.de/pkg/libev.html) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/squawkcpp/conan-cpp/Libev%3Aconan-cpp).

## Use this package

### Basic setup

    $ conan install Libev/4.24@conan-cpp/latest

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    Libev/4.24@conan-cpp/latest

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

### License
[Boost Software License](http://www.boost.org/LICENSE_1_0.txt) - Version 1.0 - August 17th, 2003

