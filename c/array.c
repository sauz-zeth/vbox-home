#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "array.lib.c"

int b[5] = {1, 2, 3, 4, 5};

int main() {
    int i = 75;
    printf("%d\n", i);
    printf("%p\n", &i);
    i = 76;
    printf("%d\n", i);
    printf("%p\n", &i);
    printf("%ld\n", sizeof i);

    int j;
    printf("%p\n", &j);
    printf("%d\n", j);

    int a[5] = {23, 45, 32};
    printf("%ld\n", sizeof a);
    printf("%p\n", a);
    printf("%d\n", a[0]);

    a[0] = 56172;
    printf("%d\n", a[0]);

    printf("****\n");
    for(int i = 0; i < 5; i++) {
        printf("%d\n", a[i]);
    }
    printf("****\n");

    int k = 32;
    printf("%p\n", &k);

    a[-2] = 15;
    printf("%d\n", k);

    print(a, 5);
    print(a + 2, 30);
    print(b, 50);
    
    print(b, 5);
    printf("%d\n", max(b, 5));
    printf("%d\n", min(b, 5));
    printf("%d\n", sum(b, 5));
    printf("%d\n", sumsqr(b, 5));
    repeat(a, 5, 20);
    print(a, 5);
//    printf("%ld\n", readn(a, 5));
//    print(a, 5);
    
    FILE *f = fopen("array.txt", "r");
    printf("%ld\n", freadn(f, a, 5));
    print(a, 5);
    a[4] = 2;
    print(a, 5);

    printf("%ld\n", count(a, 5, 2));
    reverse(a, 5);

// ********************* //
    
    seq(a, 5, 1, 1);
    print(a, 5);
    
    printf("test \n");

    copy(a, 3, a + 1);
    print(a, 5);

    seq(a, 5, 5, -1);
    print(a, 5);

    copy(a + 2, 3, a);
    print(a, 5);

    repeat(a, 5, 9);
    print(a, 5);
    
    seq(a, 5, 5, -1);
    printf("%ld\n", pos(a, 5, 9));
        
    int c[7] = {3, 1, 20, 47, 16, 3, 5};

    int cmax;
    int cmin;

    maxmin(c, 7, &cmax, &cmin);
    printf("%d\n", cmax);
    printf("%d\n", cmin);

    printf("cycle\n");

    int cyc[3] = {1, 2, 3};
    cycle_(c, 7, cyc, 3);
    print(c, 7);

//    *****************

    printf("counter\n");

    int d[8] = {3, 1, 4, 3, 3, 2, 3, 4};
    print(d, 8);
    k = counter(d, 8, b, c);

    print(b, k);
    print(c, k);


//    *****************

    srand(3);
    printf("%d\n", rand() % 100);
    printf("%d\n", RAND_MAX);

    randseq(d, 8, -2, 8);
    print(d, 8);

// ****************
    
    long n = 5;
    print(d, n);

    extend(d, &n, cyc, 3);
    print(d, n);

    print(cyc, 3);
    push(cyc, 3, 8);
    print(cyc, 3);


// ****************

    
    print(a, 5);

    int *p = copya(a, 5);
    print(p, 5);
    free(p);
    
// ****************

    seqa(&p, 5, 2, 2);
    print(p, 5);
    free(p);


// ****************

    printf("insert\n");

    int ins[10] = {1, 23, 5, 8, 9};

    int bins[3] = {999, 999, 999};
    long nins = 5;
    insert(ins, &nins, 8, bins, 3);
    print(ins, nins);


}
