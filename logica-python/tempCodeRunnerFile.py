nome_pessoa_1 = input("Digite o nome da primeira pessoa: ")
nome_pessoa_2 = input("Digite o nome da segunda pessoa: ")
idade_pessoa_1 = int(input("Digite a idade da primeira pessoa: "))
idade_pessoa_2 = int(input("Digite a idade da segunda pessoa: "))

print("Diferença de idade é de " + str(idade_pessoa_1 - idade_pessoa_2) + " anos")

idade_aux = idade_pessoa_1
idade_pessoa_1 = idade_pessoa_2
idade_pessoa_2 = idade_aux

print("Diferença de idade é de " + str(idade_pessoa_1 - idade_pessoa_2) + " anos")
