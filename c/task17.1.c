#include <stdio.h>

int main() {
    int N = 21;
    int a = 0;
    int b = 1;
    printf("%10d\n", a);
    printf("%10d\n", b);
    for(int i = 2; i <= N; i++) {
        int c = a + b;
        a = b;
        b = c;
        printf("%10d\n", c);
}
    }
