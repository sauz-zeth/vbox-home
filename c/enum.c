#include <stdio.h>

typedef
enum Colors {
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE      
} Colors;

int main() {
    printf("%d\n", YELLOW);
    int a[] = {12, 2, 3, 4, 5, 1};
    printf("%d\n", a[BLACK]);
    Colors c1 = 10;
    int c2 = RED;
    printf("%d\n", c2);
    printf("%d\n", c1);
}
