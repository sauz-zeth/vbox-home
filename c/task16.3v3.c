#include <stdio.h>

#define N 25434433

int main() {
    int i = N;
    while(i > 0) {
        printf("%d ", i % 10);
        i /= 10;
    }

}
