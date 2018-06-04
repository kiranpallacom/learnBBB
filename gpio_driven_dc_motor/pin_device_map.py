#!/usr/bin/env python

# No gpio for some pins when using 'universal' io
gpio_devices = {
    'P9_22' : '/sys/devices/platform/ocp/44e07000.gpio/gpio/gpio2',
    'P9_21' : '/sys/devices/platform/ocp/44e07000.gpio/gpio/gpio3',
    'P9_31' : '',
    'P9_29' : '',
    'P9_14' : '/sys/devices/platform/ocp/4804c000.gpio/gpio/gpio50',
    'P9_16' : '/sys/devices/platform/ocp/4804c000.gpio/gpio/gpio51',
    'P8_36' : '',
    'P8_34' : '',
    'P8_19' : '/sys/devices/platform/ocp/44e07000.gpio/gpio/gpio22',
    'P8_13' : '/sys/devices/platform/ocp/44e07000.gpio/gpio/gpio23',
    'P8_45' : '',
    'P8_46' : ''
}

from os import open, write, close
import os
from subprocess import call

# Configure pin as gpio and write value (direction: 'out')
def gpio_write(pin, value):
    call(['config-pin', pin, 'gpio'])
    f_gdir = open(gpio_devices[pin]+'/direction', os.O_WRONLY)
    f_gval = open(gpio_devices[pin]+'/value', os.O_WRONLY)
    write(f_gdir, 'out')
    write(f_gval, value)
    close(f_gdir)
    close(f_gval)
