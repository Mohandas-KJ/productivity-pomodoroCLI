def getTotal(no_of_t,t_per_task):
    Total_min = no_of_t * t_per_task
    Hour = Total_min // 60
    Minute = Total_min % 60
    return Hour,Minute
