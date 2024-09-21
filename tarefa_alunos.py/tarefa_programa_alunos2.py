from funcoes import cadastrar_alunos, mostrar_relatorio
# Programa principal
def main():
    alunos = []
    while True:
        print("Menu:")
        print("1 - Cadastro de Alunos")
        print("2 - Relatório de Alunos")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_alunos(alunos)
        elif opcao == '2':
            mostrar_relatorio(alunos)
        elif opcao == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
def situacao(m):
    mensagem = ''
    if m >=7:
        mensagem = "aprovado"
    else:
        mensagem = "reprovado"
    return mensagem





if __name__ == "__main__":
    main()
