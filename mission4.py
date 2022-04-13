#!/usr/bin/env pybricks-micropython
# 
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from mission import test_decorator
import mission as m
import debug as d


m.startup()

# Bridge Mission
@test_decorator 
def run():

    m.startup()

    d.straight(1610)
    d.turn (-720)
    d.turn(-90)
    d.straight(25)
    d.turn(220)
    d.straight(125)
   # robot.turn (-720)
    #robot.straight (1700)

if __name__ == "__main__":
    
    run()
