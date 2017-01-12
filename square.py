import turtle

class Square :
    def __init__(self,length):
        """
        Initialize new rectangle instance.

        :param length: length of rectangle (horizontal dimension).  Must be >= 0.  Otherwise, set to 0.
        :param length: height of rectangle (vertical dimension).  Must be >= 0.  Otherwise, set to 0.
        """
        if length>=0 :
            self.length=length
        else :
            self.length=0

        self.turtle=turtle.clone() #Make a new turtle object just for this instance so that drawings can be cleared.
        turtle.speed(0) #Make turtle move as fast as possible.
        self.has_been_drawn=False #Keep track of whether shape has been drawn.

    def set_length(self,new_length):
        """
        Change the length of the rectangle.

        :param new_length: length (horizontal dimension) of rectangle.  Must be >= 0.  Otherwise, no change is made.
        """
        if new_length>=0 :
            self.length=new_length
            if self.has_been_drawn : #Only redraw rectangle; don't make new drawing.
                self.draw_shape()

    def get_area(self):
        """
        Calculate the area of the shape
        """
        return self.length**2

    def draw_shape(self):
        """
        Draw the shape, starting at 0,0.

        If any old drawings exist, remove them.
        """
        self.turtle.clear() #Remove old drawings (if they exist)
        self.turtle.penup()
        self.turtle.goto(0,0)
        self.turtle.pendown()
        self.turtle.goto(self.length,0)
        self.turtle.goto(self.length,self.length)
        self.turtle.goto(0,self.length)
        self.turtle.goto(0,0)
        self.turtle.penup()
        self.has_been_drawn=True
