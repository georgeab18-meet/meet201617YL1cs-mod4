import turtle
import math

class Rectangle :
    def __init__(self,length,height,angle,xstart,ystart):
        """
        Initialize new rectangle instance.

        :param length: length of rectangle (horizontal dimension).  Must be >= 0.  Otherwise, set to 0.
        :param length: height of rectangle (vertical dimension).  Must be >= 0.  Otherwise, set to 0.
        """
        if length>=0 :
            self.length=length
        else :
            self.length=0

        if height>=0 :
            self.height=height
        else :
            self.height=0

        if angle>=0 :
            self.angle=angle
        else :
            self.angle=0

        self.xstart=xstart

        self.ystart=ystart

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

    def set_height(self,new_height):
        """
        Change the height of the rectangle.

        :param new_height: height (vertical dimension) of rectangle.  Must be >= 0.  Otherwise, no change is made.
        """   
        if new_height>=0 :
            self.height=new_height
            if self.has_been_drawn : #Only redraw rectangle; don't make new drawing.
                self.draw_shape()

    def get_area(self):
        """
        Calculate the area of the shape
        """
        return self.length*self.height

    def draw_shape(self):
        """
        Draw the shape, starting at 0,0.

        If any old drawings exist, remove them.
        """
        self.turtle.clear() #Remove old drawings (if they exist)
        self.turtle.penup()
        self.turtle.goto(self.xstart,self.ystart)
        self.turtle.pendown()
        if self.angle == 90:
            self.turtle.goto(self.xstart+self.length,self.ystart)
            self.turtle.goto(self.xstart+self.length,self.ystart+self.height)
            self.turtle.goto(self.xstart,self.ystart+self.height)
            self.turtle.goto(self.xstart,self.ystart)
            self.turtle.penup()
            self.has_been_drawn=True
        elif self.angle == 270:
            self.turtle.goto(self.xstart-self.length,self.ystart)
            self.turtle.goto(self.xstart-self.length,self.ystart-self.height)
            self.turtle.goto(self.xstart,self.ystart-self.height)
            self.turtle.goto(self.xstart,self.ystart)
            self.turtle.penup()
            self.has_been_drawn=True
        elif self.angle == 180:
            self.turtle.goto(self.xstart-self.height,self.ystart)
            self.turtle.goto(self.xstart-self.height,self.ystart-self.length)
            self.turtle.goto(self.xstart,self.ystart-self.length)
            self.turtle.goto(self.xstart,self.ystart)
            self.turtle.penup()
            self.has_been_drawn=True
        elif self.angle < 90:
            y1 = self.ystart+math.asin(math.radians(self.angle))*self.height
            x1 = self.xstart+math.acos(math.radians(self.angle))*self.height
            self.turtle.goto(x1,y1)
            y2 = self.turtle.ycor()-math.acos(math.radians(self.angle))*self.length
            x2 = self.turtle.xcor()+math.asin(math.radians(self.angle))*self.length
            self.turtle.goto(x2,y2)
            y3 = self.turtle.ycor()-math.asin(math.radians(self.angle))*self.height
            x3 = self.turtle.xcor()-math.acos(math.radians(self.angle))*self.height
            self.turtle.goto(x3,y3)
            self.turtle.goto(self.xstart,self.ystart)
            self.turtle.penup()
            self.has_been_drawn=True
        elif self.angle > 90 and self.angle <180:
            self.angle = self.angle-90
            y1 = self.ystart+math.asin(math.radians(self.angle))*self.height
            x1 = self.xstart-math.acos(math.radians(self.angle))*self.height
            self.turtle.goto(x1,y1)
            y2 = self.turtle.ycor()-math.acos(math.radians(self.angle))*self.length
            x2 = self.turtle.xcor()-math.asin(math.radians(self.angle))*self.length
            self.turtle.goto(x2,y2)
            y3 = self.turtle.ycor()-math.asin(math.radians(self.angle))*self.height
            x3 = self.turtle.xcor()+math.acos(math.radians(self.angle))*self.height
            self.turtle.goto(x3,y3)
            self.turtle.goto(self.xstart,self.ystart)
            self.turtle.penup()
            self.has_been_drawn=True
        elif self.angle > 180 and self.angle < 270:
            self.angle = self.angle-180
            y1 = self.ystart-math.asin(math.radians(self.angle))*self.height
            x1 = self.xstart-math.acos(math.radians(self.angle))*self.height
            self.turtle.goto(x1,y1)
            y2 = self.turtle.ycor()+math.acos(math.radians(self.angle))*self.length
            x2 = self.turtle.xcor()-math.asin(math.radians(self.angle))*self.length
            self.turtle.goto(x2,y2)
            y3 = self.turtle.ycor()+math.asin(math.radians(self.angle))*self.height
            x3 = self.turtle.xcor()+math.acos(math.radians(self.angle))*self.height
            self.turtle.goto(x3,y3)
            self.turtle.goto(self.xstart,self.ystart)
            self.turtle.penup()
            self.has_been_drawn=True
        elif self.angle > 270 and self.angle < 360:
            self.angle = self.angle-270
            y1 = self.ystart-math.asin(math.radians(self.angle))*self.height
            x1 = self.xstart+math.acos(math.radians(self.angle))*self.height
            self.turtle.goto(x1,y1)
            y2 = self.turtle.ycor()+math.acos(math.radians(self.angle))*self.length
            x2 = self.turtle.xcor()+math.asin(math.radians(self.angle))*self.length
            self.turtle.goto(x2,y2)
            y3 = self.turtle.ycor()+math.asin(math.radians(self.angle))*self.height
            x3 = self.turtle.xcor()-math.acos(math.radians(self.angle))*self.height
            self.turtle.goto(x3,y3)
            self.turtle.goto(self.xstart,self.ystart)
            self.turtle.penup()
            self.has_been_drawn=True
        else:
            self.angle = self.angle-360
            self.draw_shape()
    def set_start(self,x,y):
        self.xstart=x
        self.ystart=y
        self.draw_shape()
    def set_angle(self,angle):
        self.angle = angle
        self.draw_shape()
        
        
