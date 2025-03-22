# learn more about exceptions, and especially how they propagate and stuff, i want to ensure the save_changes only hits
# when there were absolutely no errors
import os
import sys
import json
import task_functions as tm
# dumps(dict to json) loads(json to dict)

# ensures the program was entered correctly in the terminal
def arg_len_checker():
    if(len(sys.argv)<2):
        raise ValueError("please enter an argument along with the pyogram name, eg list, add etc")
        
def check_open():   
    # initialise an empty task list
    task_file=[]
    ## checking if file exists
    # if it doesnt exist make a new one and add the [] to it
    file_exists = os.path.exists("tasks.json")
    if file_exists == False:
        print("file didnt exist, was created")
        with open("tasks.json", 'w') as f:
            json.dump(task_file,f)

    # loading the json file from the program
    try:
        with open('tasks.json') as f:
            task_file = json.load(f)
    except:
        raise IOError("failed to read the file, maybe file is in incorrect format")
    return task_file
    
def execute(task_file):
    func_map = {
        "add":tm.add,
        "delete":tm.deleter,
        "update":tm.update,
        "list":tm.listf,
        "mark-done":tm.marker,
        "mark-progress":tm.marker
    }
    cmd = sys.argv[1].lower()
    if cmd not in func_map:
        raise ValueError("wrong function name entered")
        
    if len(sys.argv)==2 and cmd!="list":
        raise IndexError("you didnt give the required arguments")
    
    if cmd == "add" or cmd == "delete" or cmd=="update" or cmd=="list":
        args = (task_file,sys.argv)
    elif cmd=="mark-done":
        args = (task_file,sys.argv,"done")
    elif cmd=="mark-progress":
        args = (task_file,sys.argv,"progress")
    try:
        func_map[cmd](*args)
    except Exception as e:
        print(f"Error executing the function:{e}")


def save_changes(task_file):
    if not task_file or isinstance(task_file[0],dict):
        with open('tasks.json','w') as f:
            json.dump(task_file,f)
    else:
        raise ValueError("task_file was in the wrong format and hence not saved")
   
def main():
    try:
        arg_len_checker()
        task_file=check_open()
        execute(task_file)
    except Exception as e:
        print(e)
    else:
        save_changes(task_file)
        
if __name__ == "__main__":
    main()