###################################################################
##  Font and Anti-Alias
###################################################################

## Making Text in Pygame
"""
   * There are six steps to making text appear on the screen:
     1. Create a pygame.font.Font object.
        - The parameters to the pygame.font.Font() constructor function is a string of the font file to use.
        - The integer is the size of the font.

     2. Create a Surface object with the text drawn on it by calling the Font object’s render() method.
        - The parameters to the render() method call are a string of the text to render, a Boolean value to specify
          if we want anti-aliasing, the color of the text, and the color of the background.
        - If you want a transparent background, then simply leave off the background color parameter in the method call.

     3. Create a Rect object from the Surface object by calling the Surface object’s get_rect() method.
        - This Rect object will have the width and height correctly set for the text that was rendered, but the
          top and left attributes will be 0.

     4. Set the position of the Rect object by changing one of its attributes.
        - We can set the center of the Rect object.

     5. Blit the Surface object with the text onto the Surface object returned by pygame.display.set_mode().

     6. Call pygame.display.update() to make the display Surface appear on the screen.
"""

## Anti-Aliasing
"""
   * Anti-aliasing is a graphics technique for making text and shapes look less blocky by adding a little bit 
     of blur to their edges. 
     - It takes a little more computation time to draw with anti-aliasing, so although the graphics may look better, 
       your program may run slower (but only just a little).
"""


import pygame, sys
from pygame.locals import *

pygame.init()






while True: # main game loop

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()