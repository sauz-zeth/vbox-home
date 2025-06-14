#include <iostream>
#include <initializer_list>

using namespace std;

struct A {
    A(int x) {
        cout << "int" << endl;
        cout << x << endl;
    }
    template<typename T>
    A(initializer_list<T> l) {
        cout << "initializer_list" << endl;
        for(auto x : l) {
            cout << x << endl;
        }
    }
};

template<typename T>
void f(initializer_list<T> l) {
    cout << l.size() << endl;

    for(T x : l) {
        cout << x << ' ';
    }
    cout << endl;
    initializer_list<int> l2(l);
}

int main() {
    f({123, 23, 44, 5});

    initializer_list<int> l1;
    cout << empty(l1) << endl;

    initializer_list l3 {1, 2, 23, 4};
    const int* it = l3.begin();
    cout << it[1] << endl;

    for(int x : {1, 2, 3}) {
        cout << x << ' ';
    }
    cout << endl;

    auto a = {123};

    cout << is_same_v<decltype(a), initializer_list<int>> << endl;
    cout << is_same_v<decltype(a), int> << endl;

    A a1 = A(123);
    A a2 = A({123});
    A a3 = A{123};
    A a4 = {123};
    A a5 {123};
    A a6 = 123;
    A a7(123);
    A a8({123});

}
