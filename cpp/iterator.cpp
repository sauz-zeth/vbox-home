#include <iostream>
#include <algorithm>
#include <array>
#include "vec.hpp"
#include "number.hpp"

Number* begin(Number *a) {
    return a;
}

Number* end(Number *a) {
    return a + 4;
}

int* begin(int *a) {
    return a;
}

int main() {
    Vec v16 = Vec{3};
    v16.at(0) = 1;
    v16.at(1) = 3;
    v16.at(2) = 5;

    int arr1[] = {1, 2, 4, 6};
    int arr2[4];

    std::copy(arr1, arr1 + 4, arr2);
    cout << arr2[0] << ' ' << arr2[1] << endl;

    v16.print("v16");
    for(auto& x : v16) {
        x = 1;
    }
    v16.print("v16");

    for(auto x : arr2) {
        cout << x << endl;
    }

    Number* arr3 = new Number[4] {1, 5, 123, 1};

    for(const auto& x : arr3) {
        cout << x.value << endl;
    }

    auto *arr4 = new std::array<int, 4> {1, 5, 123, 1};

    for(auto x : *arr4) {
        cout << x << endl;
    }
}
