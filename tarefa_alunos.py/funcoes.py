# Função para cadastrar alunos
def cadastrar_alunos(alunos):
    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        nota1 = float(input("Digite a nota 1: "))
        nota2 = float(input("Digite a nota 2: "))
        alunos.append({'nome': nome, 'nota1': nota1, 'nota2': nota2})

# Função para mostrar o relatório dos alunos
def mostrar_relatorio(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    print("\nRelatório de Alunos:")
    for aluno in alunos:
        media = (aluno['nota1'] + aluno['nota2']) / 2
        print(f"Nome: {aluno['nome']}, Nota 1: {aluno['nota1']}, Nota 2: {aluno['nota2']}, Média: {media:.2f}")
