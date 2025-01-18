#include <stdio.h>
#include <stdlib.h>

#define W 4

void print(int *a, long n) {
    for(long i = 0; i < n; i++) {
        printf("%*d ", W, a[i]);
    }
    printf("\n");
}

// n > 0
int max(int *a, long n) {
    int amax = a[0];
    for(long i = 1; i < n; i++) {
        if(a[i] > amax) {
            amax = a[i];
        }
    }

    return amax;
}

int min(int *a, long n) {
    int amin = a[0];
    for(long i = 1; i < n; i++) {
        if(a[i] < amin) {
            amin = a[i];
        }
    }

    return amin;
}

int sum(int *a, long n) {
    int s = 0;
    for(long i = 0; i < n; i++) {
        s += a[i];
    }

    return s;
}

long prod(int *a, long n) {
    long p = 1;
    for(long i = 0; i < n; i++) {
        p *= a[i];
    }

    return p;
}

int sumsqr(int *a, long n) {
    int s = 0;
    for(long i = 0; i < n; i++) {
        s += a[i] * a[i];
    }

    return s;
}

void seq(int *a, long n, int x, int d) {
    a[0] = x;
    for(long i = 1; i < n; i++) {
        a[i] = a[i - 1] + d;
    }
}   

void seqa(int **pa, long n, int x, int d) {
    *pa = malloc(n * sizeof(int));
    seq(*pa, n, x, d);
}   

void repeat(int *a, long n, int x) {
    seq(a, n, x, 0);
}

long freadn(FILE *f, int *a, long n) {
    int x;
    long k = 0;
    while(fscanf(f, "%d", &x) != EOF) { 
        a[k] = x;
        k++;
        if(k >= n && n > 0) break;
    }

    return k;
}    

long readn(int *a, long n) {
    return freadn(stdin, a, n);
}

long count(int *a, long n, int x) {
    long k = 0;
    for(long i = 0; i < n; i++) {
        if(a[i] == x) {
            k++;
        }
    }
    
    return k;
}

void reverse_(int *a, long n) {
    int k = 0;
    for(long i = 0; i < n / 2; i++) {
        k = a[n - i - 1];
        a[n - i - 1] = a[i];
        a[i] = k;
    }
}

void reverse(int *a, long n) {
    int x = 0;
    int *p = a;
    int *q = a + n - 1;
    for(; q > p; p++, q--) {
        x = *q;
        *q = *p;
        *p = x;
    }
}

// 0 1 2 3 4 5
// 0 1 2 3 4 5 6
// 1 2 3 4 5
// 5 4 3 4 5

int *copya(int *a, long n) {
    int *b = malloc(n * sizeof(int));
    for(long i = 0; i < n; i++) {
        b[i] = a[i];
    }
    return b;
}

void copy(int *a, long n, int *b) {
    if(b == a) return;
    
    long is = (b < a) ? 0 : n - 1;
    long ie = (b < a) ? n : -1;
    long di = (b < a) ? 1 : -1;
    for(long i = is; i != ie; i += di) {
        b[i] = a[i];
    }
}

void copy_(int *a, long n, int *b) {
    if(b < a) {
        for(long i = 0; i < n; i++) {
            b[i] = a[i];
        }
    }
    else if(b > a) {
        for(long i = n - 1; i >= 0; i--) {
            b[i] = a[i];
        }
    }
}

long pos(int *a, long n, int x) {
    for(long i = 0; i < n; i++) {
        if(a[i] == x) {
            return i;
        }
    }

    return -1;
}

long counter(int *a, long n, int *b, int *c) {
    int x = 0;
    int posb = 0;

    for(long i = 0; i < n; i++) {
        posb = pos(b, x, a[i]);
        if(posb == -1) {
            b[x] = a[i];
            c[x] = 1;
            x++;
        }
        else {
            c[posb]++;
        }
    }

    return x;
}

void maxmin(int *a, long n, int *pamax, int *pamin) {
    if(n < 1) return;

    *pamax = *pamin = a[0];
    for(long i = 0; i < n; i++) {
        if(a[i] > *pamax)
            *pamax = a[i];
        if(a[i] < *pamin)
            *pamin = a[i];
    }
}

void cycle_(int *a, long n, int *b, long k) {
    long q = n / k;
    int *p = a;
    for(long i = 0; i < q; i++) {
        copy(b, k, p);
        p += k;
    }
    copy(b, n % k, p);
}

void cycle(int *a, long n, int *b, long k) {
    for(int i = 0; i < n; i++) {
        a[i] = b[i % k];
    }
}

void extend(int *a, long *pn, int *b, long k) {
    copy(b, k, a + *pn); 
    *pn += k;
}

void push(int *a, long n, int x) {
    copy(a + 1, n - 1, a);
    a[n - 1] = x;
}

void randseq(int *a, long n, int x, int y) {
    for(int i = 0; i < n; i++) {
        a[i] = rand() % (y - x) + x;
    }
}

void insert(int *a, long *pn, long pos, int *b, long k) {

    if(pos > *pn) {
        pos = *pn;
    }

    int *p = a + pos;
    
    copy(p, *pn - pos, p + k); 
    copy(b, k, p);

    *pn += k;
}
