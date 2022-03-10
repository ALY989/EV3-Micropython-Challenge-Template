#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# To be able to use sensors and control individual motors, make them parameters here
# and pass them to the run function from main.py
def run(robot):
    robot.straight(150)
    robot.turn(-45)
    robot.straight(350)
    robot.turn(45)
    arm.run(100)
    robot.straight(100)
    robot.straight(-20)
    robot.turn(45)
    robot.straight(20)
    robot.turn(25)
    robot.straight(200)
    pass