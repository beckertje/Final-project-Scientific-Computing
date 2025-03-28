set(MY_MODS   com.f90   preparation.f90 diagonalize.f90 shooting.f90    potential_func.f90 make_pot.f90  trapez.f90 save_results.f90
              CACHE INTERNAL "")
add_library(mylib "${MY_MODS}")
add_executable(my_exe main.f90)
target_link_libraries(my_exe PRIVATE mylib ${LAPACK_LIBRARIES})
