import pygame
import random

# Definir el tamaño de la ventana y el tablero
ANCHO = 1366
ALTO = 768
TAMANO_CELDA = 40

# Cargar la imagen de fondo
FONDO_IMAGEN = pygame.image.load("images/mary.png")  # Reemplaza "ruta_de_la_imagen.jpg" con la ruta de tu imagen
FONDO_IMAGEN = pygame.transform.scale(FONDO_IMAGEN, (ANCHO, ALTO))

LETRA_COLOR = (255, 255, 255)
PALABRAS = ["SOLAR", 
            "EOLICA",
            "BIOMASA", 
            "HIDRAULICA", 
            "GEOTERMICA", 
            "MAREMOTO"]



# Matriz de letras (15x15)
MATRIZ_LETRAS = MATRIZ_LETRAS = [
    ["S", "O", "L", "A", "E", "O", "L", "I", "C", "A", "I", "C", "A", "E", "O"],
    ["H", "O", "C", "E", "C", "A", "A", "I", "D", "R", "O", "G", "E", "O", "L"],
    ["B", "M", "E", "O", "T", "E", "R", "M", "I", "C", "A", "R", "O", "L", "O"],
    ["D", "A", "A", "S", "O", "R", "O", "C", "G", "L", "H", "R", "E", "S", "N"],
    ["R", "R", "A", "I", "H", "I", "D", "R", "E", "U", "I", "I", "C", "A", "L"],
    ["O", "E", "T", "O", "M", "A", "S", "A", "O", "R", "D", "S", "L", "A", "E"],
    ["G", "M", "N", "E", "R", "A", "D", "O", "T", "E", "R", "L", "C", "O", "E"],
    ["E", "O", "I", "O", "M", "A", "A", "S", "E", "O", "A", "A", "S", "A", "E"],
    ["O", "T", "C", "A", "R", "E", "A", "T", "R", "N", "U", "N", "M", "T", "A"],
    ["I", "A", "E", "E", "C", "E", "E", "A", "M", "A", "L", "R", "I", "E", "A"],
    ["C", "A", "R", "B", "I", "E", "O", "L", "I", "C", "I", "A", "L", "A", "C"],
    ["H", "R", "N", "E", "E", "N", "A", "L", "C", "N", "C", "T", "L", "E", "G"],
    ["D", "S", "O", "L", "A", "R", "T", "A", "A", "S", "A", "S", "A", "L", "N"],
    ["R", "X", "D", "F", "E", "R", "B", "O", "I", "L", "A", "S", "R", "O", "A"],
    ["L", "S", "C", "A", "R", "E", "T", "E", "R", "M", "I", "C", "A", "E", "E"]
]
# Matriz de selección (inicialmente todas las celdas no seleccionadas)
MATRIZ_SELECCION = [[False] * 15 for _ in range(15)]

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
FPS = 60
clock = pygame.time.Clock()

# Texto de indicación debajo del tiempo
fuente_indicacion = pygame.font.Font(None, 36)
texto_indicacion = fuente_indicacion.render(" Encuentra palabras relacionadas con energías renovables ", True, LETRA_COLOR)
texto_rect = texto_indicacion.get_rect()
texto_rect.topleft = (ANCHO - 400, 40)  # Ajusta la posición vertical para que esté debajo del tiempo
ventana.blit(texto_indicacion, texto_rect.topleft)

# Lista de palabras para encontrar
palabras_encontradas = []

# Escalar la imagen de fondo al tamaño de la ventana
fondo_escalado = pygame.transform.scale(FONDO_IMAGEN, (ANCHO, ALTO))

# Inicializar variables de selección
seleccionando = False
x_inicio, y_inicio = -1, -1
x_fin, y_fin = -1, -1
color_seleccion = 0

# Variable para la palabra actual
palabra_actual = ""

# Definir la fuente para el tiempo
fuente_tiempo = pygame.font.Font(None, 40)

# Definir el tiempo de inicio
tiempo_inicio = pygame.time.get_ticks()

# Definir el tiempo máximo en milisegundos
tiempo_maximo = 900000 # 3 minutos en milisegundos

# Calcular el tiempo restante en segundos
tiempo_restante = (tiempo_maximo - (pygame.time.get_ticks() - tiempo_inicio)) // 1000
tiempo_texto = f"Tiempo: {tiempo_restante} segundos"

