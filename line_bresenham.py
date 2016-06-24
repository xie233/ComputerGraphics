from graphics import *
import time
def MidpointLine(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    d=2*dy-dx
    incrE=2*dy
    incrNE=2*(dy-dx)
    x=x1
    y=y1
    win = GraphWin('Brasenham Line', 600, 480)
    PutPixle(win, x, y)
    while x < x2:
        if (d<= 0):
            d=d+incrE
            x=x+1
        else:
            d=d+incrNE
            x=x+1
            y=y+1
        time.sleep(0.01)
        PutPixle(win, x, y)
def PutPixle(win, x, y):
    """ Plot A Pixle In The Windows At Point (x, y) """
    pt = Point(x,y)
    pt.draw(win)


def main():
    x1 = int(input("Enter Start X: "))
    y1 = int(input("Enter Start Y: "))
    x2 = int(input("Enter End X: "))
    y2 = int(input("Enter End Y: "))

    MidpointLine(x1, y1, x2, y2)

if __name__ == "__main__":

    main()

