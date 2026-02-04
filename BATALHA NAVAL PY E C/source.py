#Programação Orientada a Objetos - Batalha Naval em PYTHON

class Navio:
    def __init__ (self, nome, tamanho, posicoes):
        self.nome = nome
        self.tamanho = tamanho
        self.posicoes = posicoes
        self.hits = 0

class Tabuleiro:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.grid = [['~' for _ in range(tamanho)] for _ in range(tamanho)]
        self.navios = []
        
    def exibir(self):
        print(' ' + ' '.join([str(i) for i in range(self.tamanho)]))
        for i in enumerate(self.grid):
            print(f'{i[0]} ' + ' '.join(i[1]))


    def adicionar_navio(self, navio):
        self.navios.append(navio)
        for pos in navio.posicoes:
            x, y = pos
            self.grid[x][y] = 'N'

    def atacar(self, x, y):
        if not (0 <= x < self.tamanho and 0 <= y < self.tamanho):
            print('Coordenada fora do tabuleiro!')
            return
        
        for navio in self.navios:
            if (x, y) in navio.posicoes:
                navio.hits += 1
                self.grid[x][y] = 'X'
                if navio.hits == navio.tamanho:
                    print(f'BOOM! Navio {navio.nome} afundado!')
                else:
                    print(f'Acertou o navio {navio.nome}!')
                    return
        self.grid[x][y] = 'O'
        print('Água!')
            
class JogoBatalhaNaval:
    def __init__(self, tamanho_tabuleiro):
        self.tabuleiro = Tabuleiro(tamanho_tabuleiro)
        self.jogando = True

    def iniciar(self):
        navio1 = Navio('Destroyer', 3, [(0, 0), (0, 1), (0, 2)])
        self.tabuleiro.adicionar_navio(navio1)
        
        navio2 = Navio('Submarino', 3, [(1, 0), (1, 1), (1, 2)])
        self.tabuleiro.adicionar_navio(navio2)

        while self.jogando:
            self.tabuleiro.exibir()
            try:
                x = int(input('Digite a coordenada X do ataque: '))
                y = int(input('Digite a coordenada Y do ataque: '))
                self.tabuleiro.atacar(x, y)
            except ValueError:
                print('Por favor, insira coordenada válidas!')
            if all(navio.hits == navio.tamanho for navio in self.tabuleiro.navios):
                print('Parabéns! Todos os navios foram afundados!')
                self.jogando = False

if __name__ == '__main__':
    jogo = JogoBatalhaNaval(5)
    jogo.iniciar()
