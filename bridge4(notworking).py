#!/usr/bin/env pybricks-micropython
# 
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

# Bridge Mission
@test_decorator 
def run():

    m.startup()

    d.straight(1300)
    d.turn(90)
    d.straight(25)
    d.run_target(1000, 90)
    d.straight (-25)
    d.run_target(1000, 0)
    d.turn(90)
    d.straight(1300)
    


if __name__ == "__main__":
    
    run()
