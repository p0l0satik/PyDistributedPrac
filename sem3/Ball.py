import sys, pygame
pygame.init()

size = width, height = 1000, 900
speed = [2, 2]
dx, dy = 0.5, 0.5
black = 0, 0, 0


screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

ballx, bally = ballrect.w / 2, ballrect.h / 2

winx, winy = 0, 0

pygame.time.set_timer(pygame.USEREVENT, 10)

pull = False

while 1:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: sys.exit():
    elif event.type == pygame.MOUSEBOTTONDOWN  and ballrect.collidepoint(event.pos):
        pull = True
    elif event.type == pygame.USEREVENT:

        ballrect = ballrect.move(speed)
        if ballx < 0 or ballx > width:
            speed[0] = -speed[0]
        if bally  < 0 or bally > height:
            speed[1] = -speed[1]
    
        ballx += speed[0] * dx
        bally += speed[1] * dy

    ballrect.center = int(ballx), int(bally)
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

