project (microecc)
cmake_minimum_required(VERSION 3.5.1)

set(TARGET_GROUP main CACHE STRING "Group to build")

add_subdirectory(src)

if(TARGET_GROUP STREQUAL main)
    message(SKIP "Nothing to do...")
elseif(TARGET_GROUP STREQUAL test)
    include(CTest)
    add_subdirectory(tests)
else()
    message(FATAL_ERROR "Given TARGET_GROUP unknown")
endif()
