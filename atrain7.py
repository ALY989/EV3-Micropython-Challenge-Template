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

m.startup()

# Train. Place angled toward the train. No consistent way to place it, just eyeball it.
@test_decorator
def run():

    m.startup()
    
    d.straight(800)
    d.turn(80)
    d.straight(650)

    d.turn(-180)
    d.straight(1000)
    d.turn(90)
    d.straight(450)


if __name__ == "__main__":
    
    run()
