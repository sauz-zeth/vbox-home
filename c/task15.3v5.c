#include <stdio.h>

#define N 99

int main() {
    int s = 0;
    int i = 1;
    for(;;) {
        if(i <= N) {
            s += i;
            i += 2; 
        } else {
            break;
        }
    }
    printf("%d\n", s);
}




