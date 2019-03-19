import os

def main():
    print("=" * 20)
    print("Bem vindo ao carrinho")
    print("=" * 20)

    while True:
        print("O que deseja fazer?")
        print("1 - Criar carrinho")
        print("2 - Ver itens")
        print("3 - Adicionar item")
        print("4 - Excluir item")
        print("5 - Excluir carrinho")
        print("0 - Sair")
        funcao = input("Número da opção: ")


        if funcao == '1':
            criar_carrinho()

        elif funcao == '2':
            ver_carrinho()

        elif funcao == '0':
            print("=" * 20)
            print("Obrigado por utilizar o programa")
            print("=" * 20)
            break
        else:
            print('Valor inesistente')


def criar_carrinho():
    nome_carrinho = input("Digite o nome do carrinho: ")
    if not existe_arquivo(nome_carrinho)
    arquivo = open(nome_carrinho+".txt", "w")
    arquivo.close()

def ver_carrinho():
    nome_carrinho = input("Qual o nome?")
    arquivo = open(nome_carrinho+".txt", "r")
    arquivo.close()

def existe_arquivo():
    if os.path.isfile(nome_arquivo):
        return True
    else:
        print("Arquivo não encontrado")
        return False