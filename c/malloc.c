#include <stdio.h>
#include <stdlib.h>

#define N 10

int main() {
    int *a = malloc(N * sizeof(int));
    for(int i = 0; i < N; i++) {
        a[i] = i;
    }
    printf("%p\n", a);
    a = realloc(a, 2 * N * sizeof(int));
    printf("%p\n", a);
    printf("%d\n", a[5]);
    
    free(a);
}
