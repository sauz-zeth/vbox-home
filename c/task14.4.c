#include <stdio.h>

int main() {
    int N = 65;
    unsigned long p = 1;
    int i;
    for(i = 0; i <= N; i++) {
        printf("%2d %20lu\n", i, p);
        p *= 2;
    }
    printf("%d\n", i);
}

