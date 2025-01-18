#include <stdio.h>

int f = 17;

int main() {
    int i = 16;
    int *p = &i, *q;
    printf("%d\n", *p);
    *p = 32;
    printf("%d\n", i);
    int j = 48;
    p = &j;
    *p = 56;
    printf("%d\n", j);
    printf("%p\n", &j);

    int a[6] = {1, 2, 3, 4, 5, 6};
    printf("%p\n", a);
    printf("%ld\n", a - &j);
    p = &a[0];
    printf("%d\n", *p);
    q = a;
    q++;
    printf("%d\n", *(q + 1));
    printf("%ld\n", q - p);
    *(p - 5) = 52;
    printf("%d\n", j);
    a[-5] = 78;
    printf("%d\n", j);
    p[-5] = 24;
    printf("%d\n", j);
    *(a - 5) = 234;
    printf("%d\n", j);
    printf("%ld\n", sizeof p);
    *(3 + a) = 33;
    printf("%d\n", 3[a]);

    printf("%p\n", &f);
    printf("%p\n", main);
}
