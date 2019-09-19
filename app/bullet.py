import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set the correct position.
        self.images = [pygame.image.load('../images/fireball_0.bmp'), pygame.image.load('../images/fireball_1.bmp'), pygame.image.load('../images/fireball_3.bmp'), pygame.image.load('../images/fireball_4.bmp'), pygame.image.load('../images/fireball_5.bmp'), pygame.image.load('../images/fireball_6.bmp'), pygame.image.load('../images/fireball_7.bmp'), pygame.image.load('../images/fireball_8.bmp')]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y
        # Update the sprite animation.
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
    
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
