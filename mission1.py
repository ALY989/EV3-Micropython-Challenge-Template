#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
from mission import test_decorator
import mission as m


m.startup()

# This is the chicken mission
@test_decorator 
def run():

    # Put what the robot should do for this mission here.

    m.findObj(600)

    m.betterDrive(None,200, False)

    d.straight(200)

    m.betterDrive(5,None, True)

if __name__ == "__main__":
    
    run()
