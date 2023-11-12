import os
import pygame

BASE_IMG_PATH = 'resources/images/'

def load_image(path):
    #for better performance use convert
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0 ,0))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images

class Animation: 
    def __init__(self, images, img_dur = 5, loop= True) -> None:
        self.images =images
        self.loop = loop
        self.img_duration = img_dur
        self.done = False
        self.fram = 0
        
    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)
    
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images)) #loop over the elements in the list of animations to not get index error
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1) #don´t go pass the end of the animation, 
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True
    
    def img(self):
        return self.images[int(self.frame / self.img_duration)] #frame divide by how long each image is supposed to show for
    
    
        
    