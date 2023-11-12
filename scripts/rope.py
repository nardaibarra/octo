

import math
import random
import pygame

class Rope:
    def __init__(self, pos, length, angle, width = 2, color= (255, 0, 0)) -> None:
        self.pos = list(pos)
        self.length = length
        self.angle = angle
        self.width = width
        self.color = color
        self.swing_speed = 0.02  # Modify as needed for the swing speed
        self.swing_direction = 1  # 1 for one side, -1 for the other

    def update(self):
        #Aquí tenemos que updatear la parte de abajo
        self.angle += self.swing_speed * self.swing_direction
        if abs(self.angle) > math.pi / 4:  # Change to adjust swing range
            self.swing_direction *= -1
        
    def calculate_end_position(self, offset=(0,0)):
        # Calculate the end position of the rope based on the angle
        end_x = (self.pos[0]) + self.length * math.sin(self.angle) - offset[0]
        end_y = (self.pos[1]) + self.length * math.cos(self.angle) - offset[1]
        return (end_x, end_y)

    def render(self, surf, offset=(0,0)):
        end_pos = self.calculate_end_position(offset)
        pygame.draw.line(surf, self.color, self.pos, end_pos, self.width)
        

class Ropes:
    def __init__(self, count=16) -> None:
        self.ropes = []

        for i in range(count):
            self.ropes.append(Rope((random.randint(0, 640), random.randint(0, 480)), 50, 15))
        
    def update(self):
        for rope in self.ropes:
            rope.update()

    def render(self, surf, offset=(0,0)):
        for rope in self.ropes:
            rope.render(surf, offset = offset)
    




# import pygame
# import math

# class Rope:
#     def __init__(self, start_pos, img, length, angle, width=2, color=(255, 255, 255)):
#         self.start_pos = list(start_pos)
#         self.img = img
#         self.length = length
#         self.angle = angle
#         self.width = width
#         self.color = color
#         self.swing_speed = 0.02  # Modify as needed for the swing speed
#         self.swing_direction = 1  # 1 for one side, -1 for the other

#     def update(self):
#         # Update the swing angle
#         self.angle += self.swing_speed * self.swing_direction
#         if abs(self.angle) > math.pi / 4:  # Change to adjust swing range
#             self.swing_direction *= -1

#     # def check_collision(self, player_rect):
#     #     # Check if player collides with the rope
#     #     end_pos = self.calculate_end_position()
#     #     rope_rect = pygame.Rect(*self.start_pos, end_pos[0] - self.start_pos[0], end_pos[1] - self.start_pos[1])
#     #     return rope_rect.colliderect(player_rect)

#     def calculate_end_position(self):
#         # Calculate the end position of the rope based on the angle
#         end_x = self.start_pos[0] + self.length * math.sin(self.angle)
#         end_y = self.start_pos[1] + self.length * math.cos(self.angle)
#         return (end_x, end_y)

#     def render(self, surf, offset =(0,0)):
#         # Draw the rope
        
#         # render_pos = (self.pos[0] - offset[0], self.pos[1] - offset[1])
         
#         end_pos = self.calculate_end_position()
#         pygame.draw.line(surf, self.color, self.start_pos - offset, end_pos - offset, self.width)