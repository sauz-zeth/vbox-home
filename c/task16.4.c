#include <stdio.h>

#define N 25434433
#define M 2

int main() {
    int i = N;
    while(i > 0) {
        printf("%d ", i % M);
        i /= M;
    }

}
