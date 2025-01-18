#include <iostream>

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
}
