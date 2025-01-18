#include <stdio.h>

#define N 254
#define M 2

int main() {
    int i = N;
    int k = 1;
    int s = 0;
    while(i > 0) {
        s += i % M * k;
        i /= M;
        k *= 10;
    }
    printf("%d\n", s);
}
