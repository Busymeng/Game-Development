###################################################################
##  Color, Rect, Drawing shapes and PixelArray
###################################################################

## Colors in Pygame
"""
   * In Pygame, we represent colors with tuples of three integers.
     - The first value in the tuple is how much red is in the color.
       -> An integer value of 0 means there is no red in this color, and a value of 255 means there is the
          maximum amount of red in the color.
     - The second value is for green and the third value is for blue.
     - These tuples of three integers used to represent a color are often called RGB values.
       -> Pygame can draw 16,777,216 different colors (that is, 256 x 256 x 256 colors).

           Aqua             ( 0, 255, 255)
           Black            ( 0, 0, 0)
           Blue             ( 0, 0, 255)
           Fuchsia          (255, 0, 255)
           Gray             (128, 128, 128)
           Green            ( 0, 128, 0)
           Lime             ( 0, 255, 0)
           Maroon           (128, 0, 0)
           Navy Blue        ( 0, 0, 128)
           Olive            (128, 128, 0)
           Purple           (128, 0, 128)
           Red              (255, 0, 0)
           Silver           (192, 192, 192)
           Teal             ( 0, 128, 128)
           White            (255, 255, 255)
           Yellow           (255, 255, 0)

   * Transparent color
     - There is a fourth value to the color in Pygame.
     - This value is known as the alpha value.
       -> It is a measure of how opaque (that is, not transparent) a color is.
     - Normally when you draw a pixel onto a surface object, the new color completely replaces whatever color was
       already there.
       -> But with colors that have an alpha value, you can instead just add a colored tint to the color that
          is already there.
     - In order to draw using transparent colors, you must create a Surface object with the convert_alpha() method.
       -> anotherSurface = DISPLAYSURF.convert_alpha()
     - Once things have been drawn on the Surface object stored in anotherSurface, then anotherSurface can be "blitted"
       (that is, copied) to DISPLAYSURF so it will appear on the screen.
     - It’s important to note that you cannot use transparent colors on Surface objects not returned from a
       convert_alpha() call, including the display Surface that was returned from pygame.display.set_mode().

   * You can create Color objects by calling the pygame.Color() constructor function and passing either three or
     four integers.
     - You can store this Color object in variables just like you can store tuples in variables.
"""

## Rect Objects
"""
   * Pygame has two ways to represent rectangular areas (just like there are two ways to represent colors). 

   * The first is a tuple of four integers:
     1. The X coordinate of the top left corner.
     2. The Y coordinate of the top left corner.
     3. The width (in pixels) of the rectangle.
     4. Then height (in pixels) of the rectangle.

   * The second way is as a pygame.Rect object, which we will call Rect objects for short.
     - spamRect = pygame.Rect(10, 20, 200, 300)
     - The Rect object automatically calculates the coordinates for other features of the rectangle.
       
            myRect.left         The int value of the X-coordinate of the left side of the rectangle.
            myRect.right        The int value of the X-coordinate of the right side of the rectangle.
            myRect.top          The int value of the Y-coordinate of the top side of the rectangle.
            myRect.bottom       The int value of the Y-coordinate of the bottom side.
            myRect.centerx      The int value of the X-coordinate of the center of the rectangle.
            myRect.centery      The int value of the Y-coordinate of the center of the rectangle.
            myRect.width        The int value of the width of the rectangle.
            myRect.height       The int value of the height of the rectangle.
            myRect.size         A tuple of two ints: (width, height)
            myRect.topleft      A tuple of two ints: (left, top)
            myRect.topright     A tuple of two ints: (right, top)
            myRect.bottomleft   A tuple of two ints: (left, bottom)
            myRect.bottomright  A tuple of two ints: (right, bottom)
            myRect.midleft      A tuple of two ints: (left, centery)
            myRect.midright     A tuple of two ints: (right, centery)
            myRect.midtop       A tuple of two ints: (centerx, top)
            myRect.midbottom    A tuple of two ints: (centerx, bottom)  
"""