# Dibujar el tiempo restante en la parte superior central
texto_tiempo = fuente_tiempo.render(tiempo_texto, True, LETRA_COLOR)
ventana.blit(texto_tiempo, ((ANCHO - texto_tiempo.get_width()) // 2, 200))

# Mostrar la lista de palabras a encontrar justo debajo del tiempo
fuente_lista_palabras = pygame.font.Font(None, 40)
y_pos = 50 + texto_tiempo.get_height()  # Ajusta la posición en el eje Y

for palabra in PALABRAS:
    texto_lista_palabras = fuente_lista_palabras.render(palabra, True, LETRA_COLOR)
    ventana.blit(texto_lista_palabras, ((ANCHO - texto_lista_palabras.get_width()) // 2, y_pos))
    y_pos += 40  # Ajusta el espacio vertical entre las palabras

# Variable para verificar si todas las palabras se han encontrado
todas_encontradas = False

# Variable para verificar si el juego ha sido ganado
juego_ganado = False

# Variable de Perdiste
perdiste = False

# Variable para rastrear si el juego ha terminado
juego_terminado = False

seleccionando = False
x_inicio, y_inicio, x_fin, y_fin = -1, -1, -1, -1

# Bucle principal del juego
terminado = False
x_inicio, y_inicio, x_fin, y_fin = -1, -1, -1, -1
seleccionando = False

# Ajuste de posición para las palabras encontradas
y_pos_palabras = ALTO - 30

# Centrar la ventana en la pantalla
ventana_rect = ventana.get_rect()
ventana_rect.center = pygame.display.get_surface().get_rect().center
ventana.blit(pygame.display.get_surface(), (0, 0), ventana_rect)

# Texto de indicación debajo del tiempo
fuente_indicacion = pygame.font.Font(None, 36)  # Tamaño de fuente más grande
texto_indicacion = fuente_indicacion.render("Encuentra palabras relacionadas con energías renovables", True, LETRA_COLOR)
texto_rect = texto_indicacion.get_rect()

# Ajustar la posición vertical para centrar en la parte superior
texto_rect.topleft = (ventana_rect.width - texto_indicacion.get_width()) // 2, 10
texto_rect.topleft = (ventana_rect.height - texto_indicacion.get_height()) // 2, 9
ventana.blit(texto_indicacion, texto_rect.topleft)

# Escalar la imagen de fondo al tamaño de la ventana
fondo_escalado = pygame.transform.scale(FONDO_IMAGEN, (ANCHO, ALTO))



# Bucle principal del juego
while not terminado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True
        elif evento.type == pygame.VIDEORESIZE:
            ANCHO, ALTO = evento.w, evento.h
            ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)
            
            # Escalar la imagen de fondo al nuevo tamaño de la ventana
            fondo_escalado = pygame.transform.scale(FONDO_IMAGEN, (ANCHO, ALTO))

        # Verificar si la palabra actual es correcta
        palabra_correcta = palabra_actual.upper() in PALABRAS
        if palabra_correcta:
            # Define palabra_seleccionada as a list of coordinates representing the selected cells
            palabra_seleccionada = [(x, y) for x in range(x_inicio, x_fin + 1) for y in range(y_inicio, y_fin + 1)]

            # Marcar las celdas de la palabra como seleccionadas
            for x, y in palabra_seleccionada:
                MATRIZ_SELECCION[y][x] = True
                # Borrar la palabra correcta de la lista de palabras
            if palabra_actual.upper() in PALABRAS:
                PALABRAS.remove(palabra_actual.upper())

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

            elif evento.type == pygame.MOUSEMOTION:
                if seleccionando:
                    x, y = evento.pos

                    # Calcular la posición final ajustada al centro de la matriz
                    x_fin = max(0, min(len(MATRIZ_LETRAS[0]) - 1, (x - tablero_x) // TAMANO_CELDA))
                    y_fin = max(0, min(len(MATRIZ_LETRAS) - 1, (y - tablero_y) // TAMANO_CELDA))

                    # Verifica si estás seleccionando horizontal o verticalmente
                    palabra_actual = ""
                    if x_inicio == x_fin:
                        palabra_actual = "".join([MATRIZ_LETRAS[y][x_inicio] for y in range(min(y_inicio, y_fin), max(y_inicio, y_fin) + 1)])
                    elif y_inicio == y_fin:
                        palabra_actual = "".join([MATRIZ_LETRAS[y_inicio][x] for x in range(min(x_inicio, x_fin), max(x_inicio, x_fin) + 1)])

            elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                x, y = evento.pos

                # Calcular la posición final ajustada al centro de la matriz
                x_fin = max(0, min(len(MATRIZ_LETRAS[0]) - 1, (x - tablero_x) // TAMANO_CELDA))
                y_fin = max(0, min(len(MATRIZ_LETRAS) - 1, (y - tablero_y) // TAMANO_CELDA))
                seleccionando = False

                # Verifica si estás seleccionando horizontal o verticalmente
                palabra_actual = ""
                if x_inicio == x_fin:
                    palabra_actual = "".join([MATRIZ_LETRAS[y][x_inicio] for y in range(min(y_inicio, y_fin), max(y_inicio, y_fin) + 1)])
                elif y_inicio == y_fin:
                    palabra_actual = "".join([MATRIZ_LETRAS[y_inicio][x] for x in range(min(x_inicio, x_fin), max(x_inicio, x_fin) + 1)])

                # Verifica si la palabra seleccionada es válida y realiza las acciones necesarias
                if palabra_actual.upper() in PALABRAS and palabra_actual.upper() not in palabras_encontradas:
                    palabras_encontradas.append(palabra_actual.upper())
                    if len(palabras_encontradas) == len(PALABRAS):
                        todas_encontradas = True
                        tiempo_terminado = pygame.time.get_ticks()
                        juego_ganado = True

        # Verificar si el tiempo ha llegado a cero
        if tiempo_restante == 0:
            juego_terminado = True
            perdiste = True  # Se establece perdiste como True cuando el tiempo llega a cero
     

      # Ajuste de posición para las palabras encontradas
            y_pos_palabras = ALTO - 30

    # Bucle principal
    fuente_palabras_encontradas = pygame.font.SysFont("Arial", 20)

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
    ventana.blit(fondo_escalado, (0, 0))


    # Dibujar el contador regresivo en la parte superior derecha
    minutos_restantes = tiempo_restante // 60000
    segundos_restantes = (tiempo_restante % 60000) // 1000
    if tiempo_restante > 0:
        tiempo_texto = f"Tiempo restante: {minutos_restantes:02}:{segundos_restantes:02}"
    fuente_tiempo = pygame.font.Font(None, 34)
    texto_tiempo = fuente_tiempo.render(tiempo_texto, True, LETRA_COLOR)
    ventana.blit(texto_tiempo, (ANCHO - texto_tiempo.get_width() - 10, 10))

    # Dibujar el tablero centrado en la ventana con cuadrícula y selección
    tablero_x = (ANCHO - len(MATRIZ_LETRAS[0]) * TAMANO_CELDA) // 2
    SELECCION_COLOR = (255, 0, 0)  # Define the SELECCION_COLOR

    tablero_y = (ALTO - len(MATRIZ_LETRAS) * TAMANO_CELDA) // 2
    for y, fila in enumerate(MATRIZ_LETRAS):
        for x, letra in enumerate(fila):
            fuente = pygame.font.Font(None, 36)

            # Verificar si la celda está seleccionada y ajustar el color
            color = SELECCION_COLOR if MATRIZ_SELECCION[y][x] else LETRA_COLOR

            texto = fuente.render(letra, True, color)
            ventana.blit(texto, (tablero_x + x * TAMANO_CELDA + 3, tablero_y + y * TAMANO_CELDA + 3))

    # Dibujar el texto de indicación
    fuente_indicacion = pygame.font.Font(None, 40)
    texto_indicacion = fuente_indicacion.render(" Encuentra palabras relacionadas con energías renovables ", True, LETRA_COLOR)
    pantalla_info_actual = pygame.display.Info()  # Define pantalla_info_actual

    ANCHO_VENTANA_PEQUENA = 800  # Define the value of ANCHO_VENTANA_PEQUENA

    texto_rect = texto_indicacion.get_rect()

    # Ajustar posición según el modo de ventana
    if ANCHO == pantalla_info_actual.current_w and ALTO == pantalla_info_actual.current_h:
        # Ventana maximizada
        texto_rect.topleft = ((ANCHO - texto_indicacion.get_width()) // 2, 10)
    elif ANCHO <= ANCHO_VENTANA_PEQUENA:
        # Ventana pequeña
        texto_rect.topleft = ((ANCHO - texto_indicacion.get_width()) // 2, ALTO - 50)

    ventana.blit(texto_indicacion, texto_rect)
    for y, fila in enumerate(MATRIZ_LETRAS):
        for x, letra in enumerate(fila):
            fuente = pygame.font.Font(None, 36)

            # Verificar si la celda está seleccionada y ajustar el color
            color = SELECCION_COLOR if MATRIZ_SELECCION[y][x] else LETRA_COLOR

            texto = fuente.render(letra, True, color)
            ventana.blit(texto, (tablero_x + x * TAMANO_CELDA + 3, tablero_y + y * TAMANO_CELDA + 3))

    # Dibujar el texto de indicación
    fuente_indicacion = pygame.font.Font(None, 40)
    texto_indicacion = fuente_indicacion.render(" Encuentra palabras relacionadas con energías renovables ", True, LETRA_COLOR)
    pantalla_info_actual = pygame.display.Info()  # Define pantalla_info_actual

    ANCHO_VENTANA_PEQUENA = 800  # Define the value of ANCHO_VENTANA_PEQUENA

    texto_rect = texto_indicacion.get_rect()

    # Ajustar posición según el modo de ventana
    if ANCHO == pantalla_info_actual.current_w and ALTO == pantalla_info_actual.current_h:
        # Ventana maximizada
        texto_rect.topleft = ((ANCHO - texto_indicacion.get_width()) // 2, 10)
    elif ANCHO <= ANCHO_VENTANA_PEQUENA:
        # Ventana pequeña
        texto_rect.topleft = ((ANCHO - texto_indicacion.get_width()) // 2, 10)
    else:
        # Ventana en el centro de la pantalla
        texto_rect.topleft = ((ANCHO - texto_indicacion.get_width()) // 2, 10)

    ventana.blit(texto_indicacion, texto_rect.topleft)

    # Mostrar la lista de palabras a encontrar hacia abajo
    fuente_lista_palabras = pygame.font.Font(None, 40)
    y_pos = 100  # Posición inicial en el eje Y

    for palabra in PALABRAS:
        texto_lista_palabras = fuente_lista_palabras.render(palabra, True, LETRA_COLOR)
        ventana.blit(texto_lista_palabras, (ANCHO - texto_lista_palabras.get_width() - 10, y_pos))
        y_pos += 30  # Ajusta el espacio vertical entre las palabras


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

    # Colores Palabras
    COLORES_PALABRAS = {
        "SOLAR": (255, 0, 0),  # Rojo
        "EOLICA": (255, 0, 0),  # Verde
        "BIOMASA": (255, 0, 0),  # Azul
        "HIDRAULICA": (255, 0, 0),  # Amarillo
        "GEOTERMICA": (255, 0, 0),  # Magenta
        "MAREMOTO": (255, 0, 0)  # Cian
    }

    # Dibujar la palabra actual
    fuente_palabra = pygame.font.Font(None, 30)
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
                   

    # Dibujar la barra de palabras encontradas
    fuente_barra = pygame.font.Font(None, 36)
    barra_texto = "Palabras encontradas: " + ", ".join(palabras_encontradas)
    texto_barra = fuente_barra.render(barra_texto, True, LETRA_COLOR)
    ventana.blit(texto_barra, (10, ALTO - 60))

    # Dibujar la cuadrícula en la matriz de letras
    for x in range(tablero_x, tablero_x + len(MATRIZ_LETRAS[0]) * TAMANO_CELDA + 1, TAMANO_CELDA):
        pygame.draw.line(ventana, LETRA_COLOR, (x, tablero_y), (x, tablero_y + len(MATRIZ_LETRAS) * TAMANO_CELDA))

    for y in range(tablero_y, tablero_y + len(MATRIZ_LETRAS) * TAMANO_CELDA + 1, TAMANO_CELDA):
        pygame.draw.line(ventana, LETRA_COLOR, (tablero_x, y), (tablero_x + len(MATRIZ_LETRAS[0]) * TAMANO_CELDA, y))

    
    # Mostrar mensaje "¡Ganaste!" si se encontraron todas las palabras
    if todas_encontradas:
        tiempo_terminado = pygame.time.get_ticks()
        juego_ganado = True

        # Mostrar mensaje "¡Ganaste!" si se encontraron todas las palabras
    if todas_encontradas:
        fuente_ganaste = pygame.font.Font(None, 80)
        texto_ganaste = fuente_ganaste.render("¡ Felicidades Acabas de Ganar!", True, (0, 255, 0))
        ventana.blit(texto_ganaste, (ANCHO // 2 - texto_ganaste.get_width() // 2, ALTO // 2 - texto_ganaste.get_height() // 2))

    # Mostrar mensaje "¡Perdiste!" si se acabó el tiempo
    if perdiste:
        fuente_perdiste = pygame.font.Font(None, 80)
        texto_perdiste = fuente_perdiste.render("¡ Perdiste intentalo otra vez !", True, (255, 0, 0))
        ventana.blit(texto_perdiste, (ANCHO // 2 - texto_perdiste.get_width() // 2, ALTO // 2 - texto_perdiste.get_height() // 2))

    # Actualizar la pantalla
    pygame.display.update()
    
    clock.tick(FPS)

    

# Finalizar Pygame
pygame.quit()