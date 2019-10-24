import json
import pygame.font
from pygame.sprite import Group

class Instructions():
    """Show instructions on screen when game is not active."""

    def __init__(self):
        """Initialize attributes."""
        self.text_color = (0, 255, 0)
        self.font = pygame.font.Font('fonts/Acme-Regular.ttf', 48)

        # Call render function.
        self.prep_instructions()

    def prep_instructions(self):
        """Turn instructions into rendered image."""
        self.instructions_image = self.font.render(score_str, True, self.text_color)
        self.instructions_image = self.instructions_image.get_rect()
        self.instructions_image.right = self.screen_rect.center
        self.instructions_image.top = self.screen_rect.bottom
