import pygame
from random import randint, random



START_circle = 20
start_Square= 30
win_w = 300
win_h = 200
VEL = 1

win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Petri")
win.fill((255, 255, 255))
clock = pygame.time.Clock()






# -------------------------------------------------------//////////  MICROBE SIMPLE ///////////////---------------------
class Microbe:
    def __init__(self, x, y, xvel, yvel):
        self.x = x
        self.y = y
        self.XVEL = xvel
        self.YVEL = yvel
        pass

    def draw(self):
        pygame.draw.circle(win, (0, 150, 200), (round(self.x), round(self.y)), 10)

    def move(self):
        if self.x < 50 or self.x > win_w-20:
            self.XVEL = -self.XVEL
        if self.y < 50 or self.y > win_h-20:
            self.YVEL = -self.YVEL

        self.x += self.XVEL
        self.y += self.YVEL


microbes = []

for _ in range(START_circle):
    xvel = randint(0, VEL*100*2)/100 - VEL
    ysign = randint(0, 1)
    yvel = (VEL**2 - xvel**2)**0.5

    if ysign == 0:
        yvel *= -1

    xpos = randint(70, win_w-30)
    ypos = randint(70, win_h-30)
    microbes.append(Microbe(xpos, ypos, xvel, yvel))

    for microbe in microbes:
        microbe.draw()


pygame.display.update()


# -------------------------------------------------------------////////////////// MICROBE mangeur ////////////////////////////-------------------------
# creation des microbes mangeure
class Destructor:
    def __init__(self, x, y, xvel, yvel):
        self.x = x
        self.y = y
        self.XVEL = xvel
        self.YVEL = yvel
        pass

    def draw(self):
        pygame.draw.rect(win, (255, 0, 0), (round(self.x), round(self.y) , 10, 10))

    def move(self, tabMicrobes):
        if self.x < 50 or self.x > win_w-20:
            self.XVEL = -self.XVEL
        if self.y < 50 or self.y > win_h-20:
            self.YVEL = -self.YVEL

        self.x += self.XVEL
        self.y += self.YVEL
        
        for microbe in reversed(tabMicrobes):
            if round(self.x) == round(microbe.x) and round(self.y) == round(microbe.y):
                print("remove")
                # newNbeVirus =  START_circle - 1
                tabMicrobes.remove(microbe)
                # print("il reste ", newNbeVirus)

destructors = []

for _ in range(start_Square):
    xvel = randint(0, VEL*100*2)/100 - VEL
    ysign = randint(0, 1)
    yvel = (VEL**2 - xvel**2)**0.5

    if ysign == 0:
        yvel *= -1

    xpos = randint(70, win_w-30)
    ypos = randint(70, win_h-30)
    destructors.append(Destructor(xpos, ypos, xvel, yvel))

    for destructor in destructors:
        destructor.draw()

pygame.display.update()
clock.tick(30)





petri_run = True

while petri_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            petri_run = False
            break

    win.fill((255, 255, 255))

    for elt in microbes:
        elt.draw()
        elt.move()


    for elt in destructors:
        elt.draw()
        elt.move(microbes)

    

    pygame.display.update()
    clock.tick(24)
