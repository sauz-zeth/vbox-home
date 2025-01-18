#include <stdio.h>

#define N 1024

int main() {
    int a[N];
    int n = 0;
    int k = 0;
    int b = 0;

    FILE *f = fopen("ege18.47.txt", "r");
    int x;
    while(fscanf(f, "%d", &x) != EOF) { 
//        printf("%d\n", x);
        a[n] = x;
        n++;
    }

    for(int c = 11; c < 1000; c++) {
        b = 0;
        while(b <= c - 11) {
            if(a[c] + a[b] < 200) {
                k++;
            }
            b++;
        }
    }
        
    printf("%d\n", k);
}
