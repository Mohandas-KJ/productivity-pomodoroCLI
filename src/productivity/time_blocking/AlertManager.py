# This File maintains the CODE
# for user alerts

# Imports
from productivity.commons import platrad as pt
import os

def beep(frequency, tp_ms):

    #Check if Windows and Play the sound
    try:
        if pt.isWindows():
            import winsound
            winsound.Beep(frequency,tp_ms)
            return
    except Exception:
        pass

    

    #Fallback, if none is possible
    print("\a",end="",flush=True)

def vibrate(vibration):
    #Additional Vibration feature if it's on Andoid's Termux
    try:
        if pt.isTermux():
            os.system(f"termux-vibrate -d {vibration}")
            return
    except Exception:
        pass

def Alert(is_silent, tone):
    if is_silent and pt.isWindows():
        pass
    elif is_silent and pt.isLinux():
        pass
    elif is_silent and pt.isTermux():
        pass
    else:
        pass