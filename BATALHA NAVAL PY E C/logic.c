#LÓGICA DE BATALHA NAVAL EM C INTEGRAÇÃO COM PHYTON

#include <stdio.h>

int processar_ataque_c(int x, int y, int tamanho, char grid[tamanho][tamanho]) {
    if (grid[x][y] == 'N') {
        return 1;
    } else if (grid[x][y] == 'X' || grid[x][y] == 'O') {
        return 2;
    }
    return 0:
} 


