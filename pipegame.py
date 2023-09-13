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
    def update(self,surface):
        if self.click:
            self.rect.center = pg.mouse.get_pos()
        surface.blit(self.image,self.rect)

def update_obj2(Surface):
    Surface.blit(obj2.image,obj2.rect)  
    obj2.alpha = 255

def main(Surface,obj):
    game_event_loop(obj)
    Surface.fill(0)
    obj.update(Surface)
    obj2.update(Surface)
    update_obj2(Surface)


def game_event_loop(obj):
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if obj.rect.collidepoint(event.pos):
                obj.click = True
            elif obj2.rect.collidepoint(event.pos):
                obj2.click = True
        elif event.type == pg.MOUSEBUTTONUP:
            obj.click = False
            obj2.click = False
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
    while 1:
        main(Screen,obj)
        pg.display.update()
        MyClock.tick(60)

