#include <stdio.h>

#define N_MAX 100
#define M_MAX 10000

// O(N**3)

// TODO: решить

void print_A(int A[][N_MAX], int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }
}

void DFS(int A[][N_MAX], int visited[N_MAX], int N, int vertex) {
    visited[vertex] = 1;

    for (int i = 0; i < N; i++) {
        if (A[vertex][i] && !visited[i]) {
            DFS(A, visited, N, i);
        }
    }
}

int main() {
    FILE *file = fopen("data1.txt", "r");
    int N, M;
    fscanf(file, "%d%d", &N, &M);

    int A[N_MAX][N_MAX];
    int visited[N_MAX];

    for (int i = 0; i < N; i++) {
        visited[i] = 0;
        for (int j = 0; j < N; j++) {
            A[i][j] = 0;
        }
    }

    int a, b;
    for (int i = 0; i < M; i++) {
        fscanf(file, "%d %d", &a, &b);
        A[a - 1][b - 1] = 1;
        A[b - 1][a - 1] = 1;
    }

    print_A(A, N);

    fclose(file);
    return 0;
}
