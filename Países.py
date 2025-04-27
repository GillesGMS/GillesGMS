user = input("Escolha um lado na guerra (Eixo ou Aliados): ")

if user == "Eixo":
    pais1 = {"País": "Alemanha", "Capital": "Berlim"}
    pais2 = {"País": "Itália", "Capital": "Roma"}
    pais3 = {"País": "Japão", "Capital": "Tokyo"}
    Eixo = [pais1, pais2, pais3]

    for pais in Eixo:
        print("Sua aliança é com esses países, ao lado suas capitais", pais)

else:
    pais1 = {"País": "Estados Unidos", "Capital": "Washington"}
    pais2 = {"País": "União Soviética", "Capital": "Moscou"}
    pais3 = {"País": "Reino Unido", "Capital": "Londres"}
    Aliados = [pais1, pais2, pais3]

    for pais in Aliados:
        print("Sua aliança é com esses países, ao lado suas capitais", pais)


