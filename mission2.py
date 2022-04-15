#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from debug import test_decorator
import mission as m
import debug as d
import debug as d

m.startup()

# Crane
# Start 3-5 fingers away from the top border of home, as close to red line as possible, motor up.
@test_decorator 
def run():

    m.startup()
    
    d.straight(650)

    d.turn(90)

    d.straight(80)

    m.drag_motor(-130, -1000, 10)

    d.reset_angle(0)

    d.run_target(1000, 45)

    d.turn(100)

    d.straight(700)

    d.motor_stop()

# Code to retrieve package
def crane2():

    d.straight(400)

    d.reset_angle(0)

    m.drag_motor(-400, -1000, 10)

if __name__ == "__main__":
    
    run()
    m.onButton(Button.CENTER)
    crane2()
