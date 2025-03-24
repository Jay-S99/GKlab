import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Wariant 4")


BIALY = (255, 255, 255)
CZERWONY = (255, 0, 0)

def rysuj_Z(okno):
    # Górna belka Z
    pygame.draw.rect(okno, CZERWONY, (150, 150, 300, 50))
    # Dolna belka Z
    pygame.draw.rect(okno, CZERWONY, (150, 400, 300, 50))
    # Przekątna Z
    pygame.draw.polygon(okno, CZERWONY, [(150, 400), (450, 150), (450, 200), (150, 450)])

run = True
while run:
    win.fill(BIALY)  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    rysuj_Z(win)  
    pygame.display.update()
    
pygame.quit()
