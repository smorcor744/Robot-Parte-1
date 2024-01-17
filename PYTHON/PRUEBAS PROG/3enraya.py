import os

FICHAS = (" ","X", "O")

def borrarConsola():
    """ Limpiar la consola """
    os.system("cls")


def pulse_tecla_para_continuar():
    """Mostrar el mensaje Presione unatecla para continuar y hacer una pasuda hasta que se realice la acción"""
    os.system("pause")


def crear_fila(num_columnas = 3) -> list:
    return list(0 for _ in range(num_columnas))


def crear_tablero(num_filas = 3) -> tuple:
    """ Crea el tablero 3x3
    :para num_filas: números de filas del tablero"""
    return tuple(crear_fila() for _ in range(num_filas)) 

def mostrar_fila(fila:list):
    contenido_fila = "| "
    for celda in fila:
        contenido_fila += FICHAS[celda] + " | "
    print(contenido_fila)


def mostrar_tablero(tablero:tuple):
    borrarConsola()
    print("-"*13)
    for fila in tablero:
        mostrar_fila(fila)
        print("-"*13)


def cambiar_turno(turno: int) -> int:
    if turno % 2 == 0:
        return 1
    return 2


def jugar(tablero: tuple, jugador: int):
    turno = 0
    ronda = 0
    hay_ganador = False
    while not hay_ganador:

        turno = cambiar_turno(turno)
        if turno ==1:
            ronda += 1

        print(f"\nRONDA {ronda}")
        print("-" * len(f"RONDA {ronda}") + "\n")
        

        colocar_ficha(tablero, jugador)
        mostrar_tablero(tablero)

        if ronda >=3:
            ganador, hay_ganador = verificar_ganador(tablero)

        if hay_ganador:
            print(f"\n¡El jugador {ganador} ha ganado!\n")
        
        if ronda == 9:
            hay_ganador = True
            print("\n¡Empate!\n")


def verificar_ganador(tablero) -> tuple:
    for i in range(3):
        print("")

def colocar_ficha(tablero: tuple, jugador: int):
    """Solicita a un jugador las posiciones de la ficha que va a colocar."""
    pos_ficha = {"fila":None, "columna":None}
    pos_correcta = False
    while not pos_correcta:
        pos_ficha["fila"] = pedir_posicion("fila", f"\nJugador {jugador}, coloque una ficha...")
        pos_ficha["columna"] = pedir_posicion("columna")

        pos_correcta = comprobar_casilla(tablero, pos_ficha)

        if pos_correcta:
            tablero[pos_ficha["fila"]][pos_ficha["columna"]] = jugador
        else:
            pos_ficha["fila"] = pos_ficha["columna"] = None
            print("**Error** movimiento inválido")
            pulse_tecla_para_continuar()
            mostrar_tablero()

def comprobar_casilla(tablero: tuple, pos_ficha: dict) -> bool:
    return tablero[pos_ficha["fila"]][pos_ficha["columna"]] == 0


def pedir_posicion(fila_col: str, msj: str = "") -> int:

    pos = None
    if msj != "": print(msj)
    while pos == None:
        try:
            pos = int(input(f"Elige la {fila_col} (1, 2, 3): "))- 1
            if not 0 <= pos <= 2:
                raise ValueError

        except ValueError:
            pos = None
            print(f"**Error** {fila_col} no válida")
    return pos

def main():
    tablero = crear_tablero()
    mostrar_tablero(tablero)
    jugar(tablero)





if __name__ == "__main__":
    main()