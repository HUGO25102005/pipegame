import pygame
import random

# Definir el tamaño de la ventana y el tablero
ANCHO = 1366
ALTO = 768
TAMANO_CELDA = 40
FONDO_COLOR = (173, 216, 230)  # Azul pastel
LETRA_COLOR = (0, 0, 0)
PALABRAS = ["SOLAR", 
            "EOLICA",
            "BIOMASA", 
            "HIDRAULICA", 
            "GEOTERMICA", 
            "MAREMOTO"]



# Matriz de letras (15x15)
MATRIZ_LETRAS = [
                                                            ["S", "O", "L", "A", "M", "A", "R", "E", "M", "O", "T", "A", "I", "C", "A"],
                                                            ["E", "O", "L", "I", "C", "A", "H", "I", "D", "R", "O", "G", "E", "O", "L"],
                                                            ["B", "G", "E", "O", "T", "E", "R", "M", "I", "C", "A", "R", "O", "L", "O"],
                                                            ["D", "I", "A", "S", "O", "R", "O", "C", "E", "L", "A", "R", "E", "S", "N"],
                                                            ["R", "C", "A", "I", "H", "I", "D", "R", "A", "U", "L", "I", "C", "A", "L"],
                                                            ["O", "A", "T", "O", "N", "O", "S", "U", "T", "R", "O", "S", "L", "A", "E"],
                                                            ["G", "E", "N", "E", "R", "A", "D", "O", "R", "E", "A", "L", "C", "O", "E"],
                                                            ["E", "B", "I", "O", "M", "A", "A", "S", "A", "O", "M", "A", "S", "A", "E"],
                                                            ["O", "S", "C", "A", "R", "E", "A", "T", "M", "N", "T", "N", "M", "T", "A"],
                                                            ["I", "R", "E", "E", "C", "E", "E", "A", "L", "A", "T", "R", "I", "E", "A"],
                                                            ["C", "A", "R", "B", "I", "E", "O", "L", "I", "C", "A", "A", "L", "A", "C"],
                                                            ["H", "R", "N", "E", "E", "N", "A", "L", "A", "N", "O", "T", "L", "E", "G"],
                                                            ["D", "S", "A", "L", "B", "D", "T", "A", "M", "S", "A", "S", "A", "L", "N"],
                                                            ["R", "S", "O", "L", "A", "R", "B", "O", "I", "L", "A", "S", "R", "O", "A"],
                                                            ["L", "S", "C", "A", "R", "E", "T", "E", "R", "M", "I", "C", "A", "E", "E"]
]

# Agregar palabras al tablero
def agregar_palabras(matriz, palabras):
    for palabra in palabras:
        fila, columna = random.randint(0, 14), random.randint(0, 14)
        direccion = random.choice(["horizontal", "vertical"])
        if direccion == "horizontal":
            while columna + len(palabra) > 15:
                fila, columna = random.randint(0, 14), random.randint(0, 14)
            for i in range(len(palabra)):
                matriz[fila][columna + i] = palabra[i]
        else:  # Dirección vertical
            while fila + len(palabra) > 15:
                fila, columna = random.randint(0, 14), random.randint(0, 14)
            for i in range(len(palabra)):
                matriz[fila + i][columna] = palabra[i]

agregar_palabras(MATRIZ_LETRAS, PALABRAS)

# Inicializar Pygame
pygame.init()

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)
pygame.display.set_caption("Sopa de Letras")

# Centrar la ventana en la pantalla
ventana_rect = ventana.get_rect()
ventana_rect.center = pygame.display.get_surface().get_rect().center
ventana.blit(pygame.display.get_surface(), (0, 0), ventana_rect)

# Definir la velocidad de fotogramas (FPS)
FPS = 30
clock = pygame.time.Clock()

# Texto de indicación debajo del tiempo
fuente_indicacion = pygame.font.Font(None, 24)
texto_indicacion = fuente_indicacion.render("Encuentra palabras relacionadas con energías renovables", True, LETRA_COLOR)
texto_rect = texto_indicacion.get_rect()
texto_rect.topleft = (ANCHO - 500, 40)  # Ajusta la posición vertical para que esté debajo del tiempo
ventana.blit(texto_indicacion, texto_rect.topleft)

# Lista de palabras para encontrar
palabras_encontradas = []

# Inicializar variables de selección
seleccionando = False
x_inicio, y_inicio = -1, -1
x_fin, y_fin = -1, -1
color_seleccion = 0

# Variable para la palabra actual
palabra_actual = ""

# Variable para el tiempo restante (en milisegundos)
tiempo_maximo = 180000  # 3 minutos en milisegundos
tiempo_inicio = pygame.time.get_ticks()

# Variable para verificar si todas las palabras se han encontrado
todas_encontradas = False

# Variable para verificar si el juego ha sido ganado
juego_ganado = False

# Variable de Perdiste
perdiste = False

# Variable para rastrear si el juego ha terminado
juego_terminado = False

# Inicialización de las variables de selección
seleccionando = False
x_inicio, y_inicio = -1, -1
x_fin, y_fin = -1, -1
color_seleccion = 0

