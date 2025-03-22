import time
import datetime

def printer(task):
    
    if task['status'] == "todo":
        col = "\033[91m" # red
    elif task['status'] == "progress":
        col = "\033[94m" # blue
    elif task['status'] == "done":
        col = "\033[92m" # green
    else:
        col= ""
    # \033[0m is the end sequence, not putting in there will color everything
    txt = f"ID: {task['id']}\nDescription: \033[93m{task['desc']}\033[0m\nCreated At: {task['created']}\nUpdated At: {task['updated']}\n"
    if col!="":
        txt = txt + f"Status: {col}{task['status']}\033[0m"
    else:
        txt = txt + f"Status: {task['status']}"
    return txt
   
def get_current_time():
    """Returns the current date and time in the format 'HH:MM PM, YYYY-MM-DD'."""
    return datetime.datetime.now().strftime(" %I:%M %p , %Y-%m-%d")

# write a more efficient version of this which doesnt automatically look for the max, but from 1 till max looks for missing ints
def generate_id(task_file):
    if len(task_file)<1:
        return 1
    else:
        return max((int(t["id"]) for t in task_file),default=0)+1

def add(task_file,ips):
    
    value = ips[2]
    nt = {
        "id":generate_id(task_file),
        "desc":value,
        "status":"todo",
        "created":get_current_time(),
        "updated":"-",
    }
    task_file.append(nt)
    print("task added successfully")

def listf(task_file,ips):
    if not task_file:
        print("there are no tasks")
    else:
        if len(ips)<=2:
            filtered_list = task_file
        else:
            st = ips[2].lower()
            if st!="todo" and st!="progress" and st!="done":
                raise ValueError("enter one choice from todo,progress or done")
            filtered_list = [task for task in task_file if task["status"]==st]
        if len(filtered_list)==0:
            print("there are no such tasks")
        else:        
            print("********************************")
            for task in filtered_list:
                print(printer(task))
                print("********************************")

def deleter(task_file,ips):
    if not task_file:
        print("there are no tasks")
    else:
        try:
            task_id = int(ips[2])
        except:
            raise IndexError("enter a number only")
        to_remove = next((task for task in task_file if task["id"]==task_id),None) # check conversion on this
        if to_remove:
            task_file.remove(to_remove)
            print("task was removed")
        else:
            print("task with id not found")
         
def update(task_file,ips):
    if not task_file:
        print("there are no tasks")
    else:
        try:
            task_id = int(ips[2])
        except:
            raise IndexError("enter a number only")
        value = ips[3]
        to_update = next((task for task in task_file if task["id"]==task_id),None) # check conversion on this
        if to_update:
            to_update["desc"] = value
            to_update["updated"] = get_current_time()
            print("Task updated successfully.")
        else:
            print("task with id not found")
    
def marker(task_file,ips,opt):
    if not task_file:
        print("there are no tasks")
    else:
        try:
            task_id = int(ips[2])
        except:
            raise IndexError("enter a number only")
        value = opt
        to_update = next((task for task in task_file if task["id"]==task_id),None) # check conversion on this
        if to_update:
            to_update["status"] = value
            to_update["updated"] = get_current_time()
            print("Task updated successfully.")
        else:
            print("task with id not found")
    
        
        
        
        
