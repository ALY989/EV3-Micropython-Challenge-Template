#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# The bulk of main.py has been moved here to consolidate things. (Intializing the objects is no longer necessary to do in main)

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

def waitUntilButton(button):
    while (not button in ev3.buttons.pressed()):
        wait(10)

# Example to wait until center button is pressed:
# waitUntilButton(Button.CENTER)

# This is the global module for all the missions. Functions that can be used for all missions go here.

# Prints a message. Used at the beginning of each file to know that the file has been imported.
def startup():
    ev3.speaker.beep()
    ev3.screen.print("%s Importing..." %__name__)

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
