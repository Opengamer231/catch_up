from pygame import *

window = display.set_mode((750,550))
display.set_caption('Догонялки')

background = transform.scale(
    image.load("background.png"),
    (750,550)
)

sprite_1 = transform.scale(
    image.load("sprite1.png"),
    (100,100)
)

sprite_2 = transform.scale(
    image.load("sprite2.png"),
    (100,100)
)

x1 = 100
y1 = 225
x2 = 600
y2 = 225

clock = time.Clock()
FPS = 60

speed_1 = 10
speed_2 = 15

game = True
while game:
    clock.tick(FPS)

    window.blit(background,(0,0))
    window.blit(sprite_1,(x1,y1))
    window.blit(sprite_2,(x2,y2))

    keys_preesed = key.get_pressed()

    if keys_preesed[K_w] and y1 > 5:
        y1 -= speed_1
    if keys_preesed[K_s] and y1 < 445:
        y1 += speed_1
    if keys_preesed[K_a] and x1 > 5:
        x1 -= speed_1
    if keys_preesed[K_d] and x1 < 645:
        x1 += speed_1

    if keys_preesed[K_UP] and y2 > 5:
        y2 -= speed_2
    if keys_preesed[K_DOWN] and y2 < 445:
        y2 += speed_2
    if keys_preesed[K_LEFT] and x2 > 5:
        x2 -= speed_2
    if keys_preesed[K_RIGHT] and x2 < 645:
        x2 += speed_2

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()

    
