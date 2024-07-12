import statistics
import random
import msvcrt
import time
import csv
import os

trabajadores = ['Juan Perez', 'Maria Garcia', 'Carlos Lopez', 'Ana Martinez', 'Pedro Rodriguez', 'Laura Hernandez', 'Miguel Sanchez', 'Isabel Gomez', 'Francisco Diaz', 'Elena Fernandez']
sueldos_trabajadores = {}
sueldos = []

#menu
menu_principal = '''
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas.
4. Reporte de sueldos
5. Salir del programa'''

menu_estadisticas = '''
1. Sueldo más alto
2. Sueldo más bajo
3. Promedio de sueldos
4. Media geométrica
'''

#LOS SUELDOS SE APLICAN DE FORMA ALEATORIA PARA CADA EMPLEADO (ENTRE 300.000 Y 2.500.00)

def asignar_sueldos_aleatorios(): #FUNCIONA
    for i in range(len(trabajadores)):
        if trabajadores[i] not in sueldos_trabajadores:
            sueldo = random.randint(300000, 2500000)
            sueldos_trabajadores[trabajadores[i]] = sueldo
            sueldos.append(sueldo)
        else:
            pass
    return

sueldo_menor = []
sueldo_entre = []
sueldo_mayor = []
contador1 = 0
def clasificar_sueldos(): #FUNCIONA
    global contador1
    if contador1 == 0:
        for valor in sueldos_trabajadores:
            if sueldos_trabajadores[valor] < 800000:
                sueldo_menor.append(f'Nombre: {valor} | Sueldo: ${sueldos_trabajadores[valor]}')
                continue
            if sueldos_trabajadores[valor] >= 800000 and sueldos_trabajadores[valor] < 2000000:
                sueldo_entre.append(f'Nombre: {valor} | Sueldo: ${sueldos_trabajadores[valor]}')
                continue
            if sueldos_trabajadores[valor] >= 200000:
                sueldo_mayor.append(f'Nombre: {valor} | Sueldo: ${sueldos_trabajadores[valor]}')
                continue
        print('Sueldos menores a $800.000')
        print(f'Total: {len(sueldo_menor)}')
        for i in sueldo_menor:
            print(i)
        print('\nSueldos entre $800.000 y $2.000.000')
        print(f'Total: {len(sueldo_entre)}')
        for j in sueldo_entre:
            print(j)
        print('\nSueldos mayores a $2.000.000')
        print(f'Total: {len(sueldo_mayor)}')
        for k in sueldo_mayor:
            print(k)
        contador1 += 1
        return
    elif contador1 >= 1:
        print('Sueldos menores a $800.000')
        print(f'Total: {len(sueldo_menor)}')
        for i in sueldo_menor:
            print(i)
        print('\nSueldos entre $800.000 y $2.000.000')
        print(f'Total: {len(sueldo_entre)}')
        for j in sueldo_entre:
            print(j)
        print('\nSueldos mayores a $2.000.000')
        print(f'Total: {len(sueldo_mayor)}')
        for k in sueldo_mayor:
            print(k)
        return

def sueldo_rango():
    for valor in sueldos_trabajadores:
        if sueldos_trabajadores[valor] < 800000:
            sueldo_menor.append(f'Nombre: {valor} | Sueldo: ${sueldos_trabajadores[valor]}')
            continue
        if sueldos_trabajadores[valor] >= 800000 and sueldos_trabajadores[valor] < 2000000:
            sueldo_entre.append(f'Nombre: {valor} | Sueldo: ${sueldos_trabajadores[valor]}')
            continue
        if sueldos_trabajadores[valor] >= 200000:
            sueldo_mayor.append(f'Nombre: {valor} | Sueldo: ${sueldos_trabajadores[valor]}')
            continue

