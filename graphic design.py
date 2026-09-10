from turtle import *
from colorsys import *

tracer(10)
bgcolor('black')
pensize(2)
h = 2
goto(0, 120)

for j in range(26):
    h = j / 26
    color(hsv_to_rgb(h,1,1))
    for i in range(100):
        circle(i*0.6, 70)
        right(120)
    right(360 / 36)

done()
