#include <stdio.h>

int main () {
    int m = 0;
    int pm = 0;
    int x;
    int s = 0;
    while(1) {
        scanf("%d", &x);
        if(x == 0) break;
        
        if(x > m) {
            pm = m;
            m = x;
            s = 1;
        }
        else if(pm == x) {
            s += 1;
        }
        else if(x > pm && x < m) {
            pm = x;
            s = 1;
        }
    }
    printf("%d\n", s);
}