def ver_estadistica():
    while True:
        os.system('cls')
        print(menu_estadisticas)
        try:
            eleccion = int(input('> '))
        except ValueError:
            print('Por favor ingrese una de las opciones(1-4).')
            print('\nPulsa una tecla para continuar...')
            msvcrt.getch()
            continue
        match eleccion:
            case 1:
                os.system('cls')
                sueldo_mayor.sort()
                print('SUELDO MAS ALTO')
                print(sueldo_mayor[-1])
                return
            case 2:
                os.system('cls')
                sueldo_menor.sort()
                print('SUELDO MAS BAJO')
                print(sueldo_menor[0])
                return
            case 3:#PROMEDIO SUELDOS
                total = 0
                for sueldo in sueldos:
                    total = total + sueldo
                os.system('cls')
                print(f'Promedio de sueldos: ${round(total/len(sueldos))}')
                return
            case 4:
                os.system('cls')
                print(f'Media geometrica de sueldos: ${round(statistics.geometric_mean(sueldos))}')
                return
            case Default:
                print('Por favor ingrese una de las opciones(1-4).')
                print('\nPulsa una tecla para continuar...')
                msvcrt.getch()
                pass

def reporte_sueldos():
    with open('informe.csv', 'w') as file:
        csv.writer(file)
        file.write('Nombre Empleado , Sueldo Base , Descuento Salud , Descuento AFP , Sueldo Liquido\n')
        for nombre in sueldos_trabajadores:
            name = f'{nombre}'.ljust(16," ")
            sueldo = f'{sueldos_trabajadores[nombre]}'.ljust(11, ' ')
            descuento_salud = f'{round(sueldos_trabajadores[nombre] * 7 / 100)}'.ljust(15, " ")
            descuento_afp = f'{round(sueldos_trabajadores[nombre] * 12 / 100)}'.ljust(13, ' ')
            sueldo_liquido = sueldos_trabajadores[nombre] - (round(sueldos_trabajadores[nombre] * 7/100) + round(sueldos_trabajadores[nombre] * 12/100))
            file.write(f'{name}, ${sueldo}, ${descuento_salud}, ${descuento_afp}, ${sueldo_liquido}\n')
    return
def menu():
    contador = 0
    while True:
        os.system('cls')
        print(menu_principal)
        try:
            eleccion = int(input('> '))
        except ValueError:
            print('Por favor ingrese una de las opciones(1-5).')
            print('\nPulsa una tecla para continuar...')
            msvcrt.getch()
            continue
        match eleccion:
            case 1:
                if contador == 0:
                    contador += 1
                    asignar_sueldos_aleatorios()
                    print('Se han asignado los sueldos aleatorios.')
                    print('\nPulsa una tecla para continuar...')
                    msvcrt.getch()
                elif contador > 0:
                    print("Ya has asignado sueldos aleatorios anteriormente...")
                    print('\nPulsa una tecla para continuar...')
                    msvcrt.getch()
                    continue
            case 2:
                if contador == 0:
                    print("Primero debes generar los sueldos aleatorios.")
                    print('\nPulsa una tecla para continuar...')
                    msvcrt.getch()
                    continue
                elif contador > 0:
                    os.system('cls')
                    clasificar_sueldos()
                    print('\nPulsa una tecla para continuar...')
                    msvcrt.getch()
                    continue
            case 3:
                if contador <= 0:
                    print("Primero debes generar los sueldos aleatorios.")
                    print('\nPulsa una tecla para continuar...')
                    msvcrt.getch()
                    continue
                elif contador == 1:
                    contador = contador + 1
                    sueldo_rango()
                    ver_estadistica()
                    print('\nPulsa una tecla para continuar...')
                    msvcrt.getch()
                    continue
                elif contador > 1:
                    ver_estadistica()
                    print('\nPulsa una tecla para continuar...')
                    msvcrt.getch()
                    continue
            case 4:
                if contador == 0:
                    print("Primero debes generar los sueldos aleatorios.")
                    print('\nPulsa una tecla para continuar...')
                    msvcrt.getch()
                    continue
                elif contador >= 1:
                    reporte_sueldos()
                    print('Se ha generado el reporte de sueldos en "informe.csv".')
                    print('\nPulsa una tecla para continuar...')
                    msvcrt.getch()
                    continue
            case 5:
                print('Hasta pronto :)')
                time.sleep(2.7)
                os.system('cls')
                print('Finalizando programa...')
                time.sleep(1.5)
                print('Desarrollado por Benjamin Lizama')
                print('RUT 21.910.844-3')
                return
            case Default:
                print('Por favor ingrese una de las opciones(1-5).')
                print('\nPulsa una tecla para continuar...')
                msvcrt.getch()
                pass

menu()
