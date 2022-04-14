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
import debug as d


m.startup()

# Chicken Mission. Start anywhere facing the chicken in bottom corner.
@test_decorator 
def run():

    m.startup()

    # Put what the robot should do for this mission here.

    m.findObj(600)

    m.betterDrive(None,200, 0)

    d.straight(200)

    m.betterDrive(10,None, 0)

if __name__ == "__main__":
    
    run()
