#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# Create your objects here.
ev3 = EV3Brick()
# Startup
ev3.speaker.beep()
ev3.screen.print("%s Imported..." %__name__)

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

# This is the global class for all the missions. Functions that can be used for all missions go here.
# Prints a message. Used at the beginning of each file to know that the file has been imported.
def startup():
    ev3.speaker.beep()
    ev3.screen.print("%s Imported..." %__name__)

def format_tuple(value):
    return "(" + ",".join(repr(v) for v in value) + ")"

def test_decorator(func):
    def inner1(*args, **kwargs):
        
        name = func.__name__
        
        # Showing user which function is currently executing with what arguments on which line
        ev3.screen.print("Executing: %s %s" % (name, format_tuple(args))) 
		
		# getting the returned value
        returned_value = func(*args, **kwargs)
        
        # Showing user that the function has been executed and the arguments that were passed into it
        ev3.screen.print("Executed: %s %s" % (name, format_tuple(args)))
		
		# returning the value to the original frame
        return returned_value
		
    return inner1

@test_decorator
def findObj(distance, ev3=ev3, robot=robot, ultrasonicSensor=ultrasonicSensor):

    while ultrasonicSensor.distance() > distance: 

        ev3.screen.print(ultrasonicSensor.distance())

        robot.drive(0,120)

    return True

# Arc is the second parameter of drive.
@test_decorator
def betterDrive(seconds=None, distance=None, arc=0, ev3=ev3, robot=robot, ultrasonicSensor=ultrasonicSensor):

    if distance is not None and arc == 0:

        while ultrasonicSensor.distance() >= distance:

            ev3.screen.print(ultrasonicSensor.distance())

            robot.drive(10000,0)

        return True

    elif distance is not None and arc != 0:

        while ultrasonicSensor.distance() >= distance:

            ev3.screen.print(ultrasonicSensor.distance())

            robot.drive(10000,arc)

        return True

    elif seconds is not None and arc != 0:
        
        start_time = time.time()

        current_time = time.time()

        while current_time - start_time < seconds:

            ev3.screen.print(ultrasonicSensor.distance())

            robot.drive(100,arc)

            current_time = time.time()

        return True

    elif seconds is not None and arc == 0:

        start_time = time.time()

        curent_time = time.time()

        while current_time - start_time < seconds:

            ev3.screen.print(ultrasonicSensor.distance())

            robot.drive(100,arc)

            current_time = time.time()

        return True

    else: 

        return True

@test_decorator
def straight(distance):

    robot.straight(distance)

@test_decorator
def turn(angle):

    robot.turn(angle)

@test_decorator
def run_target(speed, target_angle):

    central_motor.run_target(speed, target_angle)

@test_decorator
def reset_angle(angle):

    central_motor.reset_angle(angle)
