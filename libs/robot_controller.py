"""
STUDENTS:
  This module contains the  Snatch3r  class.  Over the course of several
  sessions, you will implement methods in this class, including ones to:
    -- Make the robot move forward a given number of inches at a given speed
    -- Raise the arm up, make it go down
    -- XXX

  In your capstone project, you will call the methods you implement here,
  along with other methods of your own choosing.

  All the methods should be  general-purpose methods that could be used for
  a variety of tasks.  For example, suppose that you want to solve the
  following problem:
    XXX
  Here, you might implement a method YYY that YYY.  Such a method would be
  useful not only ...
"""

import ev3dev.ev3 as ev3
import sys


class Snatch3r(object):
    """ Implements methods for a Lego EV3 Snatch3r robot. """

    DEGREES_PER_INCH = 90

    def __init__(self):
        """
        Stores the motors and sensors for an EV3 Snatch3r robot
        and confirms that all of them are connected.
        """
        self.left_wheel_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_wheel_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)

        self.output_devices = [self.left_wheel_motor, self.right_wheel_motor,
                               self.arm_motor]
        self.input_devices = []
        self.devices = self.output_devices + self.input_devices

        self.assert_devices_are_connected()

    def drive_inches(self, inches, degrees_per_second):
        """ Makes the robot move the given distance (in inches) at the given
        speed (in degrees per second).  Positive distances make the robot
        move forward, negative distances make it move backward.
        """
        self.assert_devices_are_connected()

        position = inches * Snatch3r.DEGREES_PER_INCH
        brake = ev3.Motor.STOP_ACTION_BRAKE

        self.left_wheel_motor.run_to_rel_pos(position_sp=position,
                                             speed_sp=degrees_per_second,
                                             stop_action=brake)
        self.left_wheel_motor.run_to_rel_pos(position_sp=position,
                                             speed_sp=degrees_per_second,
                                             stop_action=brake)
        self.left_wheel_motor.wait(ev3.Motor.STATE_RUNNING)
        self.right_wheel_motor.wait(ev3.Motor.STATE_RUNNING)

    def assert_devices_are_connected(self):
        """
        Throws an AssertionError if any of the expected input or output devices
        are not plugged in successfully.
        """
        for device in self.devices:
            try:
                assert device.connected
            except AssertionError:
                message = "Device {} does not seem to be plugged in.\n"
                print_error(message.format(device))
                raise


def print_error(message):
    print(message, file=sys.stderr)
