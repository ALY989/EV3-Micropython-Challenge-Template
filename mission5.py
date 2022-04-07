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
    hammer= Motor(Port.D)
    #hammer.run_target(1000,70)
    robot.straight(1300)
    robot.turn(-90)
    robot.straight(310)
    robot.turn(50)
    hammer.reset_angle(180)
    hammer.run_target(1000,90)
