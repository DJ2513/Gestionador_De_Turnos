from numeros import *
from os import system


def inicio() -> int:
    system('cls')
    print("*"*55)
    print("*"*14 + " BIENVENIDO A LA FARMACIA! " + "*"*14)
    print("*"*55)
    print("Porfavor indique a que area viene para asignarle un turno: ")
    print("1) Cosmeticos\n2) Farmacia\n3) Perfumeria\n4) Salir")
    eleccion = 0
    while int(eleccion) not in range(1, 5):
        eleccion = input('Opcion: ')
    return int(eleccion)


def volver_inicio() -> None:
    eleccion = 'x'
    while eleccion != 'v':
        eleccion = input('Ingrese "v" para regresar al inicio: ')


menu = 0
finalizar_programa = False
while not finalizar_programa:
    menu = inicio()
    if menu == 1:
        decorador("cos")
        volver_inicio()
    elif menu == 2:
        decorador("far")
        volver_inicio()
    elif menu == 3:
        decorador("per")
        volver_inicio()
    elif menu == 4:
        finalizar_programa = True
        print("Gracias por ulitizar mi programa!")
