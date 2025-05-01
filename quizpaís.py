user = input("Quer iniciar o quiz?")
if  user.lower() == "sim":
    print("Certo, vamos começar!")
    resposta = input("Qual o país que foi responsável por invadir a URSS?")
    if resposta == "Alemanha":
        print("Boa, você acertou!")
    else:
        print("Errado!")

elif user.lower() == "nao":
    print("Ok, encerrando programa!")
