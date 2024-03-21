from graphics import *
def createwindow():
    #creates a window when called by main
    #needs graphics.py
    win = GraphWin(width = 200, height = 200) #creates the actual window
    win.setCoords(0, 0, 10, 10) #this sets window coords. Bottom-left is 0,0 top right is 10,10
    #replace this with code to display images when figure out how
    testsquare = Rectangle(Point(1, 1), Point(9,9)) #this will create a rectangle. will remove when done testing
    testsquare.draw(win) #draw it
    win.getMouse() #gets the mouse? will pause before closing.
    return