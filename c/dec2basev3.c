#include <stdio.h>

int main() {
    int i;
    scanf("%d", &i);
    int b;
    scanf("%d", &b);
    int k = 0;
    int s = 0;
    while(i > 0) {
        s = s * b + i % b;
        i /= b;
        k++;
    }
    for(i = 0; i < k; i++) {
        printf("%d", s % b);
        s /= b;
    }
}
