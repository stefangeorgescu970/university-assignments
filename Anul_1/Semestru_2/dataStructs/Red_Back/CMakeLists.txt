cmake_minimum_required(VERSION 3.7)
project(Red_Back)

set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_STANDARD 11)

# set(CMAKE_CXX_FLAGS "-g -o0 -Wall -fprofile-arcs -ftest-coverage")

set(SOURCE_FILES main.cpp
        DataStructures/Stack/Stack.cpp
        DataStructures/Stack/Stack.h
        Exceptions/RedBackException.h
        Tests/TestStack.cpp
        Tests/TestQueue.cpp
        DataStructures/Queue/Queue.cpp
        DataStructures/Queue/Queue.h
        Game/Player/Player.cpp
        Game/Player/Player.h
        Game/Table/Table.cpp
        Game/Table/Table.h
        Game/Game.cpp
        Game/Game.h UserInterface/UserInterface.cpp UserInterface/UserInterface.h)

find_package(Qt5Widgets REQUIRED)

add_subdirectory(lib/googletest-master)

include_directories(lib/googletest-master/googlemock/include)

include_directories(lib/googletest-master/googletest/include)

include_directories(${Qt5Widgets_INCLUDE_DIRS})

add_executable(Red_Back ${SOURCE_FILES})

target_link_libraries(Red_Back Qt5::Widgets)

target_link_libraries(Red_Back gtest gtest_main)