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
# Truck mission. Start 3 fingers away from top border of home, as close to the red line as possible
@test_decorator 
def run():

    m.startup()

    d.straight(1210)

    d.turn(-97)

    d.straight(250)

    d.turn(-97)

    d.run_until_stalled(-1000)

    d.reset_angle(0)

    d.run_target(1000, 45)

    d.straight(270)

    d.straight(-230)

    d.turn(97)

    d.run_until_stalled(1000)

    d.straight(150)

    d.turn(-115)

    d.run_until_stalled(-1000)

    d.reset_angle(0)

    d.run_target(1000, 35)

    d.straight(300)

    d.straight(-300)

    d.turn(97)

    # Put what the robot should do for this mission here. 

if __name__ == "__main__":

    run()
