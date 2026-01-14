import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(
            x = SCREEN_WIDTH / 2,
            y = SCREEN_HEIGHT / 2,
        )
    

    while 1==1:

        log_state() 
        for event in pygame.event.get():
            pass

        screen.fill("black")

      

        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
       


        pygame.display.flip()

        
    



        delta = pygame.time.Clock().tick(60)
        dt = delta / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
if __name__ == "__main__":
    main()
