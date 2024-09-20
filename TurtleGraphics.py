#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


    #drawPolygon(myTurtle, 5) #draws a pentagon
def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/5)
        
    #drawPolygon(myTurtle, 8) #draws an octogon
def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/8)
        
    #drawPolygon(myTurtle, 3) #draws a triangle
def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(3)
        
        
def fillCorner(alice, corner):
    #draw big square
    drawSquare(alice, 100)
     #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    if corner == 1:
        alice. begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
        
        
    elif corner == 2:
        alice.forward(50)
        alice. begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
        
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

# squaresInSquares(myTurtle, 5) #draws 5 concentric squares
def drawSquare(alice, size):
    for _ in range(4):
        alice.forward(size)
        alice.right(90)

def fillCorner(alice, corner):
    # Draw big square
    drawSquare(alice, 100)

    if corner == 1:
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()

    elif corner == 2:
        alice.penup()
        alice.setpos(0, -50)  # Move to bottom-left corner (inside the large square)
        alice.pendown()
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()

def main():
    myTurtle = turtle.Turtle()

    fillCorner(myTurtle, 2)  # Filling bottom-left corner
    turtle.done()
    
# squaresInSquares(myTurtle, 3) #draws 3 concentric squares

def drawSquare(alice, size):
    alice.penup()
    alice.goto(-size/2, size/2)  # Start drawing from top-left corner
    alice.pendown()
    
    for _ in range(4):
        alice.forward(size)
        alice.right(90)

def squaresInSquares(alice, n):
    max_size = 200  # Size of the largest square
    size_step = max_size / n  # Step size between squares

    for i in range(n):
        size = max_size - (i * size_step)  # Decrease size for each new square
        drawSquare(alice, size)

def main():
    myTurtle = turtle.Turtle()

    squaresInSquares(myTurtle, 3)  # Draws 3 concentric squares
    turtle.done()


main()
def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    #drawPolygon(myTurtle, 3)
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()

