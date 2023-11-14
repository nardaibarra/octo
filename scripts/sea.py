import random

class Sea:
    def __init__(self, pos, img) -> None:
        self.pos = list(pos)
        self.img = img


    def render(self, surf, offset=(0,0)):
        render_pos = (self.pos[0], self.pos[1] - offset[1])
        surf.blit(self.img, (render_pos[0] % (surf.get_width() + self.img.get_width()) - self.img.get_width(), render_pos[1] % (surf.get_height() + self.img.get_height()) - self.img.get_height()))

