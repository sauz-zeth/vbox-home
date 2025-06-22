#include <stdio.h>

#define N_MAX 100
#define M_MAX 10000

void print_graph(int graph[][N_MAX], int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", graph[i][j]);
        }
        printf("\n");
    }
}

void DFS(int graph[][N_MAX], int used[N_MAX], int N, int vertex) {
    used[vertex] = 1;

    for (int i = 0; i < N; i++) {
        if (graph[vertex][i] && !used[i]) {
            DFS(graph, used, N, i);
        }
    }
}

int main() {
    FILE *file = fopen("data1.txt", "r");
    int N, M;
    fscanf(file, "%d%d", &N, &M);

    int graph[N_MAX][N_MAX];
    int used[N_MAX];

    for (int i = 0; i < N; i++) {
        used[i] = 0;
        for (int j = 0; j < N; j++) {
            graph[i][j] = 0;
        }
    }

    int a, b;
    for (int i = 0; i < M; i++) {
        fscanf(file, "%d %d", &a, &b);
        graph[a - 1][b - 1] = 1;
        graph[b - 1][a - 1] = 1;
    }

    print_graph(graph, N);

    fclose(file);
    return 0;
}
