#include <iostream>
#include <memory>
#include "number.hpp"

using namespace std;

int main() {
    int *pi = new int(2);
    cout << *pi << endl;
    delete pi;

    double *pd = new double{0.00000012};
    cout << *pd << endl;
    delete pd;

    //new[]
    int N = 10;
    int *a = new int[N] {1, 2, 4, 5, 1};
    for(int i = 0; i < N; i++) {
        cout << a[i] << endl;
    }
    delete[] a;

    Number *arr = new Number[10];
    delete[] arr;

    Number *b = (Number *)operator new(sizeof(Number) * 10);
    Number* b1 = new(b + 1) Number; //placement new
    Number* b2 = new(b + 2) Number; //placement new
    cout << b1->value << endl;
    cout << b->value << endl;
    b1->~Number();
    destroy_at(b2);
    operator delete(b);

    allocator<Number> al;
    Number *c = al.allocate(10);
    al.deallocate(c, 10);

    cout << "end\n";
}
