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

m.startup()

# Crane
@test_decorator 
def run():

    m.straight(600)

    m.turn(90)

    m.straight(10)

    m.run_target(1000, -90)

    m.straight(-100)

    m.run_target(1000, 90)

    m.turn(90)

    m.straight(600)

if __name__ == "__main__":
    
    run()
