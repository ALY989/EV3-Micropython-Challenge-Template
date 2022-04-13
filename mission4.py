#!/usr/bin/env pybricks-micropython
# 
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


m.startup()

# Bridge Mission
@test_decorator 
def run():

    m.straight(1610)
    m.turn (-720)
    m.turn(-90)
    m.straight(25)
    m.turn(220)
    m.straight(125)
   # robot.turn (-720)
    #robot.straight (1700)
    # Put what the robot should do for this mission here. 

if __name__ == "__main__":
    
    run()
