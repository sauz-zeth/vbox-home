#include <stdio.h>
#include <stdlib.h>

#define N 10

int main() {
    int *a = (int *)malloc(N * sizeof(int));
    for(int i = 0; i < N; i++) {
        a[i] = i;
    }
    printf("%p\n", a);
    a = (int *)realloc(a, 2 * N * sizeof(int));
    printf("%d\n", a[5]);
    printf("%p\n", a);
    void *p = a;
}
