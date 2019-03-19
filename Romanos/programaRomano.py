import converteRomano

def main_Programa():

    numero = input("romano ?").upper()
    print("o numero romano {} equivale a {}".format(numero,converteRomano.converte_Numero_Romano(numero)))

if __name__ == '__main__':
    main_Programa()
