add_executable(test_microecc_app
    test.c
)

add_subdirectory(Unity)
 
target_link_libraries(test_microecc_app
    microecc
    Unity
)

target_compile_options(test_microecc_app PRIVATE 
    -Wall -pedantic 
)

target_compile_features(test_microecc_app PRIVATE
    c_std_99
)
 
add_test(test_microecc test_microecc_app)
