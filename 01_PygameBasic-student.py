
# Imports the required modules
"""
   * import pygame and sys modules so that our program can use the functions in them.
"""



# Normally if you want to call a function that is in a module, you must use the "modulename.functionname()" format
# after importing the module. However, with "from modulename import *", you can skip the modulename. portion and simply
# use functionname() (just like Python’s built-in functions).
"""
   * The reason we use this form of import statement for pygame.locals is because "pygame.locals" contains several 
     constant variables that are easy to identify as being in the "pygame.locals" module without "pygame.locals." in 
     front of them.
     - Like the "QUIT"
"""



# It needs to be called first in order for many Pygame functions to work.



# dsplay.set_mode() function
"""
   * A call to the pygame.display.set_mode() function, which returns the "pygame.Surface" object for the window. 
     - Notice that we pass a tuple value of two integers to the function: (400, 300). 
     - This tuple tells the set_mode() function how wide and how high to make the window in pixels.
     
   * Surface object and the Window
     - Surface objects are objects that represent a rectangular 2D image. The pixels of the Surface object can be 
       changed by calling the Pygame drawing functions and then displayed on the screen. 
     - The window border, title bar, and buttons are not part of the display Surface object.
     - Anything that is drawn on the display Surface object will be displayed on the window when the 
       pygame.display.update() function is called. 
     - It is a lot faster to draw on a Surface object (which only exists in the computer’s memory) than it is 
       to draw a Surface object to the computer screen. 
"""



# display.set_caption() function
"""
   * It sets the caption text that will appear at the top of the window.
"""



# Game loop concept
"""
   * A game loop (also called a main loop) is a loop where the code does three things:
     1. Handles events.
     2. Updates the game state.
     3. Draws the game state to the screen.
     
   * One iteration of the game loop is called a frame.
     
   * The game state is simply a way of referring to a set of values for all the variables in a game program. 
     - In many games, the game state includes the values in the variables that tracks the player’s health and position, 
       the health and position of any enemies, which marks have been made on a board, the score, or whose turn it is. 
     - Whenever something happens like the player taking damage (which lowers their health value), or an enemy moves 
       somewhere, or something happens in the game world we say that the game state has changed.
     - If you’ve ever played a game that let you saved, the "save state" is the game state at the point that you’ve 
       saved it. In most games, pausing the game will prevent the game state from changing.
       
   * Since the game state is usually updated in response to events (such as mouse clicks or keyboard presses) or the 
     passage of time, the game loop is constantly checking and re-checking many times a second for any new events that 
     have happened. 
     - Inside the main loop is code that looks at which events have been created (with Pygame, this is done by 
       calling the pygame.event.get() function). 
     - The main loop also has code that updates the game state based on which events have been created. 
     - This is usually called event handling.
     
   * The computer can draw frames very quickly, and our programs will often run around 30 frames per second 
     (that is, 30 FPS). This is called the "frame rate".
"""

# pygame.event.Event Objects
"""
   * Any time the user does one of several actions such as pressing a keyboard key or moving the mouse on the 
     program’s window, a pygame.event.Event object is created by the Pygame library to record this event. 
     - This is a type of object called Event that exists in the event module, which itself is in the pygame module.
     
   * We can find out which events have happened by calling the pygame.event.get() function, which returns a list of 
     pygame.event.Event objects (which we will just call Event objects for short).

   * The list of Event objects will be for each event that has happened since the last time the pygame.event.get() 
     function was called. 
     (Or, if pygame.event.get() has never been called, the events that have happened since the start of the program.)
     
   * Event objects have a member variable (also called attributes or properties) named "type" which tells us what kind 
     of event the object represents. 
     - Pygame has a constant variable for each of possible types in the pygame.locals modules.
     
   * If the Event object is a quit event, then the pygame.quit() and sys.exit() functions are called. 
     - The pygame.quit() function is sort of the opposite of the pygame.init() function: it runs code that deactivates 
       the Pygame library. 
     - Your programs should always call pygame.quit() before they call sys.exit() to terminate the program.
"""

# display.update()
"""
   * It draws the Surface object returned by pygame.display.set_mode() to the screen (remember we stored this object 
     in the DISPLAYSURF variable). 
     - Since the Surface object hasn’t changed the same black image is redrawn to the screen each time 
       pygame.display.update() is called.
"""


    
    
# Pixel Coordinates
"""
   * The window that the ―Hello World‖ program creates is just composed of little square dots on your screen 
     called pixels. 
     - Each pixel starts off as black but can be set to a different color.
     
             0 1 2 3 4 5 6 7
           0     x     x
           1   x
           2
           3       x x x
           4
           5
           6
           7
           
     - Columns are "X-axis", rows are "Y-axis". ==> (2,0),(5,0),(1,1),(3,3),(4,3),(5,3)
"""