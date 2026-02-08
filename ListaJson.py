import json

def main():
    """
    Cria uma lista de dicionários e a salva em um arquivo JSON.
    """
    # 1. Criar a lista
    # Esta lista é composta por dicionários, que são ideais para representar
    # objetos com pares de chave-valor.
    pessoas = [
        {"nome": "Maria", "idade": 30, "cidade": "São Paulo"},
        {"nome": "João", "idade": 25, "cidade": "Rio de Janeiro"},
        {"nome": "Ana", "idade": 35, "cidade": "Belo Horizonte"}
    ]

    # 2. Exportar a lista para um arquivo JSON
    # 'w' significa 'write' (escrever) e 'json.dump' converte a lista para JSON
    # e a escreve no arquivo. O 'indent' deixa o arquivo JSON mais legível.
    nome_arquivo = "pessoas.json"
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
        json.dump(pessoas, arquivo_json, indent=4, ensure_ascii=False)
    
    print(f"Lista exportada com sucesso para '{nome_arquivo}'.")

#Outro tipo de programa em JSON

import json
import os

# Caminho do arquivo JSON onde as tarefas serão armazenadas
ARQUIVO_JSON = 'tarefas.json'

# Função para carregar as tarefas do arquivo JSON
def carregar_tarefas():
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, 'r') as arquivo:
            return json.load(arquivo)
    return []

# Função para salvar as tarefas no arquivo JSON
def salvar_tarefas(tarefas):
    with open(ARQUIVO_JSON, 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    tarefas = carregar_tarefas()

    tarefa = input("Digite a descrição da tarefa: ")
    tarefas.append({"tarefa": tarefa})
    
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

# Função para exibir todas as tarefas
def exibir_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa['tarefa']}")

# Função para excluir uma tarefa
def excluir_tarefa():
    tarefas = carregar_tarefas()
    exibir_tarefas()

    if tarefas:
        try:
            indice = int(input("Escolha o número da tarefa a ser excluída: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefas.pop(indice)
                salvar_tarefas(tarefas)
                print("Tarefa excluída com sucesso!")
            else:
                print("Índice inválido!")
        except ValueError:
            print("Por favor, insira um número válido.")

# Função principal que exibe o menu e gerencia as opções
def menu():
    while True:
        print("\n--- GERENCIADOR DE TAREFAS ---")
        print("1. Adicionar tarefa")
        print("2. Exibir tarefas")
        print("3. Excluir tarefa")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            exibir_tarefas()
        elif opcao == '3':
            excluir_tarefa()
        elif opcao == '4':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Iniciar o menu principal
if __name__ == "__main__":
    menu()


# 3. Chamar a função main
# Esta estrutura garante que a função 'main' seja executada apenas
# quando o script é chamado diretamente.
if __name__ == "__main__":
    main()

import json

# 1. Criando um dicionário (objeto Python)
dados_usuario = {
    "nome": "Carlos Silva",
    "idade": 28,
    "estudante": True,
    "habilidades": ["Python", "C", "Data Science"]
}

# 2. Convertendo Dicionário para JSON (String)
# O parâmetro 'indent' deixa o texto bonito para leitura humana
json_string = json.dumps(dados_usuario, indent=4, ensure_ascii=False)

print("--- String JSON Gerada ---")
print(json_string)

# 3. Convertendo JSON de volta para Dicionário Python
dados_recebidos = json.loads(json_string)

print("\n--- Acessando dados do Dicionário ---")
print(f"Nome: {dados_recebidos['nome']}")
print(f"Primeira habilidade: {dados_recebidos['habilidades'][0]}")
