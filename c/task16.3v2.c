#include <stdio.h>

#define N 25434433

int main() {
    for(int i = N; i != 0; i /= 10) {
        printf("%d ", i % 10);
    }
}
