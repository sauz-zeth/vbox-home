#include <stdio.h>
int main() {
    int m = 0;
    int pm = 0;
    int x;
    while(1) {
        scanf("%d", &x);
        if(x == 0) break;

        if(x > m) {
            pm = m;
            m = x;
        }
        else if(x > pm && x < m) {
            pm = x;
        }
    }
    printf("%d\n", m);
    printf("%d\n", pm);
}
