#include <iostream>

struct Number {
    int value {7};

    Number() {
        std::cout << "Number constructed at " << this << std::endl;
    }

    Number(const Number& n) : value{n.value} {
        std::cout << "Number copy constructed at " << this << std::endl;
    }

    Number(Number&& n) : value{n.value} {
        std::cout << "Number move constructed at " << this << std::endl;
    }

    Number(int x) : value{x} {
        std::cout << "Number constructed from int at " << this << std::endl;
    }

    Number& operator=(int x) {
        std::cout << "Number assigned from int at " << this << std::endl;

        value = x;
        return *this;
    }

    ~Number() {
        std::cout << "Number destructed at " << this << std::endl;
    }
};
