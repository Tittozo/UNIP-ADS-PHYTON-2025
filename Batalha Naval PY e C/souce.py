import ctypes
import os

# --- INTEGRAÇÃO COM A LINGUAGEM C ---
# Tenta carregar uma biblioteca externa (DLL) para processar a lógica em C (mais rápido).
try:
    # Obtém o caminho absoluto do arquivo .dll
    lib_path = os.path.abspath('logic.dll')
    batalha_lib = ctypes.CDLL(lib_path)

    # Define os tipos de entrada (dois inteiros) e saída (um inteiro) da função C
    batalha_lib.verificar_ataque.argtypes = [ctypes.c_int, ctypes.c_int]
    batalha_lib.verificar_ataque.restype = ctypes.c_int
except:
    # Caso o arquivo C não exista ou falhe, o Python avisa e segue com a lógica nativa
    print('Não foi possível carregar a biblioteca C. Continuando apenas com Python.')

# --- CLASSES DO JOGO (POO) ---

class Navio:
    """Representa cada embarcação individualmente."""
    def __init__ (self, nome, tamanho, posicoes):
        self.nome = nome
        self.tamanho = tamanho
        self.posicoes = posicoes  # Lista de tuplas [(x, y), ...]
        self.hits = 0             # Contador de acertos sofridos

class Tabuleiro:
    """Gerencia a grade de jogo e o estado das células."""
    def __init__(self, tamanho):
        self.tamanho = tamanho
        # Cria uma matriz (lista de listas) preenchida com '~' (água)
        self.grid = [['~' for _ in range(tamanho)] for _ in range(tamanho)]
        self.navios = []
        
    def exibir(self):
        """Imprime o tabuleiro no console com índices de ajuda."""
        # Imprime o cabeçalho (números das colunas)
        print('\n  ' + ' '.join([str(i) for i in range(self.tamanho)]))
        # Imprime cada linha com seu índice lateral
        for i, linha in enumerate(self.grid):
            print(f'{i} ' + ' '.join(linha))

    def adicionar_navio(self, navio):
        """Registra o navio no tabuleiro e marca sua posição no grid com 'N'."""
        self.navios.append(navio)
        for pos in navio.posicoes:
            x, y = pos
            self.grid[x][y] = 'N'

    def atacar(self, x, y):
        """Processa a tentativa de ataque nas coordenadas X e Y."""
        # Validação de limites (para não quebrar o programa)
        if not (0 <= x < self.tamanho and 0 <= y < self.tamanho):
            print('Coordenada fora do tabuleiro!')
            return
        
        # Verifica se as coordenadas atingem algum dos navios registrados
        for navio in self.navios:
            if (x, y) in navio.posicoes:
                # Se já acertou antes, evita contar duas vezes (opcional)
                if self.grid[x][y] == 'X':
                    print("Você já acertou essa parte!")
                    return
                
                navio.hits += 1
                self.grid[x][y] = 'X' # Marca acerto no tabuleiro
                
                if navio.hits == navio.tamanho:
                    print(f'BOOM! Navio {navio.nome} afundado!')
                else:
                    print(f'Acertou o navio {navio.nome}!')
                return # Encerra a função pois houve acerto
        
        # Se o loop terminar sem encontrar um navio, é água
        self.grid[x][y] = 'O'
        print('Água!')
            
class JogoBatalhaNaval:
    """Classe controladora que gerencia o fluxo principal (loop) do jogo."""
    def __init__(self, tamanho_tabuleiro):
        self.tabuleiro = Tabuleiro(tamanho_tabuleiro)
        self.jogando = True

    def iniciar(self):
        """Configura os navios iniciais e inicia o loop de turnos."""
        # Criando e posicionando navios manualmente
        navio1 = Navio('Destroyer', 3, [(0, 0), (0, 1), (0, 2)])
        self.tabuleiro.adicionar_navio(navio1)
        
        navio2 = Navio('Submarino', 3, [(1, 0), (1, 1), (1, 2)])
        self.tabuleiro.adicionar_navio(navio2)

        # Loop principal de entrada do usuário
        while self.jogando:
            self.tabuleiro.exibir()
            try:
                x = int(input('\nDigite a linha (X) do ataque: '))
                y = int(input('Digite a coluna (Y) do ataque: '))
                self.tabuleiro.atacar(x, y)
            except ValueError:
                print('Por favor, insira números válidos!')
                continue
            
            # Condição de vitória: Todos os navios foram destruídos?
            if all(navio.hits == navio.tamanho for navio in self.tabuleiro.navios):
                self.tabuleiro.exibir()
                print('\nParabéns! Todos os navios foram afundados!')
                self.jogando = False

# --- PONTO DE ENTRADA ---
if __name__ == '__main__':
    # Cria uma instância do jogo com tabuleiro 5x5 e começa
    jogo = JogoBatalhaNaval(5)
    jogo.iniciar()
