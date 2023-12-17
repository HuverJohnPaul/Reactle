#source: using Popen https://docs.python.org/3/library/subprocess.html
#source: using os https://stackoverflow.com/questions/25701809/how-to-move-down-to-a-parent-directory-in-python


#script that is used to create the executable
#runs the main script in a new terminal

import os
import platform
import subprocess

# Determine the platform
system = platform.system()



# The command to open a new terminal and run a Python script
if system == 'Windows':
  command = 'start cmd /k python main.py'
elif system == 'Linux':
  command = 'gnome-terminal -e "python main.py"'
elif system == 'Darwin':
  command = 'open -a Terminal "python main.py"'
else:
  print('Unsupported platform must be Windows, Linux or Mac')
  exit(1)


# Run the command
subprocess.Popen(command, shell=True)
