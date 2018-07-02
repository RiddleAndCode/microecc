project (microecc)
cmake_minimum_required(VERSION 3.5.1)

set(TARGET_GROUP main CACHE STRING "Group to build")

if(CPPCHECK)
    set(CMAKE_C_CPPCHECK "cppcheck" --enable=warning,performance,portability,style --error-exitcode=1 --force --quiet)
endif()

add_subdirectory(src)

if(TARGET_GROUP STREQUAL main)
    message(SKIP "Nothing to do...")
elseif(TARGET_GROUP STREQUAL test)
    include(CTest)
    add_subdirectory(tests)
else()
    message(FATAL_ERROR "Given TARGET_GROUP unknown")
endif()
