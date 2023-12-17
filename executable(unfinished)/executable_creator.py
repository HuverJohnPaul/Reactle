#file that creates an executable for the program
#run this file to create the executable
#the executable will be independent of python or any other dependencies
#the executable will be made in the executable folder

#source:https://realpython.com/PyInstaller-python/

#import __main__ from PyInstaller
import PyInstaller.__main__
#import platform from sys to get the platform
from sys import platform



if platform == "win32":
    PyInstaller.__main__.run([
    'Reactle/main.py',
    '--onefile',
    '--windowed',
    '--icon=Reactle/Visualization (work in progress)/images/reactle-icon.ico',
    '--add-data=Reactle/periodictable.csv;.',
    '--add-data=Reactle/main.py;.',
    '--add-data=Reactle/database/*;.',
    '--name=Reactle'
])
elif platform == "linux":
    PyInstaller.__main__.run([
    'Reactle/executable/executable_creator_script.py',
    '--onefile',
    '--windowed',
    '--icon=Reactle/Visualization (work in progress)/images/reactle-icon.ico',
    '--add-data=Reactle/periodictable.csv:.',
    '--add-data=Reactle/main.py:.',
    '--add-data=Reactle/database/*:.',
    '--name=Reactle'
])
elif platform == "darwin":
    PyInstaller.__main__.run([
    'Reactle/executable/executable_creator_script.py',
    '--onefile',
    '--windowed',
    '--icon=Reactle/Visualization (work in progress)/images/reactle-icon.ico',
    '--add-data=Reactle/periodictable.csv:.',
    '--add-data=Reactle/main.py:.',
    '--add-data=Reactle/database/*:.',
    '--name=Reactle'
])

else:
    print("Platform not supported can only be windows, linux or mac")
