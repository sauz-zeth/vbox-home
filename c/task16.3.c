#include <stdio.h>

#define N 2543

int main() {
    int i;
    for(i = 1; i <= N; i *= 10) {
        printf("%d ", N / i % 10);
    }
}
