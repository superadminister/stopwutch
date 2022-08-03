"""
Binary Conversions, using formats as modes for converting tool dependency.
"""

from tkinter import (Tk, Button, Label)
from string import Formatter
import ping3
import time


class Gui(object):

    ping = ping3
    tk = Tk()
    skeleton_press = Button()
    skeleton_hello_world = Label()
    skeleton_state = Label()

    def __abs__(self, number):
        return abs(number)

    def __str__(self):
        return 'True'

    def __init__(self, command):
        self.command = command
        self.skeleton_hello_world.config(
            text='Hello World'
        )
        self.skeleton_hello_world.place(x=10, y=10)
        self.skeleton_press.config(
            text='Press!', command=self.display_state
        )
        self.skeleton_press.place(x=10, y=40)
        self.tk.geometry('300x300')
        self.tk.title('world')
        self.tk.mainloop()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def display_state(self):
        self.skeleton_state.config(
            text=f'True, Status is: {self.command} \n'
                 f'{self.ping.verbose_ping(dest_addr=self.command, count=0, interval=0)}')
        self.skeleton_state.place(x=10, y=100)
        print(self.__dir__())


class ReGui:
    def __init__(self, *data, **attrs):
        self.a, self.b = attrs['num1'], attrs['num2']
        self.data = data


class DeGui(ReGui):
    def __add__(self, *other):
        self.add = other

        return self.data + self.add, self.a, self.b


class StrFormatter(Formatter):

    def format(self, __format_string, *args, **kwargs):

        settings = []
        if kwargs['len'] is True:
            length = len(__format_string)
            settings.append(length)

        if kwargs['type'] is True:
            types = type(__format_string)
            settings.append(types)

        settings.append((__format_string, args))

        return settings


count = 0
while True:
    zero = 0
    minute = 'minute'
    count = count + 1

    for x in range(0, 60):
        time.sleep(59)
        if x < 10:
            print(f'{minute, count}:{zero}{x}')
        elif x > 9:
            print(f'{minute, count}:{x}')
