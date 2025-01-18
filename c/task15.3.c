#include <stdio.h>

#define N 99

int main() {
    int s = 0;
    for(int i = 1; i <= N; i += 2) {
        s += i;
    }
    printf("%d\n", s);
}




