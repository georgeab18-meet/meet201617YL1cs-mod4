from rectangle import Rectangle
from square import Square
import turtle
import time

###############################
#         RECTANGLE           #
###############################

my_rect=Rectangle(10,10,45)
print('The area of the rectangle is '+str(my_rect.get_area())+'.')

my_rect.set_length(50)
print('Now, the area of the rectangle is '+str(my_rect.get_area())+'.')

my_rect.draw_shape() #Draw the rectangle
time.sleep(1) #Wait 1 second

my_rect.set_height(200)
print('Now, the area of the rectangle is '+str(my_rect.get_area())+'.')
time.sleep(1) #Wait 1 second

###############################
#          SQUARE             #
###############################

my_square=Square(50)

my_square.set_length(10)
print('The area of the square is '+str(my_square.get_area())+'.')

my_square.draw_shape() #Draw the square
time.sleep(1) #Wait 1 second

my_square.set_length(50)
print('Now, the area of the square is '+str(my_square.get_area())+'.')
time.sleep(1) #Wait 1 second

my_square.set_length(100)
print('Now, the area of the square is '+str(my_square.get_area())+'.')
time.sleep(1) #Wait 1 second

turtle.mainloop()
