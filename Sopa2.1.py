import pygame
import random

# Inicializar Pygame
pygame.init()

en = False

# Leer el valor desde el archivo la próxima vez que ejecutes el programa
with open('./__pycache__/en.txt', 'r') as archivo:
   en = bool(int(archivo.read()))

volume = 0.5  # Initial volume
min_volume = 0.0
max_volume = 1.0

# Cargar el archivo de audio
pygame.mixer.music.load("assets/noworries.ogg")

# Reproducir el audio en bucle
pygame.mixer.music.play(-1)  # El valor -1 indica que el audio se reproducirá en bucle infinito

# Definir el tamaño de la ventana y el tablero
info = pygame.display.Info()
ANCHO = info.current_w
ALTO = info.current_h
TAMANO_CELDA = 40
random.seed(0)

# Cargar la imagen de fondo
FONDO_IMAGEN = pygame.image.load("assets/energia.solar.png")  # Reemplaza "ruta_de_la_imagen.jpg" con la ruta de tu imagen
FONDO_IMAGEN = pygame.transform.scale(FONDO_IMAGEN, (ANCHO, ALTO))

LETRA_COLOR = (0, 0, 0)
PALABRAS = ["LUZ", 
            "EOLICA",
            "BATERIA", 
            "NUCLEO", 
            "TERMICA", 
            "MAREMOTO"]


# Matriz de letras (15x15)
# Matriz de letras (15x15)
MATRIZ_LETRAS = [
    ["L", "U", "Z", "A", "R", "E", "O", "L", "I", "C", "A", "I", "C", "A", "E"],
    ["H", "O", "C", "E", "C", "A", "A", "I", "D", "R", "O", "G", "E", "O", "N"],
    ["B", "M", "G", "E", "O", "T", "E", "R", "M", "I", "C", "A", "O", "L", "U"],
    ["D", "A", "A", "S", "O", "R", "O", "C", "G", "L", "B", "R", "E", "S", "C"],
    ["R", "R", "A", "I", "H", "I", "D", "R", "E", "U", "A", "I", "C", "A", "L"],
    ["O", "E", "T", "O", "M", "A", "S", "A", "O", "R", "T", "S", "L", "A", "E"],
    ["G", "M", "N", "E", "R", "A", "D", "O", "T", "E", "E", "L", "C", "O", "O"],
    ["E", "O", "I", "O", "M", "A", "A", "S", "E", "O", "R", "A", "S", "A", "E"],
    ["O", "T", "C", "A", "R", "E", "A", "T", "R", "N", "I", "N", "M", "T", "A"],
    ["I", "O", "E", "E", "C", "E", "E", "A", "M", "A", "A", "R", "I", "E", "A"],
    ["C", "A", "R", "B", "I", "O", "M", "A", "S", "A", "N", "A", "L", "A", "C"],
    ["H", "R", "N", "E", "E", "N", "A", "L", "C", "N", "M", "T", "L", "E", "G"],
    ["D", "S", "O", "L", "A", "R", "T", "A", "A", "S", "F", "S", "A", "L", "N"],
    ["R", "X", "H", "I", "D", "N", "U", "C", "L", "E", "O", "R", "R", "O", "A"],
    ["L", "B", "A", "T", "E", "R", "I", "A", "R", "M", "I", "C", "A", "E", "E"]
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

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)
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

# Load the "pause.png" image
pause_button_image = pygame.image.load("assets/pause_button1.png")
pause_button_image = pygame.transform.scale(pause_button_image, (150, 150))  # Adjust the size as needed

# Create a button rectangle in the top left corner
pause_button_rect = pause_button_image.get_rect(topleft=(10, 10))

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
tiempo_maximo = 600000 # 10 minutos (en milisegundos)

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

# Variable para verificar si todas las palabras se han encontrado
todas_encontradas = False

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

# Inicializa la variable juego_ganado al principio del bucle principal
juego_ganado = False  

def get_win_text():
    if en:
        return "You Won!"
    if not en:
        return "¡Has ganado!"

