pergunta = "s, S"
while pergunta == "s, S":
    nota1 = float(input("Adicione a nota da 1º avaliação: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("A nota precisa ser maior que 0 e menor que 10. Tente novamente: "))
    nota2 = float(input("Adicione a nota da 2º avaliação: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Anota precisa ser maior que 0 e menor que 10. Tente novamente: "))
    media = (nota1 + nota2) / 2
    print(f" A média do aluno nessa unidade foi {media}")
    pergunta = input("Deseja realizar um novo cálculo? ")
else:
    print("obrigada!")