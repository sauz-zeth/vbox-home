#include <stdio.h>

int main () {
    int n;
    int imin, imax;
    scanf("%d", &n);
    int x;
    int xmax;
    for(int i = 1; i <= n; i++) {
        scanf("%d", &x);
        if(x > xmax) {
            xmax = x;
            imin = i;
        }
        if(x >= xmax) {
            imax = i;
        }
    }
    printf("%d %d %d\n", xmax, imin, imax);
}
