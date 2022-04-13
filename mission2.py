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
import debug as d

m.startup()

# Crane
@test_decorator 
def run():

    m.startup()


    m.startup()
    
    d.straight(600)

    d.turn(90)

    d.straight(60)

    m.drag_motor(-130, -1000, 4)

    d.reset_angle(0)

    d.run_target(1000, 45)

    d.turn(100)

    d.straight(650)

    d.motor_stop()

# Code to retrieve package
def crane2():

    d.straight(300)

    d.reset_angle(0)

    m.drag_motor(-300, -1000, 2)

if __name__ == "__main__":
    
    run()
    m.onButton(Button.CENTER)
    crane2()
