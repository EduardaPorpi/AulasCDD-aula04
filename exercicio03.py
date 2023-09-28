num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
x = 1
while (num2 == 0):
    num2 = float(input("Digite um número diferente de 0: "))
    x += 1
    if x == 4:
        print("Você atingiu a quantidade máxima de tentativas")
        break
else:
    divisao = num1/num2
    print(f"A divisão dos números é: {divisao}")
    