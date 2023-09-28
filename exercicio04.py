original = "dificil"
senha = input("Digite sua senha: ")
x = 1
y = 3
while senha != original:
    y -= 1
    if x >= 3:
        print("Não há mais tentativas")
        break
    tentativas = print(f"Restam {y} tentativas")
    senha = input(f"Senha incorreta. Digite novamente: ")
    x += 1
else:
    print("Seja bem vindo")