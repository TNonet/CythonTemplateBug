#ifndef test
#define test

template <class T1>
class TestClass{
    public:
        T1 ptr;

    TestClass(T1 ptr) {
        this->ptr = ptr;
    }

    TestClass() {}
    ~TestClass();
};

#endif