# Bucle principal del juego
terminado = False
x_inicio, y_inicio, x_fin, y_fin = -1, -1, -1, -1
seleccionando = False

while not terminado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True
        elif evento.type == pygame.VIDEORESIZE:
            ANCHO, ALTO = evento.w, evento.h
            ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)

        # Solo procesar eventos si el juego no ha terminado
        if not juego_terminado:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = evento.pos

                # Verifica si el clic está dentro del área de juego
                if tablero_x <= x <= tablero_x + len(MATRIZ_LETRAS[0]) * TAMANO_CELDA and \
                   tablero_y <= y <= tablero_y + len(MATRIZ_LETRAS) * TAMANO_CELDA:
                    # Calcular la posición de inicio ajustada al centro de la matriz
                    x_inicio = max(0, min(len(MATRIZ_LETRAS[0]) - 1, (x - tablero_x) // TAMANO_CELDA))
                    y_inicio = max(0, min(len(MATRIZ_LETRAS) - 1, (y - tablero_y) // TAMANO_CELDA))
                    seleccionando = True
                    color_seleccion = (color_seleccion + 1) % 255

            elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                x, y = evento.pos

                # Verifica si el clic está dentro del área de juego
                if tablero_x <= x <= tablero_x + len(MATRIZ_LETRAS[0]) * TAMANO_CELDA and \
                   tablero_y <= y <= tablero_y + len(MATRIZ_LETRAS) * TAMANO_CELDA:
                    # Calcular la posición final ajustada al centro de la matriz
                    x_fin = max(0, min(len(MATRIZ_LETRAS[0]) - 1, (x - tablero_x) // TAMANO_CELDA))
                    y_fin = max(0, min(len(MATRIZ_LETRAS) - 1, (y - tablero_y) // TAMANO_CELDA))
                    seleccionando = False

                    # Verifica si estás seleccionando horizontal o verticalmente
                    if x_inicio == x_fin:
                        for i in range(len(PALABRAS[0])):
                            if 0 <= x_inicio + i < len(MATRIZ_LETRAS[y_inicio]):
                                palabra_actual += MATRIZ_LETRAS[y_inicio][x_inicio + i]
                            else:
                                break
                    elif y_inicio == y_fin:
                        for i in range(len(PALABRAS[0])):
                            if 0 <= y_inicio + i < len(MATRIZ_LETRAS):
                                palabra_actual += MATRIZ_LETRAS[y_inicio + i][x_inicio]

                    # Verifica si la palabra seleccionada es válida y realiza las acciones necesarias
                    if palabra_actual.upper() in PALABRAS and palabra_actual.upper() not in palabras_encontradas:
                        palabras_encontradas.append(palabra_actual.upper())
                        if len(palabras_encontradas) == len(PALABRAS):
                            todas_encontradas = True
                            tiempo_terminado = pygame.time.get_ticks()
                            juego_ganado = True

                    x_inicio, y_inicio, x_fin, y_fin = -1, -1, -1, -1

     

     # Calcular el tiempo restante
    tiempo_actual = pygame.time.get_ticks()
    tiempo_restante = max(0, tiempo_maximo - (tiempo_actual - tiempo_inicio))

    # Calcular el tiempo restante solo si no se han encontrado todas las palabras
    if not todas_encontradas:
        tiempo_actual = pygame.time.get_ticks()
        tiempo_restante = max(0, tiempo_maximo - (tiempo_actual - tiempo_inicio))


    # Verificar si todas las palabras se han encontrado
    if todas_encontradas:
        tiempo_terminado = pygame.time.get_ticks()
        juego_ganado = True
    
    # Verificar si el tiempo ha llegado a cero
    if tiempo_restante == 0:
        juego_terminado = True

    # Verificar si el juego ha terminado (ganado o perdido)
    if juego_ganado or tiempo_restante == 0:
        juego_terminado = True
    ventana.fill(FONDO_COLOR)  # Limpiar la ventana antes de redibujar

    # Dibujar el contador regresivo en la parte superior derecha
    minutos_restantes = tiempo_restante // 60000
    segundos_restantes = (tiempo_restante % 60000) // 1000
    if tiempo_restante > 0:
        tiempo_texto = f"Tiempo restante: {minutos_restantes:02}:{segundos_restantes:02}"
    fuente_tiempo = pygame.font.Font(None, 24)
    texto_tiempo = fuente_tiempo.render(tiempo_texto, True, LETRA_COLOR)
    ventana.fill(FONDO_COLOR)
    ventana.blit(texto_tiempo, (ANCHO - texto_tiempo.get_width() - 10, 10))

    # Dibujar el tablero centrado en la ventana
    tablero_x = (ANCHO - len(MATRIZ_LETRAS[0]) * TAMANO_CELDA) // 2 + 10  # Ajuste hacia la derecha
    tablero_y = (ALTO - len(MATRIZ_LETRAS) * TAMANO_CELDA) // 2 + 30  # Ajuste hacia abajo
    for y, fila in enumerate(MATRIZ_LETRAS):
        for x, letra in enumerate(fila):
            fuente = pygame.font.Font(None, 36)
            texto = fuente.render(letra, True, LETRA_COLOR)
            ventana.blit(texto, (tablero_x + x * TAMANO_CELDA, tablero_y + y * TAMANO_CELDA))

    # ...

    # Dibujar el rectángulo de selección centrado en la ventana
    if seleccionando:
        pygame.draw.rect(
            ventana,
            (color_seleccion, 0, 0),
            (
                tablero_x + min(x_inicio, x_fin) * TAMANO_CELDA,
                tablero_y + min(y_inicio, y_fin) * TAMANO_CELDA,
                (abs(x_fin - x_inicio) + 1) * TAMANO_CELDA,
                (abs(y_fin - y_inicio) + 1) * TAMANO_CELDA
            ),
            2
        )


    
    # Dibujar el texto de indicación
    ventana.blit(texto_indicacion, texto_rect)

    # Mostrar la lista de palabras a encontrar hacia abajo
    fuente_lista_palabras = pygame.font.Font(None, 24)
    y_pos = 100  # Posición inicial en el eje Y

    for palabra in PALABRAS:
        texto_lista_palabras = fuente_lista_palabras.render(palabra, True, LETRA_COLOR)
        ventana.blit(texto_lista_palabras, (ANCHO - texto_lista_palabras.get_width() - 10, y_pos))
        y_pos += 30  # Ajusta el espacio vertical entre las palabras


    # Dibujar el rectángulo de selección
    if seleccionando:
        pygame.draw.rect(
            ventana,
            (color_seleccion, 0, 0),
            (min(x_inicio, x_fin) * TAMANO_CELDA, min(y_inicio, y_fin) * TAMANO_CELDA, (abs(x_fin - x_inicio) + 1) * TAMANO_CELDA, (abs(y_fin - y_inicio) + 1) * TAMANO_CELDA),
            2
        )

    # Colores Palabras
    COLORES_PALABRAS = {
        "SOLAR": (255, 0, 0),  # Rojo
        "EOLICA": (0, 255, 0),  # Verde
        "BIOMASA": (0, 0, 255),  # Azul
        "HIDRAULICA": (255, 255, 0),  # Amarillo
        "GEOTERMICA": (255, 0, 255),  # Magenta
        "MAREMOTO": (0, 255, 255)  # Cian
    }

    # Dibujar la palabra actual
    fuente_palabra = pygame.font.Font(None, 24)
    if palabra_actual.upper() in COLORES_PALABRAS:
        color_palabra = COLORES_PALABRAS[palabra_actual.upper()]
    else:
        color_palabra = LETRA_COLOR

    texto_palabra = fuente_palabra.render(palabra_actual, True, color_palabra)
    ventana.blit(texto_palabra, (10, ALTO - 30))

    # Colorear la palabra en la matriz de letras cuando se selecciona
    if palabra_actual.upper() in COLORES_PALABRAS:
        color_palabra = COLORES_PALABRAS[palabra_actual.upper()]
        for y in range(min(y_inicio, y_fin), max(y_inicio, y_fin) + 1):
            for x in range(min(x_inicio, x_fin), max(x_inicio, x_fin) + 1):
                if 0 <= y < len(MATRIZ_LETRAS) and 0 <= x < len(MATRIZ_LETRAS[y]):
                    fuente = pygame.font.Font(None, 36)
                    texto = fuente.render(MATRIZ_LETRAS[y][x], True, color_palabra)
                    ventana.blit(texto, (15 + x * TAMANO_CELDA, y * TAMANO_CELDA))

    # Dibujar la barra de palabras encontradas
    fuente_barra = pygame.font.Font(None, 24)
    barra_texto = "Palabras encontradas: " + ", ".join(palabras_encontradas)
    texto_barra = fuente_barra.render(barra_texto, True, LETRA_COLOR)
    ventana.blit(texto_barra, (10, ALTO - 60))

    # Mostrar mensaje "¡Ganaste!" si se encontraron todas las palabras
    if juego_ganado:
        fuente_ganaste = pygame.font.Font(None, 72)
        texto_ganaste = fuente_ganaste.render("¡Ganaste!", True, (0, 0, 255))
        ventana.blit(texto_ganaste, (ANCHO // 2 - texto_ganaste.get_width() // 2, ALTO // 2 - texto_ganaste.get_height() // 2))

    # Mostrar mensaje "¡Perdiste!" si se acabó el tiempo
    if juego_terminado and not juego_ganado:
        fuente_perdiste = pygame.font.Font(None, 72)
        texto_perdiste = fuente_perdiste.render("¡Perdiste!", True, (255, 0, 0))
        ventana.blit(texto_perdiste, (ANCHO // 2 - texto_perdiste.get_width() // 2, ALTO // 2 - texto_perdiste.get_height() // 2))

    pygame.display.update()

    # Verificar si el juego ha terminado (ganado o perdido)
    if juego_ganado or tiempo_restante == 0:
        juego_terminado = True

    clock.tick(FPS)

# Finalizar Pygame
pygame.quit()
