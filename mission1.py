#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import mission as m

# To be able to run from this file as opposed to from main.
# Create your objects here.sd
ev3 = EV3Brick()
# Startup 
ev3.speaker.beep()
ev3.screen.print(f"{__name__} initialized...")

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
center_motor = Motor(Port.D)

# If you want to use more motors, add them here. 
#arm_motor = Motor(Port.A)

# Initialize the drive base. 
# MIGHT WANT TO CHECK TO MAKE SURE THIS IS RIGHT
# axle_track is distance between the two wheels
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

#Initiliaze sensor
ultrasonicSensor = UltrasonicSensor(Port.S1)

# settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration
robot.settings(250, 250, 360, 720)

# To be able to use sensors and control individual motors, make them parameters here
# and pass them to the run function from main.py
# This is the chicken mission
    
def run(ev3, robot, ultrasonicSensor, left_motor, right_motor):

    ev3.screen.print(f"Running {__name__} ...")

    # Put what the robot should do for this mission here.
    
    ev3 = ev3

    robot = robot

    ultrasonicSensor = ultrasonicSensor

    leftMotor = left_motor

    rightMotor = right_motor

    m.findObj(ev3, robot, ultrasonicSensor, 600)

    m.betterDrive(ev3, robot, ultrasonicSensor,None,200, False)

    robot.straight(200)

    m.betterDrive(ev3, robot, ultrasonicSensor,5,None, True)

if __name__ == "__main__":
    run(ev3, robot, ultrasonicSensor, left_motor, right_motor)
