#include <stdio.h>

int isPrime(int x) {
    if(x < 2) return 0;    
    
    for(int j = 2; j * j <= x; j++) {
        if(x % j == 0) {
            return 0;
        }
    }

    return 1;
}

int main() {
    int N = 200000;
    int n = 0;

    for(int i = 2; i <= N; i++) {
        if(isPrime(i))
            n++;
    } 

    printf("%d\n", n);
}

