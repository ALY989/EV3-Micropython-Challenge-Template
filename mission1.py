#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time, mission

# To be able to use sensors and control individual motors, make them parameters here
# and pass them to the run function from main.py
# This is the chicken mission

class mission1(mission):

    def run(self, ev3, robot, ultrasonicSensor, left_motor, right_motor):
        # Put what the robot should do for this mission here.
        ev3 = ev3

        robot = robot

        ultrasonicSensor = ultrasonicSensor

        leftMotor = left_motor

        rightMotor = right_motor

        findObj(ev3, robot, ultrasonicSensor)

        betterDrive(ev3, robot, ultrasonicSensor,None,200, False)

        betterDrive(ev3, robot, ultrasonicSensor,5,None, True)
