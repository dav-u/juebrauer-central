cmake_minimum_required(VERSION 3.0)
project(ParticleFilterDemo)

# Find OpenCV package
find_package(OpenCV 4 REQUIRED)

# Include directories
include_directories(${OpenCV_INCLUDE_DIRS})

# Add your source files
set(SOURCES 
    particle_filter_demo.cpp
    particle_filter.cpp
    mvnrnd.cpp
    spaceship.cpp
    # Add more source files if you have them
)

# Add executable target
add_executable(${PROJECT_NAME} ${SOURCES})

# Link OpenCV libraries
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})

# copy pics folder to build folder
file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/pics DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
