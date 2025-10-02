import os
class Task:
    def __init__(self,work,done):
        self.work = work
        self.done = done
l = []
def save():
    with open("tasks.txt", "w") as o:
        for i in l:
            o.write(i.work + "^" + i.done + "\n")
def load():
    os.system("cls")
    print("To-Do List")
    for index, i in enumerate(l):
        print(f"{index+1}. {i.work} {i.done}")
with open("tasks.txt", "r") as file:
    while((x:=file.readline().strip()) != ""):
        l.append(Task(x.split("^")[0],x.split("^")[1]))
    
while True:
    load()
    while True:
        i = input("Write a to add tasks, d to delete one,m to mark them or c to clear whole list\n")
        if((i != "a" and i!= "d" and i!= "m" and i!="c") or ((i == "d" or i == "m") and len(l) == 0)):
            print("INVALID INPUT")
        else:
            break       
    match i:
        case "a":
            t = input("Write the task\n")
            l.append(Task(t,"[ ]"))
        case "d":
            while True:
                t = input("Write the task number\n")
                if(not t.isdigit() or not 1<=int(t)<=len(l)):
                    print("INVALID INPUT")
                else:
                    break
            del l[int(t)-1]
        case "m":
            while True:
                w = input("Write the task number than after a gap write u for undone and d for done\n").split()
                if (len(w) != 2 or not w[0].isdigit() or not 1<=int(w[0])<=len(l) or (w[1]!="u" and w[1]!="d")):
                    print("INVALID INPUT")
                else:
                    t = w[0]
                    c = w[1]
                    break
            match c:
                case "u":
                    l[int(t)-1].done = "[ ]"      
                case "d":
                    l[int(t)-1].done = "[x]"
        case "c":
            l = []
    save()
                
