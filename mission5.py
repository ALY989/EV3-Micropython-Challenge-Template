#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


m.startup()

@test_decorator
def run():

    #hammer.run_target(1000,70)
    m.straight(1300)
    m.turn(-90)
    m.straight(310)
    m.turn(50)
    m.reset_angle(180)
    m.run_target(1000,90)

if __name__ == "__main__":
    
    run()
