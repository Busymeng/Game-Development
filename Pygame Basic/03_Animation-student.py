###################################################################
##  Animation
###################################################################

## Animation
"""
   * Animated images are the result of drawing an image on the screen, then a split second later drawing a
     slightly different image on the screen.
"""

## Frames Per Second and pygame.time.Clock Objects
"""
   * The frame rate or refresh rate is the number of pictures that the program draws per second, and is measured 
     in FPS or frames per second.
     - On computer monitors, the common name for FPS is hertz. 
     - Many monitors have a frame rate of 60 hertz, or 60 frames per second.
     - A low frame rate in video games can make the game look choppy or jumpy. 
     - If the program has too much code to run to draw to the screen frequently enough, then the FPS goes down.
     
   * A pygame.time.Clock object can help us make sure our program runs at a certain maximum FPS. 
     - This Clock object will ensure that our game programs don’t run too fast by putting in small pauses on 
       each iteration of the game loop. 
     - If we didn’t have these pauses, our game program would run as fast as the computer could run it. 
     - This is often too fast for the player, and as computers get faster they would run the game faster too. 
     - A call to the tick() method of a Clock object in the game loop can make sure the game runs at the same speed 
       no matter how fast of a computer it runs on.
       
   * The Clock object’s tick() method should be called at the very end of the game loop, after the call to 
     pygame.display.update(). 
     - The length of the pause is calculated based on how long it has been since the previous call to tick(), 
       which would have taken place at the end of the previous iteration of the game loop.
       
   * Try modifying the FPS constant variable to run the same program at different frame rates. 
     - Setting it to a lower value would make the program run slower. 
     - Setting it to a higher value would make the program run faster.
"""

## Drawing Images with pygame.image.load() and blit()
"""
   * Pygame is able to load images onto Surface objects from PNG, JPG, GIF, and BMP image files.
     - To load the image, the image filename is passed to the pygame.image.load() function.
     - Make sure the image in in the same folder or with the right file path name.
     - It will return a Surface object that has the image drawn on it.
     - This Surface object will be a separate Surface object from the display Surface object, so we must blit 
       the image’s Surface object to the display Surface object. 
       -> Blitting is drawing the contents of one Surface onto another. 
       -> It is done with the blit() Surface object method.
       
   * surface_name.blit(source, (x, y))
     - source is the surface object that will be copied to surface_name surface object.
     - (x,y) specifies the topleft corner that the source will be blitted. 
"""

import pygame, sys
from pygame.locals import *

pygame.init()



# set up the window




while True: # the main game loop

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
