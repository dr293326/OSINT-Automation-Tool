import subprocess
from tkinter import *

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter

from src.HTTPServer import HTTPServer
from src.SystemToolsManager import exec_command


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # subprocess.run(["print_hi(\'PyCharm\')"])
    # subprocess.run(["ls", "-l"])
    # subprocess.run(["pwd"])
    # subprocess.run(["traceroute", "127.0.0.1"]
    # zwrotka = exec_command('traceroute', '127.0.0.1')
    # print(zwrotka)

    # root = Tk()
    # canvas = Canvas(root, height=500, width=1000)
    # canvas.pack()
    #
    # button = Button(root, text="Hello World")
    # button.pack()
    # root.mainloop()

    server = HTTPServer()
    server.open_report()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
