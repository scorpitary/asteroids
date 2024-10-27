import pygame
from constants import *
from circleshape import *
from player import *
clock = pygame.time.Clock()
dt = 0

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000
        
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()