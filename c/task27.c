#include <stdio.h>

long factor(long x, long j) {
    if(x < 2) {
        return 0;
    }
    while(j * j <= x) {
        if(x % j == 0) {
            return j;
        }
        j += j > 2 ? 2 : 1;
    }
    return x; 
}

int main() {
    long i;
    long a = 2;
    scanf("%ld", &i);

    while(i > 1) {
        a = factor(i, a);
        i = i / a;
        printf("%ld ", a);
    }

    printf("\n");
}
