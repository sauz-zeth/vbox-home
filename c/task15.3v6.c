#include <stdio.h>

#define N 99

int main() {
    int s = 0;
    int i = 1;
    while(1) {
        if(i > N) break;
        s += i;
        i += 2; 
    }
    printf("%d\n", s);
}




