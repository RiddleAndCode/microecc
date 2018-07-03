file(GLOB TEST_LIB_SOURCES "*.c")

add_executable(test_microecc_app
    ${TEST_LIB_SOURCES}
)

target_include_directories(test_microecc_app PUBLIC .
)

add_subdirectory(Unity)

target_link_libraries(test_microecc_app
    microecc
    Unity
    gcov
    asan
)

target_compile_features(test_microecc_app PRIVATE
    c_std_99
)

add_custom_target(gcovr
    COMMAND ${CMAKE_BINARY_DIR}/tests/test_microecc_app
    COMMAND gcovr -k  --branches  -r  ${CMAKE_SOURCE_DIR}
              --object-directory=${CMAKE_BINARY_DIR}/tests/CMakeFiles/test_microecc_app.dir/
              --xml-pretty -o ${CMAKE_BINARY_DIR}/coverage.xml
    COMMAND gcovr -k  --branches  -r  ${CMAKE_SOURCE_DIR}
              --object-directory=${CMAKE_BINARY_DIR}/tests/CMakeFiles/test_microecc_app.dir/
              --html --html-details -o ${CMAKE_BINARY_DIR}/coverage.html
    COMMENT "Creating Coverage HTML and XML summary")

add_custom_command(TARGET test_microecc_app POST_BUILD
    COMMENT "Creating Coverage HTML and XML summary"
    COMMAND ${CMAKE_BINARY_DIR}/tests/test_microecc_app
    COMMAND gcovr -k  --branches  -r  ${CMAKE_SOURCE_DIR}
              --object-directory=${CMAKE_BINARY_DIR}/tests/CMakeFiles/test_microecc_app.dir/
              --xml-pretty -o ${CMAKE_BINARY_DIR}/coverage.xml
    COMMAND gcovr -k  --branches  -r  ${CMAKE_SOURCE_DIR}
              --object-directory=${CMAKE_BINARY_DIR}/tests/CMakeFiles/test_microecc_app.dir/
              --html --html-details -o ${CMAKE_BINARY_DIR}/coverage.html
    COMMENT "Creating Gprof results from testing."              
    COMMAND cd ${CMAKE_BINARY_DIR}/tests && gprof test_microecc_app gmon.out > analysis_test_microecc_app)


add_test(test_microecc_app test_microecc_app)