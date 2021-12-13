#Escreva um programa que lê duas notas de vários alunos e armazena
#tais notas em um dicionário, onde a chave é o nome do aluno. A
#entrada de dados deve terminar quando for lida uma string vazia
#como nome. Escreva uma função que retorna a média do aluno, dado
#seu nome.
notas = {}
def media (i):
    return sum(notas[i])/2
while True:
    
    
    Aluno = input("Insira o nome do aluno: ")
    if Aluno == " ":
        break
    nota1 = float (input("Insira a nota da primeira avaliação do aluno {} : ".format(Aluno)))
    nota2 = float (input("Insira a nota da segunda avaliação do aluno {} : ".format(Aluno)))
    notas.update({Aluno : [nota1, nota2]})
for i in notas:
    print('A média do aluno {}, é: {}'.format(i, media(i)))

