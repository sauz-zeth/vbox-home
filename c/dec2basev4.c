#include <stdio.h>

#define N 64 

int main() {
    int i;
    scanf("%d", &i);
    int b;
    scanf("%d", &b);

    int k = 0;
    int a[N];

    while(i > 0) {
        a[k] = i % b;
        i /= b;
        k++;
    }

    for(int i = k - 1; i >= 0; i -= 1) {
        printf("%d", a[i]);
    }
}
