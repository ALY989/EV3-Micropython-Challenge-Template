#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time

# To be able to use sensors and control individual motors, make them parameters here
# and pass them to the run function from main.py
# This is the chicken mission

def run(ev3, robot, ultrasonicSensor):
    # Put what the robot should do for this mission here.
    ev3 = ev3

    robot = robot

    ultrasonicSensor = ultrasonicSensor

    while True:
        if ultrasonicSensor.distance():
            
            ev3.screen.print(ultrasonicSensor.distance())

            findObj(ev3, robot, ultrasonicSensor)
        
        else: 

            break

    robot.turn(10)

    robot.straight(380)

    start_time = time.time()
    
    current_time = time.time()
    
    while start_time - current_time < 5:
        
        robot.drive(100, 60) 

        current_time = time.time()
      

def findObj(ev3, robot, ultrasonicSensor):

    while ultrasonicSensor.distance() > 550: 

        ev3.screen.print(ultrasonicSensor.distance())

        robot.drive(0,120)

def chargeObj(ev3, robot, ultrasonicSensor):

    while ultrasonicSensor.distance() <= 550: 

        ev3.screen.print(ultrasonicSensor.distance())

        robot.drive(10000,0)