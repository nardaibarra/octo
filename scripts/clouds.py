import random
import pygame

class Cloud:
    def __init__(self, pos, img, speed, depth) -> None:
        self.pos = list(pos)
        self.img = img
        self.speed = speed
        self.depth = depth

    def update(self):
        self.pos[1] -= self.speed
        
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.img.get_width(), self.img.get_height())

    def render(self, surf, offset=(0,0), draw = False):
        
        render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)
        # render_pos = (self.pos[0] - offset[0], self.pos[1] - offset[1])
        
        surf.blit(self.img, (render_pos[0] % (surf.get_width() + self.img.get_width()) - self.img.get_width(), render_pos[1] % (surf.get_height() + self.img.get_height()) - self.img.get_height()))

        # if draw:
        #     rect = self.rect()
        #     pygame.draw.rect(surf,(255, 0, 0), rect, 2)
            # print(f'cloud drawing {rect}')

class Clouds:
    def __init__(self, cloud_images, count = 16) -> None:
        self.clouds = []

        for i in range(count):
            self.clouds.append(Cloud((random.random() * 99999, random.random() * 99999), random.choice(cloud_images), random.random()* 0.05 + 0.05, random.random()* 0.6 + 0.2))
        
        self.clouds.sort(key=lambda x: x.depth) #the clouds closer to camara will be pushed to the front while rendering
    
    def update(self):
        for cloud in self.clouds:
            cloud.update()

    def render(self, surf, offset=(0,0), draw = False):
        for cloud in self.clouds:
            cloud.render(surf, offset=offset, draw=draw)
    
    
    def check_player_collision(self, player):
        for cloud in self.clouds:
            cloud_rect = cloud.rect()
            if player.colliderect(cloud_rect):
                return True
        return False