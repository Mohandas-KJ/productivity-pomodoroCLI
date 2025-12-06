#Task Segregation Sample Script
no_of_tasks = int(input('Enter the number of Tasks: '))
time_per_tasks = int(input('Time per Task (min): '))

if time_per_tasks < 2:
    print('Should be greater than 2')

Total_min = no_of_tasks * time_per_tasks
print(f'Time: {Total_min // 60} hours {Total_min % 60} Minutes')