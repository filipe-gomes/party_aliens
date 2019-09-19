class GameStats():
    """Track statistics for Party Aliens."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Party Aliens in an inactive state.
        self.game_active = False

        # High score has static value, never reset.
        self.highscore = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
