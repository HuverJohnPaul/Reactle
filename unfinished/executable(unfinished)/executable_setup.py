# import the necessary modules from cx_Freeze
from cx_Freeze import setup, Executable

#import os to check if the periodictable.csv file is in the same directory as this file
import os

# Specify the required additional files to be included in the final package (all required files that are not .py files)
# first element in the tuple is the path of the file the second element is the name you want the file to have in the package

#checks what directory the file is run from and sets the additional files accordingly
if os.path.exists("periodictable.csv"):
    additional_files = [("periodictable.csv", "periodictable.csv")]
elif os.path.exists("../Reactle/periodictable.csv"):
    additional_files = [("../Reactle/periodictable.csv", "periodictable.csv")]
else:
    print("Error: periodictable.csv not found")

setup(
    name="Reactle",
    version="1.0",
    description="Reactle is a chemistry text based game where users have to guess the elements that comprise a reaction given the numerical values of the reaction and hints from previous guesses",
    author="Group 6, ChE 120 2023; lead coder: John-Paul Huver",
    options={"build_exe": {"include_files": additional_files,"zip_include_packages": "*"}},
    executables=[Executable("../Reactle/main.py")]
)
# Run this file to create the executable by running the command "python executable_setup.py build" in the terminal and it will create a folder called "build" in the same directory as this file. Inside the build folder there will be a file called Reactle.exe which is the executable.