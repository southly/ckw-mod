cmake_minimum_required(VERSION 2.8)
project(ckw-mod CXX)

include_directories(${CMAKE_SOURCE_DIR})
aux_source_directory(${CMAKE_SOURCE_DIR} SRCS)
file(GLOB RCFILES ${CMAKE_SOURCE_DIR} "*.rc")

set(CMAKE_BUILD_TYPE Release)
set(LIBS shlwapi imm32)

add_executable(ckw WIN32 ${SRCS} ${RCFILES})
target_link_libraries(ckw ${LIBS})
