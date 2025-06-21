#include <iostream>

struct Point {
    float x{}, y{};

    Point() {
        std::cout << "Point constructed at " << this << std::endl;
    }

    Point(const Point& p) : x{p.x}, y{p.y} {
        std::cout << "Point copy constructed at " << this << std::endl;
    }

    Point(Point&& p) : x{p.x}, y{p.y} {
        std::cout << "Point move constructed at " << this << std::endl;
    }

    Point(float xx, float yy) : x{xx}, y{yy} {
        std::cout << "Point constructed from int at " << this << std::endl;
    }

    Point(std::initializer_list<int> lst) {
        std::cout << "Point initializer_list constructed at " << this << std::endl;
        
        auto it = lst.begin();
        x = it[0];
        y = it[1];
    }

    Point& operator=(const Point& p) {
        std::cout << "Point copy assigned at " << this << std::endl;

        x = p.x;
        y = p.y;

        return *this;
    }

    ~Point() {
        std::cout << "Point destructed at " << this << std::endl;
    }
};
