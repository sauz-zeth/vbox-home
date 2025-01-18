#include <iostream>

using namespace std;

namespace my {
    int i {20};
    int j {40};
    int k {80};
}

namespace my {
    struct A {
        int x {34};
    } a;

    void f() {
        cout << "f: " << i << endl;
    }

    void g(int i) {
        cout << "g: " << i << endl;
    }

    void h(A a) {
        cout << "h: " << a.x << endl;
    }
}

int main() {
    int j = 23;
    cout << my::i << endl;

    using my::k;    // using declaration
    cout << k << endl;
//    int k = 70;

    my::f();
    my::g(my::a.x);
    h(my::a);   //ADL (argument dependent lookup)
    using my::a;
    h(a);   

    using namespace my; // using directive
    cout << j << endl;
}
