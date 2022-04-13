#!/usr/bin/env pybricks-micropython
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
# Truck and Plane
@test_decorator
def run():

    m.startup()


    #hammer.run_target(1000,70)
    d.straight(1300)
    d.turn(-90)
    d.straight(310)
    d.turn(50)
    d.reset_angle(180)
    d.run_target(1000,90)

if __name__ == "__main__":
    
    run()
