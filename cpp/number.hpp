#include <iostream>

struct Number {
    int value {7};

    Number() {
        std::cout << "constructed at: " << this << std::endl;
    }

    ~Number() {
        std::cout << "destructed at: " << this << std::endl;
    }
};
