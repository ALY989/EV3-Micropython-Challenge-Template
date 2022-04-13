#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import time

import debug as d
from debug import test_decorator
# Create your objects here.
ev3 = EV3Brick()

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
tiny_font = Font(size=16)
ev3.screen.set_font(tiny_font)


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

# Initialize any sensors you want here by uncommenting and changing the port.

#touch_sensor = TouchSensor(Port.S1)
# To use touch sensor, pass it in as a parameter in the run function for whichever mission needs it.
# Example usage:
# def run(robot, touch_sensor):
#     # drive forward until the touch sensor is pressed
#     while !touch_sensor.pressed():
#         robot.drive(100, 0)
#     robot.stop()

#color_sensor = ColorSensor(Port.S2)
# To use color sensor, pass it in as a parameter in the run function for whichever mission needs it.
# Example usage:
# def run(robot, color_sensor):
#     # drive forward until the color sensor sees the color you want
#     while color_sensor.color() != Color.BLACK:
#         robot.drive(100, 0)
#     robot.stop()

#ultrasonic_sensor = UltrasonicSensor(Port.S3)
# To use ultrasonic sensor, pass it in as a parameter in the run function for whichever mission needs it.
# Example usage:
# def run(robot, ultrasonic_sensor):
#     # drive forward until the ultrasonic sensor sees the distance you want
#     while ultrasonic_sensor.distance() > 10:
#         robot.drive(100, 0)
#     robot.stop()

#gyro_sensor = GyroSensor(Port.S4)
# To use gyro sensor, pass it in as a parameter in the run function for whichever mission needs it.
# Example usage:
# def run(robot, gyro_sensor):
#     # turn until the gyro sensor sees the angle you want
#     while gyro_sensor.angle() < 10:
#         robot.drive(0, 100)
#     robot.stop()

# This is the global module for all the missions. Functions that can be used for all missions go here.

# Prints a message. Used at the beginning of each file to know that the file has been imported.
@test_decorator
def startup():
    d.ev3_beep()
    d.ev3_print("%s Imported" %__name__)

# "Drags" the motor across a surface. Iterations is how many times you want the motor to make sure that it is touching the surface.
@test_decorator
def drag_motor(distance, speed, iterations=3):

    for i in range(iterations):

        distance_per_move = distance/iterations

        d.run_until_stalled(speed)

        d.hold()

        d.straight(distance_per_move)

        i += 1

@test_decorator
def findObj(distance, ev3=ev3, robot=robot, ultrasonicSensor=ultrasonicSensor):

    while ultrasonicSensor.distance() > distance: 

        d.ev3_print(ultrasonicSensor.distance())

        d.drive(0,120)

    return True

# Arc is the second parameter of drive.
@test_decorator
def betterDrive(seconds=None, distance=None, arc=0, ev3=ev3, robot=robot, ultrasonicSensor=ultrasonicSensor):

    if distance is not None and arc == 0:

        while ultrasonicSensor.distance() >= distance:

            d.ev3_print(ultrasonicSensor.distance())

            d.drive(10000,0)

        return True

    elif distance is not None and arc != 0:

        while ultrasonicSensor.distance() >= distance:

            d.ev3_print(ultrasonicSensor.distance())

            d.drive(10000,arc)

        return True

    elif seconds is not None and arc != 0:
        
        start_time = time.time()

        current_time = time.time()

        while current_time - start_time < seconds:

            d.ev3_print(ultrasonicSensor.distance())

            d.drive(100,arc)

            current_time = time.time()

        return True

    elif seconds is not None and arc == 0:

        start_time = time.time()

        curent_time = time.time()

        while current_time - start_time < seconds:

            d.ev3_print(ultrasonicSensor.distance())

            d.drive(100,arc)

            current_time = time.time()

        return True

    else: 

        return True

@test_decorator
def onButton(button):
    while (not button in ev3.buttons.pressed()):
        wait(10)

# Example to wait until center button is pressed:
# waitUntilButton(Button.CENTER)

@test_decorator
def show_dist():
    while True:
        ev3.screen.print(ultrasonicSensor.distance())
