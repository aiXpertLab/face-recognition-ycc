class Settings:
    """a class to store all settings"""
    def __init__(self) -> None:
        self.screen_width   = 1200
        self.screen_height  = 800
        self.bg_color       = (23,230,230)

        # ship settings
        self.ship_speed = 2.5
        self.ship_limit = 1

        # Bullet settings
        self.bullet_speed = 2.8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (240, 67, 60)
        self.bullets_allowed = 8

        # alien settings
        self.alien_speed = 2.0
        self.fleet_drop_speed = 20
        self.fleet_direction = 1
        