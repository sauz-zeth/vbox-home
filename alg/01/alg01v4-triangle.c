#include <stdio.h>

#define N_MAX 100
#define M_MAX 10000

// O(M**3)
// TODO: алгоритм поиска треугольников

typedef int vertex_t;
typedef vertex_t (*adj_list_ptr)[2]; 

vertex_t adj_list[M_MAX][2];
char visited[N_MAX] = {};
char marked[N_MAX] = {};
int N, M;

void print_list(adj_list_ptr a, int m) {
    for (int i = 0; i < m; i++) {
        printf("%d %d\n", a[i][0], a[i][1]);
    }
}

char triangle(vertex_t children[], int children_count) {
    for(int i = 0; i < M; i++) {
        vertex_t u = adj_list[i][0];
        vertex_t v = adj_list[i][1];

        char found_u = 0, found_v = 0;
        for(int j = 0; j < children_count; j++) {
            if(children[j] == u) found_u = 1;
            else if(children[j] == v) found_v = 1;
        }
        if(found_u && found_v) return 1;
    }

    return 0;
}

void findChildren(vertex_t *children, int *children_count_ptr, vertex_t parent) {
    for(int i = 0; i < M; i++) {
        vertex_t u = adj_list[i][0];
        vertex_t v = adj_list[i][1];
        
        if(u == parent || v == parent) {
            vertex_t neighbour = u == parent ? v : u;
            if(!visited[neighbour]) {
                marked[neighbour] = 1;
                children[(*children_count_ptr)++] = neighbour;
            }
        }
    }
}

char DFS(vertex_t parent) {
    visited[parent] = 1;

    vertex_t children[N_MAX] = {};
    int children_count = 0;
    findChildren(children, &children_count, parent);

    if(triangle(children, children_count)) {
        return 0;
    }

    for(int i = 0; i < children_count; i++) {
        vertex_t child = children[i];
        if(!visited[child] && !marked[child]) {
            if(!DFS(child)) return 0;
        }
    }

    return 1;
}

vertex_t findRoot() {
    for(vertex_t v = 1; v <= N; v++) {
        if(!visited[v]) return v;
    }

    return 0;
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

//    print_list(adj_list, M);

    vertex_t root;
    while(root = findRoot()) {
        if(!DFS(root)) {
            printf("NO\n");
            return 0;
        }
    }

    printf("YES\n");

    fclose(file);
    return 0;
}
