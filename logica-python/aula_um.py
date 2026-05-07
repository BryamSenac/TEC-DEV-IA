#I/O em Python
#Entrada e saida de dados
print("Olá")
input("Qual seu nome: ")
input("Como você esta: ")
print("Que bom, até mais!")

#Variaveis
nome = input("Qual seu nome: ")
idade = input("Qual sua idade: ")
print("Cadastro feito de " + nome + " com " + idade + " anos")

#Sistemas de concatenação e transformação de valores
print(1 + 1)
print('1' + '1')
print('1' + str(1))
print(str(1) + str(1))
print(int('1') + int('1'))
idade = int(input("Qual sua idade: "))

#Operadores matemáticos
valor1 = 10
valor2 = 20

resultado = valor1 + valor2
resultado = valor1 - valor2
resultado = valor1 * valor2
resultado = valor1 / valor2
resultado = valor1 % valor2
resultado = valor1 ** valor2
print("Resultado: " + str(resultado))

nota = int(input("Nota 1:"))
nota = nota + int(input("Nota 2:"))
nota = nota + int(input("Nota 3:"))
nota = nota / 3
print("Media: " + str(nota))

#Operadores de atribuicao
nota = int(input("Nota 1:"))
nota += int(input("Nota 2:"))
nota += int(input("Nota 3:"))
nota /= 3
print("Media: " + str(nota))

valor1 = valor1 + valor2
valor1 += valor2
valor1 -= valor2
valor1 *= valor2
valor1 /= valor2
valor1 **= valor2
valor1 %= valor2

#Atividade Final da Aula
nome_pessoa_1 = input("Digite o nome da primeira pessoa: ")
nome_pessoa_2 = input("Digite o nome da segunda pessoa: ")
idade_pessoa_1 = int(input("Digite a idade da primeira pessoa: "))
idade_pessoa_2 = int(input("Digite a idade da segunda pessoa: "))

print("Diferença de idade é de " + str(idade_pessoa_1 - idade_pessoa_2) + " anos")

idade_aux = idade_pessoa_1
idade_pessoa_1 = idade_pessoa_2
idade_pessoa_2 = idade_aux

print("Diferença de idade é de " + str(idade_pessoa_1 - idade_pessoa_2) + " anos")
