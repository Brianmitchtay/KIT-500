"""
3.4CR Stamp Function

Implements a reusable 'stamp' that can draw the author's initials at
any location on the Turtle Graphics window.
"""

__author__ = "Brian Taylor"

from turtle import Turtle


def place_stamp(stamper: Turtle, x: float, y: float, ink: str):
    """
    Draws my initials in the turtle graphics window, like a stamp.
    With the bottom left corner at (x, y).
    """
    # store the prior turtle state so we can restore it after stamping
    old_ink: str
    old_direction: float
    old_x: float
    old_y: float

    old_ink = stamper.pencolor() 
    old_direction = stamper.heading()
    old_x, old_y = stamper.pos()    

    # Change turtle speed if desired
    # (1=slowest .. 10=fastest | 0=no animation)
    stamper.speed(10)

    # Begin stamping initials at given coordinates and color
    stamper.up()
    stamper.goto(x + 50, y) # move to the bottom left corner of the stamp, then move right 50 to begin "stamping" the initials
    stamper.right(225)
    stamper.forward(100)
    stamper.down()
    stamper.color(ink)
    stamper.right(135) # pointing right to draw the top of the B
    stamper.forward(30)
    stamper.right(40) # to start the curve of the upper B bulge
    stamper.forward(5)
    stamper.right(20)
    stamper.forward(5)
    stamper.right(20)
    stamper.forward(5)
    stamper.right(20)
    stamper.forward(5)
    stamper.right(20)
    stamper.forward(5)
    stamper.right(20)
    stamper.forward(5)
    stamper.right(40)
    stamper.forward(30)
    stamper.left(180) # turn around to draw the bottom bulge of the B
    stamper.forward(30)
    stamper.right(40)
    stamper.forward(8)
    stamper.right(20)
    stamper.forward(5)
    stamper.right(20)
    stamper.forward(5)
    stamper.right(20)
    stamper.forward(5)
    stamper.right(20)
    stamper.forward(5)
    stamper.right(20)
    stamper.forward(8)
    stamper.right(40) # pointing back due left
    stamper.forward(30)
    stamper.right(90) # pointing up to draw the straight line of the B
    stamper.forward(55)
    stamper.right(90)
    stamper.up()
    stamper.forward(50) # jump over to where we’ll draw the T
    stamper.down()
    stamper.forward(60)
    stamper.right(180)
    stamper.forward(30)
    stamper.left(90)
    stamper.forward(60)
    # And that should draw us some nice turtle initials. BT

    # restore the prior turtle state
    stamper.up()
    stamper.setpos(old_x, old_y)
    stamper.color(old_ink)
    stamper.setheading(old_direction)


def main():
    t = Turtle() # The turtle graphics object

    place_stamp(t, 0, 10, "violet")
   
    place_stamp(t, 250, 250, "red")
   
    place_stamp(t, 50, -50, "blue")   


    # Avoid closing the window automatically
    t.screen.mainloop()


if __name__ == "__main__":
    main()
