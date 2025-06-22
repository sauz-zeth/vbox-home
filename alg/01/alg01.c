#include <stdio.h>

#define N_MAX 100
#define M_MAX 10000

typedef char vertex_t;
typedef vertex_t (*adj_list_ptr)[2]; 

vertex_t adj_list[M_MAX][2];
char visited[N_MAX] = {};
int N, M;

void print_list(adj_list_ptr a, int m) {
    for (int i = 0; i < m; i++) {
        printf("%d %d\n", a[i][0], a[i][1]);
    }
}

char DFS(vertex_t parent) {
    vertex_t children[N_MAX] = {};
    int children_count = 0;
// TODO: Заполнить массив Children, выполнить проверку на треугольник, запустить DFS рекурсивно.
    visited[parent] = 1;

    vertex_t child;
    for(int i = 0; i < M; i++) {
        if(adj_list[i][0] == parent) {
            child = adj_list[i][1];
        }
        else if(adj_list[i][1] == parent) {
            child = adj_list[i][0];
        } 
        else continue;

        if(!visited[child]) {
            if(!DFS(child)) return 0;
        }
    }

    return 1;
}

int main() {
    FILE *file = fopen("data1.txt", "r");
    fscanf(file, "%d%d", &N, &M);

    int a, b;
    for (int i = 0; i < M; i++) {
        fscanf(file, "%d%d", &a, &b);
        adj_list[i][0] = a;
        adj_list[i][1] = b;
    }

    print_list(adj_list, M);

    fclose(file);
    return 0;
}
