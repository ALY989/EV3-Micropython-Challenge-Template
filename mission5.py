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

# Plane and Truck Mission

def run(robot):
    robot.straight(1100)
    robot.turn(90)
    robot.straight(330)
    robot.turn(50)
    hammer= Motor(Port.D)
    hammer.run_target(1000,90)
    hammer.run_target(1000,0)