#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This is the global class for all the missions. functions that can be used for all missions go here.
class mission:
    
    def findObj(ev3, robot, ultrasonicSensor):

        while ultrasonicSensor.distance() > 600: 

            ev3.screen.print(ultrasonicSensor.distance())

            robot.drive(0,120)

        return True

    def betterDrive(ev3, robot, ultrasonicSensor, seconds=None, distance=None, arc=False):

        if distance is not None and arc==False:

            while ultrasonicSensor.distance() >= distance:

                ev3.screen.print(ultrasonicSensor.distance())

                robot.drive(10000,0)

            return True

        elif distance is not None and arc==True:

            while ultrasonicSensor.distance() >= distance:

                ev3.screen.print(ultrasonicSensor.distance())

                robot.drive(10000,60)

            return True

        elif seconds is not None and arc is True:
            
            start_time = time.time()

            curent_time = time.time()

            while current_time - start_time < seconds:

                ev3.screen.print(ultrasonicSensor.distance())

                robot.drive(100,60)

                current_time = time.time()

            return True

        elif seconds is not None and arc is False:

            start_time = time.time()

            curent_time = time.time()

            while current_time - start_time < seconds:

                ev3.screen.print(ultrasonicSensor.distance())

                robot.drive(100,60)

                current_time = time.time()

            return True

        else: 

            return True
