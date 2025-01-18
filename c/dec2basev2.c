#include <stdio.h>

#define N 87626798
#define M 2

int main() {
    int i = N;
    int k = 0;
    int s = 0;
    while(i > 0) {
        s = s * M + i % M;
        i /= M;
        k++;
    }
    for(i = 0; i < k; i++) {
        printf("%d", s % M);
        s /= M;
    }
}
