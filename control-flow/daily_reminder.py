#Enter a task description
task = input ("Enter your task: ")
priority = input ("Priority (high/medium/low): ")
time_bound = input ("Is it time-bound? (yes/no):")

if time_bound == "yes":
        print("Reminder: ", end = "")
else:
        print("Note: ", end = "")

match priority:   
    case "high":
        print (task, "is a high priority task that requires immeddiate attention today!")
    case "medium":
        print (task, "is a medium priority task, so you can put it aside for now.")
    case "low" :
        print(task, "is a low priority task. Consider completing it when you have free time.")
    