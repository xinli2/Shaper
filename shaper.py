###
###
### Author: Xin Li
### Description: shaper.py
### Program should have the capability to print out different
### three different shapes: An hourglass, a plumbbob, or a
### house. Below is a  table that shows examples of each of
### these shapes.
###
shape = input('Enter shape to display:\n')
arrow = input('Enter arrow character:\n')
height = int(input('Enter row-area height:\n'))
def main ():
    if shape == 'hourglass':
        hourglass (arrow)
    elif shape == 'plumbbob':
        plumbbob (arrow, height)
    elif shape == 'house':
        house (arrow, height)

def line (height):
    i = 0
    while i < height :
        print('|---------|')
        i += 1
def up_arrow (arrow):
    i = 0
    while i < 6:
        print(' '*(5-i),arrow*(2*i+1),' '*(5-i),sep='')
        i += 1

def down_arrow (arrow):
    i = 0
    while i < 6:
        print(' '*i,arrow*(11-2*i),' '*i,sep='')
        i += 1

def hourglass(arrow):
    line(height)
    down_arrow(arrow)
    up_arrow(arrow)
    line(height)
def plumbbob (arrow, height):
    up_arrow(arrow)
    line(height)
    down_arrow(arrow)

def house(arrow, height):
    up_arrow(arrow)
    line(height)
print()
main()
