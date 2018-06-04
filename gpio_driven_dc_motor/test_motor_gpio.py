#!/usr/bin/env python

# Test: test_moto_gpio
# Run DC motor forward, reverse, coast & brake with GPIO toggles (and no PWM)
# Motor is controlled using DRV-8333 H-Bridge Logic
# xIN1 | xIN2 | FUNCTION
#   0  |  0   | Coast
#   0  |  1   | Reverse
#   1  |  0   | Forward
#   1  |  1   | Brake

import pin_device_map as dev
from time import sleep

# Connect DRV8333 pins xIN1 to P9_22 & xIN2 to P9_22
# Change below pins to use different GPIOs
pin_1 = 'P9_22'
pin_2 = 'P9_21'

def motor_gpio_forward():
    dev.gpio_write(pin_1, '1')
    dev.gpio_write(pin_2, '0')

def motor_gpio_reverse():
    dev.gpio_write(pin_1, '0')
    dev.gpio_write(pin_2, '1')

def motor_gpio_coast():
    dev.gpio_write(pin_1, '0')
    dev.gpio_write(pin_2, '0')

def motor_gpio_brake():
    dev.gpio_write(pin_1, '1')
    dev.gpio_write(pin_2, '1')

# Simple Test
motor_gpio_forward()
sleep(10)
motor_gpio_brake()
sleep(3)
motor_gpio_reverse()
sleep(10)
motor_gpio_coast()
