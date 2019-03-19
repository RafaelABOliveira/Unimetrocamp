
def converte_Numero_Romano(numero_para_converter):
    numeros_base = {
        "I": "1",
        "V": "5",
        "X": "10",
        "L": "50",
        "C": "100",
        "D": "500",
        "M": "1000"
    }
    numero_direita = 0
    numero_final = 0
    contador = 1
    numero_texto = " Somando ..."

    for digito in range(len(numero_para_converter)):

        numero_atual = int(numeros_base.get(numero_para_converter[digito]))

        if contador < len(numero_para_converter):
            numero_direita = int(numeros_base.get(numero_para_converter[contador]))
        else:
            numero_direita = 0

        if numero_atual < numero_direita:
            numero_atual = numero_atual * -1

        contador += 1

        numero_texto = numero_texto + "  " + str(numero_atual)
        numero_final += numero_atual

        print(numero_texto)

    return numero_final
