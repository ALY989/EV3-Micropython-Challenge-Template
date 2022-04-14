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
    d.turn(-100)
    d.straight(410)
    d.turn(50)
    d.straight(-35)
    # d.reset_angle(180)
    # d.run_time(-10000, 3000)
    # m.drag_motor(-15, -10000, 30)
    # d.run_until_stalled(10000)
    d.straight(10)
    m.bang(10000, 10)
    # d.run_time(-10000, 10000)
    # m.drag_motor(40, -10000, 40)
    d.straight(-10)
    d.turn(-90)
    d.straight(100)
    d.turn(60)
    d.straight(-10)
    m.bang(10000,10)


if __name__ == "__main__":
    
    run() 
