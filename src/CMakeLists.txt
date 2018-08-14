
file(GLOB SOURCES "*.c")
add_library(microeccdyn SHARED ${SOURCES} )
add_library(microecc STATIC ${SOURCES} )

target_include_directories(microecc PUBLIC
    ../include
)
target_include_directories(microeccdyn PUBLIC
    ../include
)