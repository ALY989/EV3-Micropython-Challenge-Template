#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import time

# This file contains all of the inbuilt functions for the robot wrapped in the test_decorator.

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

# data = DataLog("Time", "Line", "Distance", "Angle", extension="txt")

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

def format_tuple(value):
    return "(" + ",".join(repr(v) for v in value) + ")"

# Decorator that prints the currently running function to the screen.
def test_decorator(func):
    def inner1(*args, **kwargs):
        
        name = func.__name__
        
        # Showing user which function is currently executing with what arguments on which line
        ev3.screen.print("%s %s Start" % (name, format_tuple(args))) 
        # data.log(time.time(),"%s %s %d %d" % (name, format_tuple(args), robot.distance(),robot.angle()))
		
		# getting the returned value
        returned_value = func(*args, **kwargs)
        
        # Showing user that the function has been executed and the arguments that were passed into it
        ev3.screen.print("%s %s Done" % (name, format_tuple(args)))
		
		# returning the value to the original frame
        return returned_value
		
    return inner1


def show_dist(func):
    def inner1(*args, **kwargs):

        ev3.screen.print(ultrasonicSensor.distance())

        returned_value = func(*args, **kwargs)

        return returned_value
    
    return inner1


@test_decorator
def ev3_print(printable):

    ev3.screen.print(printable)

@test_decorator
def ev3_beep():

    ev3.speaker.beep()

@test_decorator
def straight(distance):

    robot.straight(distance)

@test_decorator
def turn(angle):

    robot.turn(angle)

@test_decorator
def drive(speed, angle):

    robot.drive(speed, angle)

@show_dist
def ultrasonic_drive(speed, angle):

    robot.drive(speed, angle)

@test_decorator
def run_target(speed, target_angle):

    center_motor.run_target(speed, target_angle)

@test_decorator
def reset_angle(angle):

    center_motor.reset_angle(angle)

@test_decorator
def motor_stop():

    center_motor.stop()

@test_decorator
def run_until_stalled(speed):

    center_motor.run_until_stalled(speed)

@test_decorator
def hold():

    center_motor.hold()

@test_decorator
def run_time(speed, milliseconds):

    center_motor.run_time(speed, milliseconds)