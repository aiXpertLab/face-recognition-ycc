import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
     """overall class to manage assets and behavior"""
     def __init__(self):
          """Initialzie the game, and create game resources"""
          pygame.init()

          self.clock    = pygame.time.Clock()
          self.settings = Settings()
          # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
          # self.settings.screen_width = self.screen.get_rect().width
          # self.settings.screen_height = self.screen.get_rect().height
          self.screen   = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))

          pygame.display.set_caption("LEO Alien Invasion")
          self.ship     = Ship(self)
          self.bullets  = pygame.sprite.Group()
          print(f"\nself in AlienInvasion: {self}")

          self.bg_color = (23, 230, 230)

     def _check_events(self):
            #watch for keyboard & mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                     
                elif event.type == pygame.KEYUP:
                     print("key up")
                     self._check_keyup_events(event)

     def _check_keydown_events(self, event):
                     if event.key == pygame.K_RIGHT:
                          print("key right")
                          self.ship.moving_right = True
                          self.ship.rect.x += 10

                     elif event.key == pygame.K_LEFT:
                          print("key left")
                          self.ship.moving_left = True
                          self.ship.rect.x -= 10
               
                     elif event.key == pygame.K_q:
                         sys.exit()
                     elif event.key == pygame.K_SPACE:
                         self._fire_bullet()

     def _fire_bullet(self):
          print("new bullets ------- --  ---   ----  --")
          if len(self.bullets) < self.settings.bullets_allowed:
               new_bullet = Bullet(self)
               self.bullets.add(new_bullet)

     def _check_keyup_events(self, event):
                          if event.key == pygame.K_RIGHT:
                             self.ship.moving_right = False           
                          if event.key == pygame.K_LEFT:
                             self.ship.moving_left  = False           
     def _update_bullets(self):
          self.bullets.update()

             # get rid of bullets
          for bullet in self.bullets.copy():
               if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
 
     def _update_screen(self):
            # redraw the screen
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
               bullet.draw_bullet()
            self.ship.blitme()

            # make the most recently drawn screen visible
            pygame.display.flip()   
    
     def run_game(self):
        """start the main loop for the game"""
        while True:
             self._check_events()
             self.ship.update()
             self._update_bullets()
             self._update_screen()
             self.clock.tick(60)

if __name__=='__main__':
    # make a game instance, and run the game,
    ai = AlienInvasion()
    print(f"  ai in AlienInvasion: {ai}")
    ai.run_game()
