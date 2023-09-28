x = int(input("Quantas notas iremos calcular? "))
y = 1
soma = 0
while (y <= x):
    nota = float(input("Digite uma nota: "))
    soma += nota
    y += 1
media = soma / x
print(f"A média dessas notas é: {media:.1f}")
