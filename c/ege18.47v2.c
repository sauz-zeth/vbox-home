#include <stdio.h>

#define N 1024

int main() {
    int a[N];
    int n = 0;
    int k = 0;

    FILE *f = fopen("ege18.47.txt", "r");
    int x;
    while(fscanf(f, "%d", &x) != EOF) { 
        a[n] = x;
        for(int i = 0; i <= n - 11; i++) {
            if(a[i] + a[n] < 200) {
                k++;
            }
        }
        n++;
    }        

    printf("%d\n", k);
}
