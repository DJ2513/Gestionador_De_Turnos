def turno_cosmeticos():
    for turn in range(1, 10000):
        yield f'C-{turn}'


def turno_perfumeria():
    for turn in range(1, 10000):
        yield f'P-{turn}'


def turno_farmacia():
    for turn in range(1, 10000):
        yield f'F-{turn}'


cos = turno_cosmeticos()
per = turno_perfumeria()
far = turno_farmacia()


def decorador(turno):
    print("*"*55)
    print(f"Su turno es: ")
    if (turno == "cos"):
        print(next(cos))
    elif (turno == "per"):
        print(next(per))
    else:
        print(next(far))
    print("Espere y será atendido!")
    print("*"*55)
