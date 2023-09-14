#Short Circuit
import os,sys
import pygame as pg #Avoid namespace flooding
import pygame

class Object:
    def __init__(self,rect):
        self.rect = pg.Rect(rect)
        self.click = False
        self.image = pg.Surface(self.rect.size).convert()
        self.image = pygame.image.load("./images/hori_block.png")
        self.collide_rect = self.rect
    def update(self,surface):
        if self.click:
            self.rect.center = pg.mouse.get_pos()
        surface.blit(self.image,self.rect)

def update_obj2(Surface):
    Surface.blit(obj2.image,obj2.rect)  
    obj2.alpha = 255

def update_obj3(Surface):
    Surface.blit(obj3.image,obj3.rect)
    obj3.alpha = 255

def main(Surface,obj,obj2,obj3):
    game_event_loop(obj,obj2,obj3)
    Surface.fill(0)
    obj.update(Surface)
    obj2.update(Surface)
    obj3.update(Surface)
    update_obj2(Surface)
    update_obj3(Surface)


def game_event_loop(obj,obj2, obj3):
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if obj.rect.collidepoint(event.pos):
                obj.click = True
            elif obj2.rect.collidepoint(event.pos):
                obj2.click = True
            elif obj3.rect.collidepoint(event.pos):
                obj3.click = True
        elif event.type == pg.MOUSEBUTTONUP:
            obj.click = False
            obj2.click = False
            obj3.click = False
        elif event.type == pg.QUIT:
            pg.quit(); sys.exit()

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((1000,600))
    MyClock = pg.time.Clock()
    obj = Object((0,0,100,100))
    obj.rect.center = Screen.get_rect().center
    obj2 = Object((100,100,100,100))
    obj3 = Object((200,200,100,100))
    while 1:
        main(Screen,obj,obj2,obj3)
        pg.display.update()
        MyClock.tick(60)