def get_back_text():
    if en:
        return "Back"
    if not en:
        return "Atras"

def get_reset_text():
    if en:
        return "Reset"
    if not en:
        return "Reiniciar"

def get_continue_text():
    if en: 
        return "CONTINUE"
    else:
        return "CONTINUAR"

def get_restart_text():
    if en: 
        return "RESTART"
    else:
        return "REINICIAR"

def get_options_text():
    if en: 
        return "OPTIONS"
    else:
        return "OPCIONES"

def get_quit_text():
    if en: 
        return "QUIT"
    else:
        return "SALIR"

def get_back1_text():
    if en:
        return "BACK"
    else:
        return "ATRAS"

def options_game():
    global volume, en

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(FONDO_IMAGEN, (0, 0))
        BG2 = pygame.image.load("assets/background_2.png")
        BG2 = pygame.transform.scale(BG2, (SCREEN_WIDTH, SCREEN_HEIGHT))
        SCREEN.blit(BG2, (0, 0)) # Dibuja la imagen de fondo en la pantalla

        # Carga la imagen del volumen al comienzo de la función
        volumen_image = pygame.image.load("./assets/volumen_menu.png")

        # Define bar position and dimensions
        bar_x = SCREEN_WIDTH // 4  # Ajustar la posición de la barra según la resolución
        bar_y = SCREEN_HEIGHT // 4
        bar_width = SCREEN_WIDTH // 2
        bar_height = 20

        OPTIONS_ID = Button(image=pygame.image.load("assets/options.png"), pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.5),
                            text_input=get_language_text(), font=get_font(75), base_color="Black", hovering_color="")

        OPTIONS_ID.update(SCREEN)

        # Dibuja la imagen del volumen al lado izquierdo de la barra
        SCREEN.blit(volumen_image, (bar_x - 100, bar_y - 40))  # Ajusta las coordenadas

        OPTIONS_EN = Button(image=pygame.image.load(get_language()), pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.8),
                            text_input="", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_EN.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_EN.update(SCREEN)

        # Draw the volume bar
        bar_color = (255, 255, 255)  # White color
        pygame.draw.rect(SCREEN, bar_color, (bar_x, bar_y, bar_width, bar_height))

        # Draw a volume indicator on the bar
        indicator_pos = bar_x + int(volume * bar_width)
        indicator_color = (0, 255, 0)  # Green color
        pygame.draw.rect(SCREEN, indicator_color, (indicator_pos, bar_y - 5, 10, 30))

        OPTIONS_BACK = Button(image=pygame.image.load("assets/play.png"), pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.2),
                              text_input=get_back1_text(), font=get_font(75), base_color="Black", hovering_color="Cyan")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # Get mouse position
                if bar_x <= mouse_pos[0] <= bar_x + bar_width and bar_y <= mouse_pos[1] <= bar_y + bar_height:
                    volume = calculate_volume(mouse_pos, bar_x, bar_y, bar_width)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_EN.checkForInput(OPTIONS_MOUSE_POS):
                    if en:
                        en = False
                    else:
                        en = True

                    # Guardar el valor en un archivo
                    with open('./__pycache__/en.txt', 'w') as archivo:
                        archivo.write(str(int(en)))

        pygame.display.update()

