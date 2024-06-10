import pygame, sys, cl, math
pygame.init()


info = pygame.display.Info()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello World!')

floorS = 400
wallS = 25

wall = cl.Thing(math.inf, pygame.math.Vector2(0,0), pygame.math.Vector2(25, 25), 50, 450, (255,255,255))
floor = cl.Thing(math.inf, pygame.math.Vector2(0,0), pygame.math.Vector2(25, 425), 450, 50, (255,255,255))

obj1 = cl.Thing(10, pygame.math.Vector2(0,0), pygame.math.Vector2(100, 390), 25, 25, (255,0,255))
obj2 = cl.Thing(100, pygame.math.Vector2(-50,0), pygame.math.Vector2(300, 390), 25, 25, (255,0,255))


while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    win.fill((0,0,0))
    for x in cl.objects:
        x.move()
    pygame.display.update()
