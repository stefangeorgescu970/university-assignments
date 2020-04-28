cmake_minimum_required(VERSION 3.3)



set(CMAKE_CXX_STANDARD 11) # C++11...
set(CMAKE_CXX_STANDARD_REQUIRED ON) #...is required...
set(CMAKE_CXX_EXTENSIONS OFF) #...without compiler extensions like gnu++11

project(ppd_proj_nompi)





# Open CV
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
add_executable(ppd_proj_nompi.o main.cpp)
target_link_libraries(ppd_proj_nompi.o ${OpenCV_LIBS})
# Pthread
set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)
target_link_libraries(ppd_proj_nompi.o Threads::Threads)