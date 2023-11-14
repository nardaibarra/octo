import pygame
import math as m

class Rod:
    def __init__(self, game, position, length, radius):
        self.game = game
        self.position = position  # Position of the pendulum's anchor point
        self.length = length
        self.radius = radius
        self.angle = -20  # Initial angle
        self.angular_velocity = -0.002
        self.swinging = True
        self.attached_entity = None
        self.gravity = 0.01  # Gravity effect
        self.vertical_velocity = 0  # Vertical velocity

    def rect(self):
        end_x = self.position[0] + self.length * m.sin(self.angle)
        end_y = self.position[1] + self.length * m.cos(self.angle)
        return pygame.Rect(end_x - self.radius, end_y - self.radius, self.radius * 2, self.radius * 2)

    def attach_entity(self, entity):
        self.attached_entity = entity
        self.swinging = True

    def detach_entity(self):
        if self.attached_entity:
            # Calculate the pendulum's velocity components
            horizontal_velocity = self.length * self.angular_velocity * m.cos(self.angle)
            vertical_velocity = -self.length * self.angular_velocity * m.sin(self.angle)

            # Apply this velocity to the attached entity
            self.attached_entity.velocity[0] = horizontal_velocity * 2
            self.attached_entity.velocity[1] = vertical_velocity * 2

            # Detach the entity
            self.attached_entity = None
            self.swinging = False

    def update(self):
        if self.swinging and self.attached_entity:
            # Pendulum physics
            g = 0.3  # Acceleration due to gravity
            angular_acceleration = -(g / self.length) * m.sin(self.angle)
            self.angular_velocity += angular_acceleration
            self.angle += self.angular_velocity

            # # Damping (optional)
            # self.angular_velocity *= 0.99

            # Gravity effect on the attached entity
            self.vertical_velocity = min(3, self.vertical_velocity + self.gravity)
            if self.attached_entity.collisions['down']:
                self.vertical_velocity = 0

            # Update the position of the attached entity
            end_x = self.position[0] + self.length * m.sin(self.angle)
            end_y = self.position[1] + self.length * m.cos(self.angle) + self.vertical_velocity
            self.attached_entity.pos = [end_x - self.radius, end_y - self.radius]

    def draw(self, surface, offset=(0, 0)):
        # Calculate pendulum's end position based on angle
        end_x = self.position[0] + self.length * m.sin(self.angle)
        end_y = self.position[1] + self.length * m.cos(self.angle)
        # Draw the pendulum
        pygame.draw.line(surface, (255, 255, 255), (self.position[0] - offset[0], self.position[1] - offset[1]), (end_x - offset[0], end_y - offset[1]), 4)
        pygame.draw.circle(surface, (255, 0, 0), (round(end_x - offset[0]), round(end_y - offset[1])), self.radius)
