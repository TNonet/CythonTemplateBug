from cy_test cimport TestClass

cdef build_TestClass(x):
    cdef double[:] x_memview = x

    cdef TestClass arr_item = TestClass(x_memview[0])
