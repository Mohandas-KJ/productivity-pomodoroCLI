# This Script is to start the CLI Tool

# Imports
import sys
import subprocess

# Command template
cmd = [sys.executable,"src/pomodoro.py"]

# Check if argument is passed
if len(sys.argv) > 1:
    cmd.extend(sys.argv[1:])  # Pass it to the file

subprocess.run(cmd)