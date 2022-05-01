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

# Billboard Destruction
# Place five fingers away from right border with the arm downward, but not touching the ground. Move it as close as possible to the red border.
@test_decorator
def run():

    m.startup()

    d.straight(590)
    d.straight(-600)

if __name__ == "__main__":
    
    run()
