#include <stdio.h>

int main() {
    int N = 3577000;
    int n = 0;

    for(int i = 2; i <= N; i++) {
        int prime = 1;
        for(int j = 2; j * j <= i; j++) {
            if(i % j == 0) {
                prime = 0;
                break;
            }
        }

        if(prime)
            n++;
    } 

    printf("%d\n", n);
}

