#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
from debug import test_decorator
import mission as m
import debug as d


m.startup()

# Chicken Mission. Start facing the chicken in bottom corner.
@test_decorator 
def run():

    m.startup()

    m.betterDrive(10000, None, 150)

    d.straight(200)

    m.betterDrive(10000, 10)

if __name__ == "__main__":
    
    run()
