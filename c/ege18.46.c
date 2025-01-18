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

        int i0 = n >= 5 ? n - 5 : 0;
        for(int i = i0; i < n; i++) {
            int s = a[i] + a[n]; 
            if(s < 1500 && s > 1000) {
                k++;
            }
        }

        n++;
    }        

    printf("%d\n", k);
}

