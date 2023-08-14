# tupla con los dos valores establecidos para ganador(5) y perdedor (-2)
valores = (5, -2)
# diccionario jugadores con puntaje en 0
jugadores = {}
# diccionario historial
historial = {}
# numero de rondas que se van a jugar
rondas = [1, 2, 3, 4, 5, 6]

# Función definida para actualizar el puntaje de los jugadores, restriccion de maximo y monimo en el puntaje
def actualizar_puntaje(jugador, eleccion):
    global jugadores
    if eleccion == "ganar":
        jugadores[jugador] = max(-10, min(20, jugadores[jugador] + valores[0]))
    elif eleccion == "perder":
        jugadores[jugador] = max(-10, min(20, jugadores[jugador] + valores[1]))


# Bucle para ejecucion del juego, agregar nombre del jugador y agregar eleccion para el historial
print("Bienvenido al juego de puntos.")
for ronda in rondas:
    print(f"Ronda {ronda}:")
    nombre = input("Nombre del jugador: ")
    if nombre not in jugadores:
        jugadores[nombre] = 0
        historial[nombre] = {'ganar': [], 'perder': []}

    eleccion = input("¿Ganó o perdió? (ganar/perder): ").lower()
    while eleccion not in ["ganar", "perder"]:
        eleccion = input("Por favor, responde 'ganar' o 'perder': ").lower()

    actualizar_puntaje(nombre, eleccion)
    historial[nombre][eleccion].append(ronda)

# Imprimir el puntaje final y el historial de cada jugador
print("\nPuntajes finales:")
for jugador, puntaje in jugadores.items():
    print(f"{jugador}: {puntaje}")
    print(f"Historial de {jugador}:")
    print(f"Rondas ganadas: {historial[jugador]['ganar']}")
    print(f"Rondas perdidas: {historial[jugador]['perder']}")
