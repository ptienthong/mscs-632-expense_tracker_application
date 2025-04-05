cmake_minimum_required(VERSION 3.10)
#list( APPEND CMAKE_CXX_FLAGS "-std=c++0x ${CMAKE_CXX_FLAGS} -g -ftest-coverage -fprofile-arcs")
# Set the C++ standard to C++20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Add debugging and coverage flags
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -ftest-coverage -fprofile-arcs")
project(expense_tracker)


include_directories(cpp/include)

add_executable(expense_tracker 
    cpp/src/main.cpp 
    cpp/src/expense_tracker.cpp
    
)

# ---------------------
# GoogleTest Integration
# ---------------------

# Download and configure GoogleTest
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/heads/main.zip
)

FetchContent_MakeAvailable(googletest)

enable_testing()

# Add test executable
add_executable(expense_tracker_test 
    cpp/test/expense_tracker_test.cpp 
    cpp/src/expense_tracker.cpp
)

target_include_directories(expense_tracker_test PUBLIC cpp/include)

target_link_libraries(expense_tracker_test 
    gtest_main 
)

include(GoogleTest)
gtest_discover_tests(expense_tracker_test)