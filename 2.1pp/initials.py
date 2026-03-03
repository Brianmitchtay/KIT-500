"""
KIT101 2.1PP Turtle Graphics

Turtle Graphics task to draw the author's initials.
Some of the code below has been _over_ commented to help
you understand what is happening.
"""

__author__ = "Brian Taylor"

import turtle as t


def main():
    # Change turtle speed if desired
    # (1=slowest .. 10=fastest | 0=no animation)
    t.speed(8)

    # Draw your initials below, remembering to use painter.penup() to
    # move without drawing a line...
    t.up()
    t.right(225)
    t.forward(100)
    t.down()
    t.color("blue")
    t.right(135) # pointing right to draw the top of the B
    t.forward(30)
    t.right(40) # to start the curve of the upper B bulge
    t.forward(5)
    t.right(20)
    t.forward(5)
    t.right(20)
    t.forward(5)
    t.right(20)
    t.forward(5)
    t.right(20)
    t.forward(5)
    t.right(20)
    t.forward(5)
    t.right(40)
    t.forward(30)
    t.left(180) # turn around to draw the bottom bulge of the B
    t.forward(30)
    t.right(40)
    t.forward(8)
    t.right(20)
    t.forward(5)
    t.right(20)
    t.forward(5)
    t.right(20)
    t.forward(5)
    t.right(20)
    t.forward(5)
    t.right(20)
    t.forward(8)
    t.right(40) # pointing back due left
    t.forward(30)
    t.right(90) # pointing up to draw the straight line of the B
    t.forward(55)
    t.right(90)
    t.up()
    t.forward(50) # jump over to where we’ll draw the T
    t.down()
    t.forward(60)
    t.right(180)
    t.forward(30)
    t.left(90)
    t.forward(60)

    # And that should draw us some nice turtle initials. BT




    # Avoid closing the window automatically
    t.mainloop()


if __name__ == "__main__":
    main()
