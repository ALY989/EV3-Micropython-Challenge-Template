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

@test_decorator 
def run():

    m.startup()

    30 degree angle

    d.straight(1210)

    d.turn(90)

    d.straight(200)

    d.turn(90)

    d.run_until_stalled(-1000)

    d.reset_angle(0)

    d.run_target(1000, 35)

    d.straight(260)

    d.straight(-260)

    d.turn(90)

    d.straight(50)

    d.turn(90)

    d.straight(260)

    d.straight(-260)

    d.turn(90)

    # Put what the robot should do for this mission here. 

if __name__ == "__main__":

    run()
