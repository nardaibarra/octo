import pygame
import sys
from entities import PhysicsEntity
from tilemap import Tilemap
from utils import load_image, load_images
from clouds import Clouds
from sea import Sea
from rod import Rod


class Game:
    W = 640 #320 
    H = 480 #240

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("octo")
        self.screen = pygame.display.set_mode((self.W,self.H))
        self.display = pygame.Surface((self.W/2, self.H/2))
        self.clock = pygame.time.Clock()
        self.movement = [False, False]

        self.assets = {
            'sand': load_images('tiles/sand'),
            'player': load_image('player.png'),
            'background': load_image('background.png'),
            'clouds': load_images('clouds'),
            'sea' : load_image('sea.png')
        }
        self.clouds = Clouds(self.assets['clouds'], count=9)
        self.sea = Sea((self.W/2, self.H/2),self.assets['sea'])
        self.player = PhysicsEntity(self, 'player', (50,50), (14,14))
        self.tilemap = Tilemap(self, tile_size=16)
        self.scroll = [0,0]
        self.rod = Rod(self,(100,120), 80, 5)
        self.rod1 = Rod(self,(200,120), 80, 5)
        

    def run(self) -> None:
        while True:

            self.display.blit(self.assets['background'], (0,0))
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 10 - self.scroll[0])
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 1.1 - self.scroll[1])

            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.sea.render(self.display,offset=render_scroll)
            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll)
            self.tilemap.render(self.display, offset=render_scroll)
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)
            self.rod.update()
            self.rod.draw(self.display, offset=self.scroll)
            self.rod1.update()
            self.rod1.draw(self.display, offset=self.scroll)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                    if event.key == pygame.K_SPACE:
                        # Check for collision with the pendulum when space is pressed
                        if self.rod.rect().colliderect(self.player.rect()):
                            print(self.player.velocity)
                            self.rod.attach_entity(self.player)
                        if self.rod1.rect().colliderect(self.player.rect()):
                            self.rod1.attach_entity(self.player)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pygame.K_SPACE and self.rod.attached_entity:
                        # Detach the player when space is released
                        self.rod.detach_entity()
                    if event.key == pygame.K_SPACE and self.rod1.attached_entity:
                        # Detach the player when space is released
                        self.rod1.detach_entity()

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()