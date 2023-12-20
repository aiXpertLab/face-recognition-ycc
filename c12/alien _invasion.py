import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

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

          # create an instance to store game stat
          self.stats = GameStats(self)

          self.bg_color = (23, 230, 230)
          self.ship     = Ship(self)
          self.bullets  = pygame.sprite.Group()
          self.aliens   = pygame.sprite.Group()
          self._create_fleet()

     def _create_alien(self, x_position, y_position):
                new_alien = Alien(self)
                new_alien.x = x_position
                new_alien.rect.x = x_position
                new_alien.rect.y = y_position
                self.aliens.add(new_alien)
           
     def _create_fleet(self):
          alien = Alien(self)
          alien_width, alien_height = alien.rect.size
          print("create fleet")

          current_x, current_y = alien_width, alien_height
          while current_y < (self.settings.screen_height - 3 * alien_height):
               while current_x < (self.settings.screen_width - 2 * alien_width):
                    self._create_alien(current_x, current_y)                
                    current_x += 2 * alien_width
               print ("finish a row, reset x value")
               current_x  = alien_width
               current_y += 2 * alien_height

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
          
          for bullet in self.bullets.copy():
               if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

          self._check_bullet_alien_collisions()

     def _check_bullet_alien_collisions(self):
          """respond to bulet-alien"""

          collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

          if not self.aliens:
                self.bullets.empty()
                self._create_fleet()

     def _update_aliens(self):
           self._check_fleet_edges()
           self.aliens.update()

           if pygame.sprite.spritecollideany(self.ship, self.aliens):
                 self._ship_hit()

     def _update_screen(self):
            # redraw the screen
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
               bullet.draw_bullet()
            self.ship.blitme()
            self.aliens.draw(self.screen)

            # make the most recently drawn screen visible
            pygame.display.flip()   
    
     def _check_fleet_edges(self):
           for alien in self.aliens.sprites():
                 if alien.check_edges():
                       self._change_fleet_direction()
                       break

     def _change_fleet_direction(self):
          for alien in self.aliens.sprites():
                 alien.rect.y += self.settings.fleet_drop_speed
          self.settings.fleet_direction *= -1
    
     def _ship_hit(self):
           self.stats.ships_left -=1

           self.bullets.empty()
           self.aliens.empty()

           self._create_fleet()
           self.ship.center_ship()

           
           sleep(0.5)

     def run_game(self):
        """start the main loop for the game"""
        while True:
             self._check_events()
             self.ship.update()
             self._update_bullets()
             self._update_aliens()
             self._update_screen()
             self.clock.tick(60)

if __name__=='__main__':
    # make a game instance, and run the game,
    ai = AlienInvasion()
    print(f"  ai in AlienInvasion: {ai}")
    ai.run_game()
