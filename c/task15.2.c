
#include <stdio.h>

#define N 20

int main() {
    unsigned long s = 1;
    int i;
    for(i = 1; i <= N; i++) {
        s *= i;
        printf("%20lu\n", s);
    }
}
