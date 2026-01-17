# This file Contains the essentials for OS Detection
import platform
import os, subprocess
from productivity.commons import config

def isWindows():
    if platform.system() == "Windows":
        return True
    else:
        return False
    
def isLinux():
    if platform.system() == "Linux":
        return True
    else:
        return False

def isTermux():
    if "ANDROID_ROOT" in os.environ or "com.termux" in os.environ.get("TERM",""):
        return True
    else:
        return False

def isMac():
    if platform.system() == "Darwin":
        return True
    else:
        return False

def Clear_Screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def Termux_api_support():
    try:
        out  = subprocess.run(
            ["termux-info"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        ).stdout

        config.IS_TERMUX = True
        config.TERMUX_API_SUPPORTED = "Termux:API" in out
    
    except FileNotFoundError:
        config.IS_TERMUX = False

