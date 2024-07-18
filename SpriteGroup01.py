import pygame
import random

pygame.init()

#define screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Groups")

#frame rate
clock = pygame.time.Clock()
FPS = 60

#create class for squares
class Square(pygame.sprite.Sprite):
  def __init__(self, col, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((50, 50))
    self.image.fill(col)
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)

#create square and add to squares group
square = Square("crimson", 500, 300)
print(square)

#game loop
run = True
while run:

  clock.tick(FPS)

  #update background
  screen.fill("cyan")

  #event handler
  for event in pygame.event.get():
    #quit program
    if event.type == pygame.QUIT:
      run = False

  #update display
  pygame.display.flip()

pygame.quit()