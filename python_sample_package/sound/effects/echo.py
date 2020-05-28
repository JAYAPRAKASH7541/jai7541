"""The module echo

This is the "echo" module, providing some useless functions!
"""


def func1():
    print("echo function func1 has been called!")


def func2():
    print("echo function func2 has been called!")


def func3():
    print("echo function func3 has been called!")

def print_echo():
    from .reverse import reverse_sound
    #from sound.filters.equalizer import print_equa
    from ..filters.equalizer import print_equa
    print("echo echo!")
    reverse_sound()
    print_equa()
print("Module echo.py has been loaded!")

print_echo()