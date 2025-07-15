import pygame
pygame.init()

screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("Cat_Runner")
clock=pygame.time.Clock()

plain_surface = pygame.Surface((100,200))
plain_surface.fill('Red')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()




    screen.blit(plain_surface,(0,0))
    pygame.display.update()
    clock.tick(60)  
