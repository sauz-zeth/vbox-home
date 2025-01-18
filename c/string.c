#include <stdio.h>

int main() {
    char c = 0x57;
    printf("%c\n", c);
    c = 'W';
    printf("%d\n", c);
    printf("%c\n", 0x444);
    char a[] = {'a', 'c', 0, 'f', 'g', '\0'};
    printf("%s\n", a);
    char b[] = "kl\0da";
    printf("%ld\n", sizeof b);
    printf("%s\n", b);
    b[0] = 'g';
    printf("%s\n", b);
}
