cimport cython

cdef extern from "test.h":

    cdef cppclass TestClass[T]:
        TestClass()
        TestClass(T ptr)
        T ptr;