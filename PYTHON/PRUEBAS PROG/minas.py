"""
En esta solución del busca minas, se ha estructurado el código para que sea claro y fácil de seguir. 

Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible y mantenible. 

Además, se han utilizado constantes para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

**DCS.2023.11.19**
¿Qué debéis hacer con este programa?
------------------------------------

- Controlar las posibles excepciones que se puedan producir en el código.

- Desarrollar la función colocar_minas que tiene la siguiente descripción:

  Esta función coloca las minas en el tablero de juego. 
  Se asegura de que el número de minas colocadas sea igual a NUMERO_MINAS.

- Actualiza el código de la función contar_minas_adyacentes para que retorne 
el número total de minas adyacentes que tiene la celda.

  Ejemplo: la celda (3,3) tiene 3 minas en sus celdas adyacentes...

  1 2 3 4 5 6 7 8
 1  1 2 2 1
 2  1 * * 1 
 3  1 3 2 2
 4    1 * 1
 5    1 1 1
 6
 7
 8

  * Ayuda: Puedes usar 2 bucles para recorrer las celdas adyacentes y acumular las 
  minas que encuentres. Pero cuidado con comprobar celdas que estén fuera del rango
  FILAS x COLUMNAS (utiliza las constantes para asegurarte).

- Consejo 1: depura el programa en la función calcular_numeros porque es 
  que soluciones un grave pufo que el programador-becario anterior ha dejado.

- Desarrollar el contenido de la función imprimir_tablero. Podéis usar cómo base la
  función imprimir_tablero_oculto. Analizad dónde se llama a imprimir_tablero y pensad
  bien qué debe mostrar.

- Consejo 2: Nuestro amigo programador-becario dejó otro gran pufo en pedir_accion y
  revelar_celda.

- Consejo 3: La función marcar_celda no funciona cómo debería... 
  ¿otro regalo de nuestro amigo?

- Comprueba por qué no funciona la función jugar()... yo que tú empezaba a depurar.

"""

import random

# Acciones del jugador
MARCAR = "M"
REVELAR = "R"

# Dimensiones del tablero
FILAS = 8
COLUMNAS = 8
NUMERO_MINAS = 10

# Representación del tablero
VACIO = " "
MINA = "*"
BANDERA = "F"
VALOR_CELDA_DEFECTO = "."


def generar_tablero() -> list:
    """
    Esta función genera un tablero de juego vacío y coloca las minas en el tablero. Luego, calcula el número de minas adyacentes a cada celda.
    :return: tablero de juego
    """
    tablero = [[VACIO for _ in range(COLUMNAS)] for _ in range(FILAS)]
    #TODO: colocar las minas en el tablero
    colocar_minas(tablero)
    calcular_numeros(tablero)
    return tablero


def colocar_minas(tablero: list):
    """
    Esta función coloca las minas en el tablero de juego. Se asegura de que el número de minas colocadas sea igual a NUMERO_MINAS.
    """
    cont = 1
    while cont <= NUMERO_MINAS:
        fila = random.randint(0,7)
        columna = random.randint(0, 7)
        if tablero[fila][columna] == VACIO:
            tablero[fila][columna] = MINA
            cont += 1




def calcular_numeros(tablero):
    """
    Esta función calcula el número de minas adyacentes a cada celda del tablero. Si la celda no contiene una mina, se coloca el número de minas adyacentes en la celda. Si la celda contiene una mina, se deja como está.
    :param tablero: tablero de juego
    """
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if tablero[fila][columna] != MINA:
                numero_minas = contar_minas_adyacentes(tablero, fila, columna)
                if numero_minas > 0:
                    tablero[fila][columna] = str(numero_minas)


def contar_minas_adyacentes(tablero, fila, columna):
    """
    Esta función cuenta el número de minas adyacentes a la celda(i,j) seleccionada.
    :param tablero: tablero de juego
    :param fila: fila de la celda seleccionada
    :param columna: columna de la celda seleccionada
    :return: número de minas adyacentes a la celda(i,j) seleccionada
    """
    minas = 0

    for i in range(fila - 1, fila +2):
        for j in range(columna - 1, columna +2):
            if 0 <= i < FILAS and 0 <= j< COLUMNAS:
                if tablero[i][j] == MINA:
                    minas += 1
    return minas


def imprimir_tablero(tablero):
    """
    Esta función toma el tablero como argumento e imprime cada celda del tablero.
    :param tablero: tablero de juego
    """
    print("  " + " ".join(str(i + 1) for i in range(COLUMNAS)))
    for fila in range(FILAS):
        print(str(fila + 1), end=" ")
        for columna in range(COLUMNAS):
                if tablero[fila][columna] == VACIO:
                    print(VALOR_CELDA_DEFECTO, end=" ")
                else:
                    print(tablero[fila][columna], end=" ")
        print()


def imprimir_tablero_oculto(tablero, celdas_reveladas, celdas_maracadas):
    """
    Imprime cada celda del tablero: si la celda ha sido revelada o marcada con una bandera, muestra su contenido actual (número, vacio_revelado o bandera); si no, muestra la celda como vacía.
    :param tablero: tablero de juego
    :param celdas_reveladas: conjunto de celdas que ya han sido mostradas al jugador
    :param celdas_maracadas: conjunto de celdas que han sido marcadas con una bandera
    """
    print("  " + " ".join(str(i + 1) for i in range(COLUMNAS)))
    for fila in range(FILAS):
        print(str(fila + 1), end=" ")
        for columna in range(COLUMNAS):
            if (fila, columna) in celdas_reveladas:
                if tablero[fila][columna] == VACIO:
                    tablero[fila][columna] = VALOR_CELDA_DEFECTO
                print(tablero[fila][columna], end=" ")
            elif (fila, columna) in celdas_maracadas:
                print(BANDERA, end=" ")
            else:
                print(VACIO, end=" ")
        print()


