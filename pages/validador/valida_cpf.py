def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    contador = [10, 11]
    calculo = [0, 0]

    volta = 9

    for a in range(2):
        for i, j in enumerate(cpf[:volta]):
            calculo[a] = calculo[a] + int(j) * contador[a]
            contador[a] -= 1

        calculo[a] = 11 - (calculo[a] % 11)

        if calculo[a] > 9:
            calculo[a] = 0

        volta += 1

    digitos = "".join(map(str, calculo))
    cpf = cpf[9:]

    if cpf == digitos:
        return True
    else:
        return False
