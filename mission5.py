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
# Truck and Plane. Start three fingers away from top border, as close to red line as possible, motor up.
@test_decorator
def run():

    m.startup()

    #hammer.run_target(1000,70)
    d.straight(1200)
    d.turn(-95)
    d.straight(400)
    d.turn(55)
    d.straight(-30)
    d.reset_angle(180)
    d.run_until_stalled(-1000)

if __name__ == "__main__":
    
    run() 