def pedir_accion():
    """
    Esta función pide al jugador que ingrese una acción, una fila y una columna.
    Si la acción no es válida, se le pide al jugador que ingrese una acción nuevamente.
    Si la fila o la columna no son válidas, se le pide al jugador que ingrese una fila o columna nuevamente.
    :return: acción, fila y columna ingresadas por el jugador
    """
    accion_valida = False
    while not accion_valida:
        
        accion = input("Elige una acción (R para revelar, M para marcar): ").upper()
        try:
            fila = int(input("Ingresa la fila (1-8): ")) - 1
            columna = int(input("Ingresa la columna (1-8): ")) - 1
        except ValueError:
            fila = -1
            columna = -1

        if accion in [REVELAR, MARCAR] and 0 <= fila < FILAS and 0 <= columna < COLUMNAS:
            accion_valida = True
        else:
            print("Acción inválida. Inténtalo de nuevo.")
    return accion, fila, columna


def revelar_celda(tablero, celdas_reveladas, celdas_marcadas, fila, columna) -> bool:
    """
    Esta función revela la celda seleccionada.
    Si la celda contiene una mina, devuelve False.
    Si la celda no contiene una mina, se agrega a celdas_reveladas y devuelve True.
    :param tablero: tablero de juego
    :param celdas_reveladas: conjunto de celdas que ya han sido mostradas al jugador
    :param celdas_marcadas: conjunto de celdas que han sido marcadas con una bandera
    :param fila: fila de la celda seleccionada
    :param columna: columna de la celda seleccionada
    :return: False si la celda contiene una mina, True en caso contrario
    """
    revelada = True
    if tablero[fila][columna] == MINA:  # La celda contiene una mina
        revelada = False
    elif tablero[fila][columna] != VACIO:  # La celda contiene un número
        celdas_reveladas.add((fila, columna))
        celdas_marcadas.discard((fila, columna))
    else:  # La celda está vacía
        revelar_celdas_vacias(tablero, celdas_reveladas, celdas_marcadas, fila, columna)
    return revelada



def revelar_celdas_vacias(tablero, celdas_reveladas, celdas_marcadas, fila, columna):
    """
    Esta función revela la celda seleccionada. Si está vacía, revela recursivamente las celdas vacías adyacentes a la celda seleccionada.
    :param tablero: tablero de juego
    :param celdas_reveladas: conjunto de celdas que ya han sido mostradas al jugador
    :param celdas_marcadas: conjunto de celdas que han sido marcadas con una bandera
    :param fila: fila de la celda seleccionada
    :param columna: columna de la celda seleccionada
    """
    if (fila, columna) not in celdas_reveladas:
        celdas_reveladas.add((fila, columna))
        celdas_marcadas.discard((fila, columna))
        # Si la celda esta vacía, revela también las celdas adyacentes
        if tablero[fila][columna] == VACIO:
            # Recursivamente revela las celdas adyacentes
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= fila + i < FILAS and 0 <= columna + j < COLUMNAS:
                        revelar_celdas_vacias(tablero, celdas_reveladas, celdas_marcadas, fila + i, columna + j)


def marcar_celda(celdas_marcadas, fila, columna, tablero):
    """
    Esta función marca la celda seleccionada con una bandera.
    :param tablero: tablero de juego
    :param celdas_marcadas: conjunto de celdas que han sido marcadas con una bandera
    :param fila: fila de la celda seleccionada
    :param columna: columna de la celda seleccionada
    """
    if (fila, columna) in celdas_marcadas:
        celdas_marcadas.add((fila, columna))
        tablero[fila][columna] = BANDERA


def verificar_victoria(tablero, celdas_reveladas) -> bool:
    """
    Esta función verifica si el jugador ha ganado el juego. Que se daŕa solo y solo si todas las celdas que no contienen
    minas han sido reveladas.
    :param tablero: tablero de juego
    :param celdas_reveladas: conjunto de celdas que ya han sido mostradas al jugador
    :return: True si el jugador ha ganado, False de lo contrario
    """
    victoria = True

    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if tablero[fila][columna] != MINA and (fila, columna) not in celdas_reveladas:
                victoria = False
    return victoria


def jugar():
    """
    Esta función ejecuta el juego. Primero genera un tablero de juego, luego pide al jugador que ingrese una acción, una fila y una columna. Luego, revela la celda seleccionada y verifica si el jugador ha ganado o perdido el juego. Si el jugador ha ganado o perdido, termina el juego. Si no, pide al jugador que ingrese una acción, una fila y una columna nuevamente.
    """
    tablero = generar_tablero()
    celdas_reveladas = set()
    celdas_marcadas = set()
    terminar_juego = False

    while not terminar_juego:

        imprimir_tablero_oculto(tablero, celdas_reveladas, celdas_marcadas)

        accion, fila, columna = pedir_accion()

        if accion == REVELAR:
            celda_con_mina = not revelar_celda(tablero, celdas_reveladas, celdas_marcadas, fila, columna)

            if celda_con_mina:
                print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡Oh no! ¡Has pisado una mina!!!!!!!!!!!!!!!!!!!!!")
                imprimir_tablero(tablero)
                terminar_juego = True
            elif verificar_victoria(tablero, celdas_reveladas):
                print("¡Felicidades! ¡Has ganado el juego!")
                imprimir_tablero(tablero)
                terminar_juego = True
        elif accion == MARCAR:
            marcar_celda(tablero, celdas_marcadas, fila, columna)


if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    jugar()