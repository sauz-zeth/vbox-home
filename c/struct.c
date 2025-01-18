#include <stdio.h>

typedef
struct Point {
    double x, y, z;
    int index;
} Point;

void f(int *pj) {
    static int i = 5;
    printf("f::i: %d\n", i++);
    ++*pj;
}

int i;
int i;

int main() {
    Point q = {2.7, 4.6, 1.2, 7};
//   Point Point;
    printf("%g\n", q.y); 
    struct Point *pq = &q;
    int *p = NULL;
    printf("%g\n", (*pq).y); 
    printf("%g\n", pq->y); 

    Point a[] = {
        {1, 2, 3, 0},
        {7, 2, 3, 1},
        {3, 5, 1, 2},
        {6, 1, 4, 3}
    };

    printf("%g\n", a[1].x);

    int i = 100;
    int j = i; //(copy) i12n

    int k;
    k = i; //assignment
    
    Point qqq = q;
    printf("%g\n", qqq.x);

    Point qq;
    qq = q;
    printf("%g\n", qq.x);
    
    f(&j);
    printf("%d\n", j);
    f(&j);
    printf("%d\n", j);
    
    const int l = 33;
    int *pl = (int *)&l;
    *pl = 66;
    printf("%d\n", l);
    printf("%d\n", *pl);

}
