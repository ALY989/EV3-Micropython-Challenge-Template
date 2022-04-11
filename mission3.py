#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# To be able to run from this file as opposed to from main.
# Create your objects here.
ev3 = EV3Brick()
# Startup  
ev3.speaker.beep()
ev3.screen.print("%s initialized..." %__name__)

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
def run(ev3, robot):

    ev3.screen.print("Running %s ..." %__name__)

    # Put what the robot should do for this mission here. 
    pass

if __name__ == "__main__":
    run(ev3, robot)
