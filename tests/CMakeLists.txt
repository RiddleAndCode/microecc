add_executable(test_microecc_app
    test.c
)

add_subdirectory(Unity)
 
target_link_libraries(test_microecc_app
    microecc
    Unity
)
 
add_test(test_microecc test_microecc_app)