## Primitive Drawing Functions
"""
   * Pygame provides several different functions for drawing different shapes onto a surface object. 
     - These shapes such as rectangles, circles, ellipses, lines, or individual pixels are often called 
       drawing primitives.

   * fill(color) – 
     - The fill() method is not a function but a method of pygame.Surface objects. 
     - It will completely fill in the entire Surface object with whatever color value you pass as for the 
       color parameter.
       
   * pygame.draw.polygon(surface, color, pointlist, width) – 
     - A polygon is shape made up of only flat sides. 
     - The surface and color parameters tell the function on what surface to draw the polygon, and what color to 
       make it.
     - The pointlist parameter is a tuple or list of points (that is, tuple or list of two-integer tuples 
       for XY coordinates). 
       -> The polygon is drawn by drawing lines between each point and the point that comes after it in the tuple. 
       -> Then a line is drawn from the last point to the first point. 
       -> You can also pass a list of points instead of a tuple of points.
     - The width parameter is optional. If you leave it out, the polygon that is drawn will be filled in, just like 
       our green polygon on the screen is filled in with color. 
       -> If you do pass an integer value for the width parameter, only the outline of the polygon will be drawn. 
       -> The integer represents how many pixels width the polygon’s outline will be. 
       -> Passing 1 for the width parameter will make a skinny polygon, while passing 4 or 10 or 20 will make 
          thicker polygons. 
       -> If you pass the integer 0 for the width parameter, the polygon will be filled in (just like if you left 
          the width parameter out entirely).
      - All of the pygame.draw drawing functions have optional width parameters at the end, and they work the same 
        way as pygame.draw.polygon()’s width parameter. 
        -> Probably a better name for the width parameter would have been thickness, since that parameter controls 
           how thick the lines you draw are.
           
   * pygame.draw.line(surface, color, start_point, end_point, width) – 
     - This function draws a line between the start_point and end_point parameters.
     
   * pygame.draw.lines(surface, color, closed, pointlist, width) – 
     - This function draws a series of lines from one point to the next, much like pygame.draw.polygon(). 
     - The only difference is that if you pass False for the closed parameter, there will not be a line from the 
       last point in the pointlist parameter to the first point. 
     - If you pass True, then it will draw a line from the last point to the first.
     
   * pygame.draw.circle(surface, color, center_point, radius, width) – 
     - This function draws a circle. 
     - The center of the circle is at the center_point parameter. 
     - The integer passed for the radius parameter sets the size of the circle.
       -> The radius of a circle is the distance from the center to the edge. (The radius of a circle is always 
          half of the diameter.) 
          
   * pygame.draw.ellipse(surface, color, bounding_rectangle, width) – 
     - This function draws an ellipse. 
     - This function has all the usual parameters, but in order to tell the function how large and where to draw the 
       ellipse, you must specify the bounding rectangle of the ellipse. 
     - A bounding rectangle is the smallest rectangle that can be drawn around a shape. 
     - The bounding_rectangle parameter can be a pygame.Rect object or a tuple of four integers. N
     - Note that you do not specify the center point for the ellipse like you do for the pygame.draw.circle() function.
     
   * pygame.draw.rect(surface, color, rectangle_tuple, width) – 
     - This function draws a rectangle. 
     - The rectangle_tuple is either a tuple of four integers (for the XY coordinates of the top left corner, 
       and the width and height) or a pygame.Rect object can be passed instead. 
     - If the rectangle_tuple has the same size for the width and height, a square will be drawn.
"""

## pygame.PixelArray Objects
"""
   * Unfortunately, there isn’t a single function you can call that will set a single pixel to a color. If it had to
     do this for every single pixel you wanted to set, your program would run much slower.
     
   * Instead, you should create a pygame.PixelArray object of a Surface object and then set individual pixels. 
     - Creating a PixelArray object of a Surface object will "lock" the Surface object. 
     - While a Surface object is locked, the drawing functions can still be called on it, but it cannot have 
       images like PNG or JPG images drawn on it with the blit() method.
     - If you want to see if a Surface object is locked, the get_locked() Surface method will 
       return True if it is locked and False if it is not.
     - The PixelArray object can have individual pixels set by accessing them with two indexes.
     - To tell Pygame that you are finished drawing individual pixels, delete the PixelArray object with 
       a del statement. 
       -> Deleting the PixelArray object will "unlock" the Surface object so that you can once again draw images on it. 
       -> If you forget to delete the PixelArray object, the next time you try to blit (that is, draw) an image to 
          the Surface the program will raise an error that says, 
          "pygame.error: Surfaces must not be locked during blit".
"""

## pygame.display.update()
"""
   * The one thing that you must remember is that pygame.display.update() will only make the display Surface 
     (that is, the Surface object that was returned from pygame.display.set_mode()) appear on the screen. 
     - If you want the images on other Surface objects to appear on the screen, you must "blit" them 
       (that is, copy them) to the display Surface object with the blit() method.
"""

import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window


# set up the colors


# draw on the surface object


# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()