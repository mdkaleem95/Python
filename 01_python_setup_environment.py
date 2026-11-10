
# Program: Python Setup and Environment Verification

import sys
import platform
from datetime import datetime

# Display Python version
print("===== PYTHON ENVIRONMENT CHECK =====")

print("Python Version:", sys.version)
print("Python Executable:", sys.executable)

# Display operating system information
print("Operating System:", platform.system())
print("OS Version:", platform.release())
print("Machine Architecture:", platform.machine())

# Display current date and time
current_time = datetime.now()

print("Current Date:", current_time.strftime("%d-%m-%Y"))
print("Current Time:", current_time.strftime("%H:%M:%S"))

# Verify basic Python execution
print("\nPython environment is configured successfully!")
