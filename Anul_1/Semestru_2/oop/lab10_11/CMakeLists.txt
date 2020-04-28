cmake_minimum_required(VERSION 3.7)
project(lab10_11)


set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        socks.txt
        socks_test.txt
        main.cpp
        Console.cpp
        Console.hpp
        Controller.cpp
        Controller.hpp
        Exceptions.cpp
        Repository.cpp
        Repository.hpp
        Socks.cpp
        Socks.hpp
        Tests.cpp
        Tests.hpp
        GUI.cpp
        GUI.hpp)


find_package(Qt5Widgets REQUIRED)

include_directories(${Qt5Widgets_INCLUDE_DIRS})

add_executable(lab10_11 ${SOURCE_FILES})

target_link_libraries(lab10_11 Qt5::Widgets)