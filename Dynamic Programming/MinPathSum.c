#include <stdio.h>
#include <stdlib.h>

int minPathSum(int** grid, int gridSize, int* gridColSize) {
    int ans[100][100];
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < *gridColSize; j++) {
            if (i == 0 && j == 0) ans[i][j] = grid[i][j];
            else if (i == 0) ans[i][j] = ans[i][j-1] + grid[i][j];
            else if (j == 0) ans[i][j] = ans[i-1][j] + grid[i][j];
            else {
                int up, left;
                up = ans[i-1][j];
                left = ans[i][j-1];
                ans[i][j] = grid[i][j] + ((up<left)?up:left);
            }
        }
    }
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < *gridColSize; j++) {
            printf("%d ", ans[i][j]);
        }
        printf("\n");
    }
    return ans[gridSize - 1][*gridColSize - 1];
}

int main() {
    int gridArray[3][3] = {{1, 3, 1}, {1, 5, 1}, {4, 2, 1}};
    int gridSize = 3;
    int gridColSize = 3;

    // 动态分配内存用于存储指针数组
    int** grid = (int**)malloc(gridSize * sizeof(int*));
    for (int i = 0; i < gridSize; i++) {
        grid[i] = gridArray[i];
    }

    int result = minPathSum(grid, gridSize, &gridColSize);
    printf("Minimum Path Sum: %d\n", result);

    // 释放动态分配的内存
    free(grid);

    return 0;
}