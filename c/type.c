#include <stdio.h>

int main() {
    int i = 35;
    printf("%ld\n", sizeof i);
    long l = 64;
    printf("%ld\n", sizeof l);
    short h = 16;
    printf("%ld\n", sizeof h);
    char c = 128;
    printf("%ld\n", sizeof c);
    printf("%lx\n", (long)c);
    printf("%hx\n", c);
    printf("%d\n", c);
    unsigned char uc = 128;
    printf("%hx\n", uc);
    printf("%hhd\n", uc);
    uc = 255;
    printf("%hhd\n", uc);
    printf("%hhu\n", uc);

    printf("%ld\n", sizeof -15);
    printf("%x\n", -15);
    unsigned char c1 = -15;
    printf("%x\n", c1);
    printf("%u\n", c1);
    unsigned char c2 = c1 + 256;
    printf("%u\n", c2);
    printf("%u\n", c1 + 256);
    printf("%u\n", (char)(c1 + 256));
    printf("%u\n", (unsigned char)(c1 + 256));
    printf("%x\n", (char)(c1 + 256));
    printf("%d\n", (char)(c1 + 256));

    printf("%ld\n", sizeof 15 + 1);

    printf("%d\n", !0);
}
