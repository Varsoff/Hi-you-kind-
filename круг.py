
import pygame
pygame.init()
a=1920
b=1080
d=50
win = pygame.display.set_mode((a, b))
x = a / 2
y = b / 2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    k = pygame.key.get_pressed()
    if k[pygame.K_LEFT]:
        x -= 6
    if k[pygame.K_RIGHT]:
        x += 6
    if k[pygame.K_UP]:
        y -= 6
    if k[pygame.K_DOWN]:
        y += 6
    if k[pygame.K_SPACE]:
        y -= 12
    if k[pygame.K_TAB]:
        if x < a / 2:
            x+=3
        if x > a / 2:
            x-=3
        if y < b / 2:
            y+=3
        if y > b / 2:
            y-=3
    if x > a:
        x = 0
    if y > b:
        y = 0
    if y < 0:
        y = 1080
    if x < 0:
        x = 1920
    kl =(250, 250, 250)
    win.fill(kl)
    k=int(a)
    pygame.draw.circle(win,(250, 250, 0), (x,y),d)
      #  pygame.draw.rect(win,(0, 0, 0), (300,100,c,c))
#  pygame.draw.polygon(win,(0,0,0),[(0,100),(100,50),(100,150)],False)
   # pygame.draw.line(win, (255, 255, 255),(0,0),(a,), 10)
    #pygame.draw.line(win, (255, 255, 255),(a,0),(0  ,b), 10)
    #pygame.draw.line(win, (255, 255, 255),(a,0),(0  ,b), 10)
    pygame.display.update()
    pygame.time.delay(10)
