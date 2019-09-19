class Settings():
    """A class to store all settings for Party Aliens!"""

    def __init__(self):
        """Initialize the static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # This defines the scale at which the game speeds up
        self.speedup_scale = 1.3

        # This defines the scale at which aliens point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize the settings that will change throughout the game."""
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 14
        self.alien_speed_factor = 7

        # Scoring
        self.alien_points = 50

        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and points awarded for aliens killed."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
