import pygame

class Ship:
    """manage the ship"""
    def __init__(self, ai_game) -> None:
        print(f"\nself in Ship: {self}")
        print(f"ai_game in Ship: {ai_game}")
        self.screen = ai_game.screen
        self.settings = ai_game.settings    
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('c12/image/ship.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left  = False

    def update(self):
            """Update the ship's position based on the movement flag."""
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed
                
            if self.moving_left and self.rect.left > 0:
                self.x -= self.settings.ship_speed
            
            # Update rect object from self.x.
            self.rect.x = self.x    

    def center_ship(self):
         self.rect.midbottom = self.screen_rect.midbottom
         self.x = float(self.rect.x)

    def blitme(self):
        """draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)