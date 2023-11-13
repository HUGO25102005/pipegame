  from typing import Self
if 0 <= y1 < len(acomodo) and 0 <= x1 < len(acomodo[y1]):

if x1 is None and y1 is None:

                x1 = x
                y1 = y
                acomodo[y1][x1].mostrar = True
                pygame.mixer.Sound.play(sonido_voltear)   
            else:
                x2 = x
                y2 = y
                acomodo[y2][x2].mostrar = True
                cuadro1 = acomodo[y1][x1]
                cuadro2 = acomodo[y2][x2]