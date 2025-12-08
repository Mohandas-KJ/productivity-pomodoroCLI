import Productivity.Commons.SpinnerTimer as stimer
import winsound,threading
import Productivity.Time_Blocking.MicroTasker as mt

count = 0

def execute_task(tasks,per_task):
    global count
    target = len(tasks)

    if count > target:
        return
    
    temp = tasks.pop(0)

    winsound.Beep(1000,500)
    print(f'Current Tasks: {temp}')
    stimer.spintimer(per_task)
    print(f'Completed: {temp}')
    winsound.Beep(1500,700)

    if count < target:
        threading.Timer(2,execute_task,args=(tasks,per_task)).start()