def pause():
    while True:
        ventana.blit(FONDO_IMAGEN, (0, 0))

        BG2 = pygame.image.load("assets/background_2.png")
        BG2 = pygame.transform.scale(BG2, (SCREEN_WIDTH, SCREEN_HEIGHT))
        ventana.blit(BG2, (0, 0)) # Dibuja la imagen de fondo en la pantalla

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        # Crea botones para "JUGAR", "OPCIONES" y "SALIR" en el menú principal
        CONTINUE_BUTTON = Button(image=pygame.image.load("assets/options.png"), pos=get_scaled_position(640, 250), 
                            text_input=get_continue_text(), font=get_scaled_font(75), base_color="White", hovering_color="Cyan")
        RESTART_BUTTON = Button(image=pygame.image.load("assets/options.png"), pos=get_scaled_position(640, 350), 
                            text_input=get_restart_text(), font=get_scaled_font(75), base_color="White", hovering_color="Cyan")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/options.png"), pos=get_scaled_position(640, 450), 
                            text_input=get_options_text(), font=get_scaled_font(75), base_color="White", hovering_color="Cyan")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/quit.png"), pos=get_scaled_position(640, 550), 
                           text_input=get_quit_text(), font=get_scaled_font(75), base_color="White", hovering_color="Cyan")
        
        # Actualiza y muestra los botones en el menú principal
        for button in [CONTINUE_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, RESTART_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTINUE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if tiempo_restante > 0:
                        return
                    else:
                        exec(open("./Sopa2.1.py", "r").read(), globals()) 
                        pygame.quit()
                        sys.exit()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options_game()
                if RESTART_BUTTON.checkForInput(MENU_MOUSE_POS):
                    exec(open("./Sopa2.1.py", "r").read(), globals()) 
                    pygame.quit()
                    sys.exit()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    exec(open("./main.py", "r").read(), globals()) 
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


# Bucle principal del juego
while not terminado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True
        elif evento.type == pygame.VIDEORESIZE:
            ANCHO, ALTO = evento.w, evento.h
            ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            x, y = evento.pos
            if pause_button_rect.collidepoint(x, y):
                pause()
            
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

            # Verificar si todas las palabras se han encontrado
            todas_encontradas = all(palabra.upper() not in PALABRAS for palabra in PALABRAS)
            if todas_encontradas and not juego_terminado:
                tiempo_terminado = pygame.time.get_ticks()
                juego_ganado = True
                juego_terminado = True  # Asegúrate de que el juego esté marcado como terminado

            # Verificar si el tiempo ha llegado a cero
            if tiempo_restante == 0 and not juego_terminado:
                juego_terminado = True
                perdiste = True  # Se establece perdiste como True cuando el tiempo llega a cero   

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
                    if len(palabras_encontradas) >= len(PALABRAS):
                        todas_encontradas = True
                        tiempo_terminado = pygame.time.get_ticks()
                        juego_ganado = True

        
        
        # # Verificar si todas las palabras se han encontrado
        if todas_encontradas and not juego_terminado:
            tiempo_terminado = pygame.time.get_ticks()
            juego_ganado = True
            juego_terminado = True  # Asegúrate de que el juego esté marcado como terminado


        # Verificar si el tiempo ha llegado a cero
        if tiempo_restante == 0 and not juego_terminado:
            juego_terminado = True
            perdiste = True  # Se establece perdiste como True cuando el tiempo llega a cero

     

      # Ajuste de posición para las palabras encontradas
            y_pos_palabras = ALTO - 30

    
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
    tablero_y = (ALTO - len(MATRIZ_LETRAS) * TAMANO_CELDA) // 2
    SELECCION_COLOR = (255, 0, 0)  # Define el SELECCION_COLOR

    for y, fila in enumerate(MATRIZ_LETRAS):
        for x, letra in enumerate(fila):
            # Dibujar el borde blanco alrededor de la letra
            fuente = pygame.font.Font(None, 48)
            color = SELECCION_COLOR if MATRIZ_SELECCION[y][x] else LETRA_COLOR
            fuente_borde = pygame.font.Font(None, 55)
            texto_borde = fuente_borde.render(letra, True, (255, 255, 255))
            for i in range(-2, 3):
                for j in range(-2, 3):
                    ventana.blit(texto_borde, (tablero_x + x * TAMANO_CELDA + 3, tablero_y + y * TAMANO_CELDA + 3))
                    texto = fuente.render(letra, True, color)
                    ventana.blit(texto, (tablero_x + x * TAMANO_CELDA + 4.5, tablero_y + y * TAMANO_CELDA + 4.5))


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

    ventana.blit(pause_button_image, pause_button_rect.topleft)

    # Mostrar un mensaje de victoria si todas las palabras se han encontrado
    if todas_encontradas:
        BG2 = pygame.image.load("assets/background_2.png")
        BG2 = pygame.transform.scale(BG2, (SCREEN_WIDTH, SCREEN_HEIGHT))
        SCREEN.blit(BG2, (0, 0))

        three_stars = False
        two_stars = False
        one_star = False

         # Mostrar un mensaje de victoria
        font = pygame.font.Font(None, 120)
        text = font.render(get_win_text(), True, (255, 0, 0))
        text_rect = text.get_rect(center=(ventana.get_width() // 2, ventana.get_height() // 5))
        ventana.blit(text, text_rect)

        # Dibujar estrella central
        frs_star_b = pygame.image.load("assets/starb.png")
        frs_star_b = pygame.transform.scale(frs_star_b, (200,200))
        frs_star_b_rect = frs_star_b.get_rect(center=(ventana.get_width() // 2, ventana.get_height() // 3))
        ventana.blit(frs_star_b, frs_star_b_rect)
        
        # Posicionar segunda estrella a la izquierda de la primera
        snd_star_b_rect = pygame.Rect(frs_star_b_rect.left - frs_star_b_rect.width, frs_star_b_rect.top + 20, 100, 40)
        snd_star_b = pygame.image.load("assets/starb.png")
        snd_star_b = pygame.transform.scale(snd_star_b, (200,200))
        ventana.blit(snd_star_b, snd_star_b_rect)

        # Posicionar segunda estrella a la izquierda de la primera
        trd_star_b_rect = pygame.Rect(frs_star_b_rect.right - frs_star_b_rect.width + 200, frs_star_b_rect.top + 20, 100, 40)
        trd_star_b = pygame.image.load("assets/starb.png")
        trd_star_b = pygame.transform.scale(trd_star_b, (200,200))
        ventana.blit(trd_star_b, trd_star_b_rect)


        if tiempo_restante >= 420000:
            three_stars = True
         
        if tiempo_restante >= 210000 and tiempo_restante < 420000:
            two_stars = True
    
        if tiempo_restante < 210000:
            one_star = True
        
        if three_stars:
            # Dibujar estrella central
            frs_star = pygame.image.load("assets/star.png")
            frs_star = pygame.transform.scale(frs_star, (200,200))
            frs_star_rect = frs_star.get_rect(center=(ventana.get_width() // 2, ventana.get_height() // 3))
            ventana.blit(frs_star, frs_star_rect)
        
            # Posicionar segunda estrella a la izquierda de la primera
            snd_star_rect = pygame.Rect(frs_star_rect.left - frs_star_rect.width, frs_star_rect.top + 20, 100, 40)
            snd_star = pygame.image.load("assets/star.png")
            snd_star = pygame.transform.scale(snd_star, (200,200))
            ventana.blit(snd_star, snd_star_rect)

            # Posicionar segunda estrella a la izquierda de la primera
            trd_star_rect = pygame.Rect(frs_star_rect.right - frs_star_rect.width + 200, frs_star_rect.top + 20, 100, 40)
            trd_star = pygame.image.load("assets/star.png")
            trd_star = pygame.transform.scale(trd_star, (200,200))
            ventana.blit(trd_star, trd_star_rect)

        if two_stars:
            # Dibujar estrella central
            frs_star = pygame.image.load("assets/star.png")
            frs_star = pygame.transform.scale(frs_star, (200,200))
            frs_star_rect = frs_star.get_rect(center=(ventana.get_width() // 2, ventana.get_height() // 3))
            ventana.blit(frs_star, frs_star_rect)
        
            # Posicionar segunda estrella a la izquierda de la primera
            snd_star_rect = pygame.Rect(frs_star_rect.left - frs_star_rect.width, frs_star_rect.top + 20, 100, 40)
            snd_star = pygame.image.load("assets/star.png")
            snd_star = pygame.transform.scale(snd_star, (200,200))
            ventana.blit(snd_star, snd_star_rect)

        if one_star:
            # Dibujar estrella central
            frs_star = pygame.image.load("assets/star.png")
            frs_star = pygame.transform.scale(frs_star, (200,200))
            frs_star_rect = frs_star.get_rect(center=(ventana.get_width() // 2, ventana.get_height() // 3))
            ventana.blit(frs_star, frs_star_rect)
        
        # Dibujar un botón de retorno
        back_button_text = font.render(get_back_text(), True, (255, 255, 255))
        back_button_text_rect = back_button_text.get_rect(center=(ventana.get_width() // 2, text_rect.bottom + 450))
        back_button_rect = back_button_text_rect.inflate(10, 10)  
        ventana.blit(back_button_text, back_button_text_rect)
        
        # Manejar eventos de clic en el botón de retorno
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and back_button_rect.collidepoint(event.pos):
                exec(open("./main.py", "r").read(), globals()) 
                pygame.display.update()
                pygame.quit()
                sys.exit()
        

    # Mostrar mensaje "¡Perdiste!" si se acabó el tiempo
    if tiempo_restante <= 0 and not todas_encontradas:
        BG2 = pygame.image.load("assets/background_2.png")
        BG2 = pygame.transform.scale(BG2, (SCREEN_WIDTH, SCREEN_HEIGHT))
        SCREEN.blit(BG2, (0, 0))

        three_stars = False
        two_stars = False
        one_star = False

        # Mostrar "Game Over"
        font = pygame.font.Font(None, 120)
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        game_over_text_rect = game_over_text.get_rect(center=(ventana.get_width() // 2, ventana.get_height() // 5))
        ventana.blit(game_over_text, game_over_text_rect)

        # Dibujar estrella central
        frs_star_b = pygame.image.load("assets/starb.png")
        frs_star_b = pygame.transform.scale(frs_star_b, (200,200))
        frs_star_b_rect = frs_star_b.get_rect(center=(ventana.get_width() // 2, ventana.get_height() // 3))
        ventana.blit(frs_star_b, frs_star_b_rect)
        
        # Posicionar segunda estrella a la izquierda de la primera
        snd_star_b_rect = pygame.Rect(frs_star_b_rect.left - frs_star_b_rect.width, frs_star_b_rect.top + 20, 100, 40)
        snd_star_b = pygame.image.load("assets/starb.png")
        snd_star_b = pygame.transform.scale(snd_star_b, (200,200))
        ventana.blit(snd_star_b, snd_star_b_rect)

        # Posicionar segunda estrella a la izquierda de la primera
        trd_star_b_rect = pygame.Rect(frs_star_b_rect.right - frs_star_b_rect.width + 200, frs_star_b_rect.top + 20, 100, 40)
        trd_star_b = pygame.image.load("assets/starb.png")
        trd_star_b = pygame.transform.scale(trd_star_b, (200,200))
        ventana.blit(trd_star_b, trd_star_b_rect)

        # Dibujar un botón "Reset"
        reset_button_text = font.render(get_reset_text(), True, (255, 255, 255))
        reset_button_text_rect = reset_button_text.get_rect(center=(ventana.get_width() // 2, game_over_text_rect.bottom + 450))
        reset_button_rect = reset_button_text_rect.inflate(10, 10)
        ventana.blit(reset_button_text, reset_button_text_rect)

        # Dibujar un botón "Back"
        back_button_text = font.render(get_back_text(), True, (255, 255, 255))
        back_button_text_rect = back_button_text.get_rect(center=(ventana.get_width() // 2, game_over_text_rect.bottom + 550))
        back_button_rect = back_button_text_rect.inflate(10, 10)  
        ventana.blit(back_button_text, back_button_text_rect)

            
        # Manejar eventos de clic en el botón de retorno
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and back_button_rect.collidepoint(event.pos):
                # Código para volver al menú principal
                exec(open("./main.py", "r").read(), globals()) 
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and reset_button_rect.collidepoint(event.pos):
                exec(open("./Sopa2.1.py", "r").read(), globals()) 
                pygame.quit()
                sys.exit()

    

    # Actualizar la pantalla
    pygame.display.update()
    
    clock.tick(FPS)

# Finalizar Pygame
pygame.quit()


