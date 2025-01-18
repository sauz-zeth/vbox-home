#include <stdio.h>

#define N 100

int main() {
    int s = 0;
    int i;
    for(i = 1; i <= N; i++) {
        s += i * i;
    }
    printf("%d\n", s);
//    printf("%d\n", s);
}
