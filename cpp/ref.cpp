#include <iostream>

using namespace std;

int main() {
    int x;
    int *p = &x;

    int&& y = move(*p);
    int&& z = move(y);
}
