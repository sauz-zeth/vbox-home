#include <stdio.h>

int isPrime(int x) {
    if(x < 2) return 0;    

    int j = 2;
    while(j * j <= x) {
        if(x % j == 0) {
            return 0;
        }
        j += j > 2 ? 2 : 1;  
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

