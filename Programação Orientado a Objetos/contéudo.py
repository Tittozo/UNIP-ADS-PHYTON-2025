seclass Animal:
    def __init__(self, nome):
        self.nome = nome
    def emitir_som(self):
        pass
class Cachorro(Animal):
    def emitir_som(self):
        return 'AU, AU!'

class Gato(Animal):
    def emitir_som(self):
        return 'MIAU!'

dog = cachorro('Ronaldo')
cat = gato('Estrassalha Pussy')

print(dog.nome,'-',dog.emitir_som())
print(cat.nome,'-',cat.emitir_som())

# Definindo a classe (o molde)
class Carro:
    # O método __init__ é o construtor. Ele inicializa os atributos do objeto.
    def __init__(self, marca, modelo, cor):
        self.marca = marca   # Atributo
        self.modelo = modelo # Atributo
        self.cor = cor       # Atributo
        self.ligado = False  # Atributo com valor padrão

    # Um método (comportamento do objeto)
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.modelo} ligou... Vrum!")
        else:
            print(f"O {self.modelo} já está ligado.")

    def exibir_info(self):
        status = "Ligado" if self.ligado else "Desligado"
        print(f"Carro: {self.marca} {self.modelo} | Cor: {self.cor} | Status: {status}")

# --- Usando a classe (Criando objetos) ---

# Criando o primeiro objeto (instância)
meu_carro = Carro("Toyota", "Corolla", "Prata")

# Criando o segundo objeto
carro_do_vizinho = Carro("Fiat", "Uno", "Escada no teto")

# Chamando os métodos
meu_carro.exibir_info()
meu_carro.ligar()
meu_carro.exibir_info()

print("-" * 20)
carro_do_vizinho.exibir_info()



class Pessoa:
    # O método __init__ é onde definimos as características (atributos)
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    # Um método para a pessoa se apresentar
    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}.")

# Criando "objetos" (pessoas específicas) a partir da classe
pessoa1 = Pessoa("Ana", 28, "Engenheira")
pessoa2 = Pessoa("Carlos", 35, "Professor")

# Usando as características
pessoa1.apresentar()
pessoa2.apresentar()

# Acessando uma característica específica
print(f"A profissão da Ana é {pessoa1.profissao}.")

class PedidoPesqueiro:
    def __init__(self, item, valor):
        self.item = item
        self.valor = valor
        self.status = "Pendente"

    def entregar_pedido(self):
        self.status = "Entregue"
        print(f"✅ O item '{self.item}' foi entregue na mesa!")

    def exibir_resumo(self):
        print(f"📋 Pedido: {self.item} | Valor: R$ {self.valor:.2f} | Status: {self.status}")

# --- Usando o código ---

# Criando (instanciando) um pedido
pedido01 = PedidoPesqueiro("Tilápia Porção Familiar", 85.90)

# Verificando o que foi pedido
pedido01.exibir_resumo()

# Garçom entrega o pedido
pedido01.entregar_pedido()

# Verificando o status atualizado
pedido01.exibir_resumo()
