#Short Circuit
import os,sys
import pygame
from pygame.locals import *

NUM_CELLS = 8
CELL_SIZE = 68

class Object:
    def __init__(self, rect, cell_pos):
        self.rect = pygame.Rect(rect)
        self.cell_pos = cell_pos
        self.click = False
        self.image = pygame.Surface(self.rect.size).convert()
        self.image = pygame.image.load("./assets/hori_block.png")
        self.collide_rect = self.rect

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image,self.rect)

def update_obj2(Surface):
    Surface.blit(obj2.image,obj2.rect)  
    obj2.alpha = 255

def update_obj3(Surface):
    Surface.blit(obj3.image,obj3.rect)
    obj3.alpha = 255

def main(Surface,obj,obj2,obj3):
    game_event_loop(obj,obj2,obj3)
    Surface.fill((255, 255, 255))
    for i in range(NUM_CELLS + 1):
        pygame.draw.line(Screen, (0, 0, 0), (0, i * CELL_SIZE), (NUM_CELLS * CELL_SIZE, i * CELL_SIZE))
        pygame.draw.line(Screen, (0, 0, 0), (i * CELL_SIZE, 0), (i * CELL_SIZE, NUM_CELLS * CELL_SIZE))
    obj.update(Surface)
    obj2.update(Surface)
    obj3.update(Surface)
    update_obj2(Surface)
    update_obj3(Surface)

    if obj.cell_pos == (0, 0):  
        font = pygame.font.Font(None, 36)
        text = font.render("You Won", True, (255, 0, 0))
        Surface.blit(text, (10, 10))

def game_event_loop(obj,obj2, obj3):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if obj.rect.collidepoint(event.pos):
                obj.click = True
            elif obj2.rect.collidepoint(event.pos):
                obj2.click = True
            elif obj3.rect.collidepoint(event.pos):
                obj3.click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            obj.click = False
            obj2.click = False
            obj3.click = False
        elif event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    Screen = pygame.display.set_mode((NUM_CELLS * CELL_SIZE, NUM_CELLS * CELL_SIZE))
    MyClock = pygame.time.Clock()
    obj = Object((CELL_SIZE * 0, CELL_SIZE * 0, CELL_SIZE, CELL_SIZE), (0, 0))  
    obj2 = Object((CELL_SIZE * 2, CELL_SIZE * 2, CELL_SIZE, CELL_SIZE), (2, 2))
    obj3 = Object((CELL_SIZE * 4, CELL_SIZE * 4, CELL_SIZE, CELL_SIZE), (4, 4)) 
    obj2.image = pygame.image.load("./assets/vert_block.png")
    obj3.image = pygame.image.load("./assets/cross_block.png")

    while 1:
        main(Screen,obj,obj2,obj3)
        pygame.display.update()
        MyClock.tick(60)

