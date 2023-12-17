#source: using Popen https://docs.python.org/3/library/subprocess.html
#source: using os https://stackoverflow.com/questions/25701809/how-to-move-down-to-a-parent-directory-in-python


#script that is used to create the executable
#runs the main script in a new terminal

import os
import platform
import subprocess

# Determine if the application is a script file or a frozen exe
if getattr(sys, 'frozen', False):
   application_path = os.path.dirname(sys.executable)
elif __file__:
   application_path = os.path.dirname(__file__)
# The command to open a new terminal and run a Python script
if platform.system() == 'Windows':
  command = f'start cmd /k python {os.path.join(application_path, "main.py")}'
elif platform.system() == 'Linux':
  command = f'gnome-terminal -e "python {os.path.join(application_path, "main.py")}"'
elif platform.system() == 'Darwin':
  command = f'open -a Terminal "python {os.path.join(application_path, "main.py")}"'
else:
 print('Unsupported platform must be Windows, Linux or Mac')
 exit(1)


# Run the command
subprocess.Popen(command, shell=True)
