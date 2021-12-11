#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
int m,n;

int min_energy(int **grid, int **table, int m, int n)
{
    if (grid[m-1][n-1] < 0){
        table[m-1][n-1] = abs(grid[m-1][n-1])+1;
    } else {
        table[m-1][n-1] = 1;
    }

    for (int i = m-2; i> -1; i--){
        table[i][n-1] = max(table[i+1][n-1]-grid[i][n-1], 1);
    }
    for (int j = n-2; j > -1; j--){
        table[m-1][j] = max(table[m-1][j+1]-grid[m-1][j], 1);
    }
    for (int i=m-2; i> -1; i--)
    {
        for (int j=n-2; j> -1; j--)
        {
            int min_cell = min(table[i+1][j], table[i][j+1]);
            table[i][j] = max(min_cell-grid[i][j], 1);
        }
     }
     return table[0][0];
}

int main() {
  int m, n;
  cin >> m;
  cin >> n;
  int **arr = new int *[m];
  int **table = new int *[m];
  for (int i = 0; i < m; i++) {
    arr[i] = new int[n];
    table[i] = new int[n];
  }
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      cin >> arr[i][j];
      table[i][j] = 0;
    }
  }
  cout << min_energy(arr, table, m, n);
}