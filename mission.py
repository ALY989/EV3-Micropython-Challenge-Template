#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import inspect
from inspect import currentframe, getframeinfo

# This is the global class for all the missions. Functions that can be used for all missions go here.Ks
def findObj(ev3, robot, ultrasonicSensor, distance):

    while ultrasonicSensor.distance() > distance: 

        ev3.screen.print(ultrasonicSensor.distance())

        robot.drive(0,120)

    return True

def betterDrive(ev3, robot, ultrasonicSensor, seconds=None, distance=None, arc=0):

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

def format_tuple(value):
    return "(" + ",".join(repr(v) for v in value) + ")"

def test_decorator(func):
    def inner1(*args, **kwargs):
        
        name = func.__name__
        print(name)
        print(inspect.stack())
        linenumber = inspect.currentframe().f_back.f_lineno
        
        # Showing user which function is currently executing with what arguments on which line
        ev3.screen.print("Line {}: Executing: {}{}" %(linenumber, name, format_tuple(args))) 
		
		# getting the returned value
        returned_value = func(*args, **kwargs)
        
        # Showing user that the function has been executed and the arguments that were passed into it
        ev3.screen.print("Executed: {}{} on line: {}" %(name, format_tuple(args), linenumber))
		
		# returning the value to the original frame
        return returned_value
		
    return inner1

@test_decorator
def test_straight(robot, distance):

    robot.straight(distance)
