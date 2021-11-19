###################################################################
##  Playing Sound and Music
###################################################################

## Playing Sounds
"""
   * Playing sounds that are stored in sound files is even simpler than displaying images from image files.

   * First, you must create a pygame.mixer.Sound object (which we will call Sound objects for short) by calling
     the pygame.mixer.Sound() constructor function.
     - It takes one string parameter, which is the filename of the sound file.
     - Pygame can load WAV, MP3, or OGG files.

   * To play this sound, call the Sound object’s play() method.
     - If you want to immediately stop the Sound object from playing call the stop() method.
     - The stop() method has no arguments.

   * The Sound objects are good for sound effects to play when the player takes damage, slashes a sword, or
     collects a coin.
"""

## Playing Music
"""
   * Pygame can only load one music file to play in the background at a time. 
     - To load a background music file, call the pygame.mixer.music.load() function and pass it a string argument 
       of the sound file to load. 
     - This file can be WAV, MP3, or MIDI format.
     
   * To begin playing the loaded sound file as the background music, call the pygame.mixer.music.play(-1, 0.0) function. 
     - The -1 argument makes the background music forever loop when it reaches the end of the sound file. 
     - If you set it to an integer 0 or larger, then the music will only loop that number of times instead of 
       looping forever. 
     - The 0.0 means to start playing the sound file from the beginning. 
     - If you pass a larger integer or float, the music will begin playing that many seconds into the sound file.
     
   * To stop playing the background music immediately, call the pygame.mixer.music.stop() function.
"""

import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window


# Loading and playing background music:



# run the game loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()