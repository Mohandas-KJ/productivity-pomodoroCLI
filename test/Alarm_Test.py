import threading
import winsound
from test.Style import spinner_timer

tasks = ['Task 1','Task 2','Task 3']

target = len(tasks)
count = 0

def execute_task():
    global count
    if count >= target:
        return
    print(f'Current Task: {tasks.pop(0)}')
    winsound.Beep(1000,500)
    spinner_timer(10)
    count += 1
    winsound.Beep(1500,700)
    if count < target:
        threading.Timer(2, execute_task).start()

# start the repeating task once; the timer will reschedule as needed
execute_task()