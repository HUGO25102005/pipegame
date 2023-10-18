import pygame

# Constantes
ANCHO = 800
ALTO = 600

# Definimos la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Definimos los colores
COLOR_FONDO = (0, 0, 0)
COLOR_TEXTO = (255, 255, 255)

# Cargamos la imagen de la cuadrícula
imagen_cuadricula = pygame.image.load("assets/cuadricula.png")

# Creamos la lista de palabras
palabras = ["gato", "perro", "casa", "árbol", "coche", "luna", "sol", "mar", "cielo"]

# Creamos la lista de posiciones de las palabras
posiciones = []
for palabra in palabras:
    # Generamos una posición aleatoria para la palabra
    posicion_inicial = (random.randint(0, ANCHO - len(palabra)), random.randint(0, ALTO - len(palabra)))
    # Añadimos la posición a la lista
    posiciones.append(posicion_inicial)

# Bucle principal
while True:
    # Actualizamos la pantalla
    pantalla.fill(COLOR_FONDO)
    pantalla.blit(imagen_cuadricula, (0, 0))

    # Dibujamos las palabras
    for posicion, palabra in enumerate(palabras):
        pygame.draw.rect(pantalla, COLOR_TEXTO, (posiciones[posicion][0], posiciones[posicion][1], len(palabra), len(palabra)))
        pygame.display.set_caption(palabra)

    # Actualizamos la pantalla
    pygame.display.update()

    # Procesamos los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
