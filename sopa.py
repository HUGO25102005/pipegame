import sys
import random
import pygame
import matriz
# Constantes
ANCHO = 800
ALTO = 600

# Definimos la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Definimos los colores
COLOR_FONDO = (0, 0, 0)
COLOR_TEXTO = (255, 255, 255)

# Cargamos la imagen de la cuadrícula
imagen_cuadricula = pygame.image.load("cuadricula.png")

# Creamos la lista de palabras
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lista_palabras = ["gato", "perro", "casa", "árbol", "coche", "luna", "sol", "mar", "cielo"]

N = 5
class Objeto:
    def __init__(self, palabra=None, encontrada=False):
        self.palabra = palabra
        self.encontrada = encontrada
# Creamos la matriz
matriz = [[Objeto() for i in range(N)] for j in range(N)]



# Colocamos las palabras en la matriz
for palabra in lista_palabras:
    # Escogemos una dirección aleatoria
    direccion = random.choice(["izquierda_a_derecha", "derecha_a_izquierda", "arriba_abajo", "abajo_arriba", "diagonal_de_arriba_abajo", "diagonal_de_abajo_arriba"])
    # Colocamos la palabra en la matriz
    matriz = direccion(matriz, palabra)

# Bucle principal
while True:
    # Actualizamos la pantalla
    pantalla.fill(COLOR_FONDO)
    pantalla.blit(imagen_cuadricula, (0, 0))

    # Dibujamos las palabras
    for i in range(N):
        for j in range(N):
            # Si la celda no está vacía, dibujamos la palabra
            if matriz[i][j].palabra != "":
                pygame.draw.rect(pantalla, COLOR_TEXTO, (i * 20, j * 20, 20, 20))
                pygame.draw.rect(pantalla, COLOR_TEXTO, (i * 20, j * 20, 20, 20), 1)
                pygame.display.set_caption(matriz[i][j].palabra)

    # Eventos del mouse
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # Obtenemos la posición del mouse
            posicion_mouse = pygame.mouse.get_pos()

            # Buscamos la celda que contiene el mouse
            i, j = posicion_mouse // 20

            # Comprobamos si la celda contiene una palabra
            if matriz[i][j].palabra != " ":
                # Marcamos la celda como encontrada
                matriz[i][j].encontrada = True

                # Actualizamos el progreso
                progreso = len(list(filter(lambda x: x.encontrada, matriz))) / len(lista_palabras)

                # Actualizamos la tabla
                tabla = [[matriz[i][j].palabra if matriz[i][j].encontrada else " " for j in range(N)] for i in range(N)]

    # Actualizamos la pantalla
    pygame.display.update()

    # Procesamos los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
