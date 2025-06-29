#include <stdio.h>

#define N_MAX 100
#define M_MAX 10000

typedef int vertex_t;
typedef vertex_t (*adj_list_ptr)[2]; 

vertex_t adj_list[M_MAX][2];
char visited[N_MAX] = {};
int N, M;

void print_list(adj_list_ptr a, int m) {
    for (int i = 0; i < m; i++) {
        printf("%d %d\n", a[i][0], a[i][1]);
    }
}

char triangle_in_children(vertex_t children[], int children_count) {
    for (int i = 0; i < M; i++) {
        vertex_t u = adj_list[i][0];
        vertex_t v = adj_list[i][1];

        char found_u = 0, found_v = 0;
        for (int j = 0; j < children_count; j++) {
            if (children[j] == u) found_u = 1;
            else if (children[j] == v) found_v = 1;
        }
        if (found_u && found_v) return 1;
    }
    return 0;
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
            children[children_count] = child;
            children_count++;
        }
        else if(adj_list[i][1] == parent) {
            child = adj_list[i][0];
            children[children_count] = child;
            children_count++;
        }

        else continue;
    }


    if(triangle_in_children(children, children_count)) {
        return 0;
    }

    for (int i = 0; i < children_count; i++) {
        if (!visited[children[i]]) {
            if (!DFS(children[i])) return 0;
            }
    }

    return 1;
}

int main() {
    FILE *file = fopen("data1.txt", "r");
    fscanf(file, "%d%d", &N, &M);

    int a, b;
    for(int i = 0; i < M; i++) {
        fscanf(file, "%d%d", &a, &b);
        adj_list[i][0] = a;
        adj_list[i][1] = b;
    }

    print_list(adj_list, M);

    for (int i = 0; i < N; i++) {
    if (!visited[i]) {
        if (!DFS(i)) {
            printf("YES\n");
            return 0;
            }
        }
    }
    printf("NO\n");

    fclose(file);
    return 0;
}
