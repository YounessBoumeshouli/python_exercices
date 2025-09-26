import tkinter as tk
from tkinter import messagebox
from PythonProject.mini_projet.Controllers.taches_controller import *
from tkcalendar import DateEntry

tc = taskController
data = {}

def add_task():
    task = entry.get().strip()
    print(task)

    if task:
        todo_list.insert(tk.END,task )
        entry.delete(0, tk.END)
        data["title"] = task
        showDescription()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")
def add_description():
    description = description_entry.get().strip()
    if description:
        todo_list.insert(tk.END,description )
        entry.delete(0, tk.END)
        data["description"] = description

        showStartDate()
    else:
        messagebox.showwarning("Input Error", "Please enter a description of task.")

def add_start():
    start = start_entry.get_date()
    if start:
        todo_list.insert(tk.END,start )
        entry.delete(0, tk.END)
        data["start"] = start
        showDeadline()
    else:
        messagebox.showwarning("Input Error", "Please enter a description of task.")
def add_deadline():
    deadline = deadline_entry.get_date()
    if deadline:
        todo_list.insert(tk.END,deadline )
        entry.delete(0, tk.END)
        data["deadline"] = deadline
        tc.addTask(data)
    else:
        messagebox.showwarning("Input Error", "Please enter a description of task.")


def showDescription():
    print("hello")
    description_entry.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=10)
    add_btn_description = tk.Button(root, text="Add description", command=add_description)
    add_btn_description.grid(row=1, column=3, padx=10)
def showStartDate():
    start_entry.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=10)
    add_btn_description = tk.Button(root, text="start at", command=add_start)
    add_btn_description.grid(row=2, column=3, padx=10)
def showDeadline():
    deadline_entry.grid(row=3, column=0, columnspan=3, sticky="ew", padx=10, pady=10)
    add_btn_description = tk.Button(root, text="End at", command=add_deadline)
    add_btn_description.grid(row=3, column=3, padx=10)
def move_task(source, target):
    selected = source.curselection()
    if selected:
        task = source.get(selected[0])
        source.delete(selected[0])
        target.insert(tk.END, task)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to move.")

def delete_task(listbox):
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

root = tk.Tk()
root.title("Three-List To-Do App")
root.geometry("600x400")

entry = tk.Entry(root, font=("Arial", 12))
entry.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

add_btn = tk.Button(root, text="Add to To-Do", command=add_task)
add_btn.grid(row=0, column=3, padx=10)
description_entry = tk.Entry(root, font=("Arial", 12))
start_entry =  DateEntry(root,  width=12, background="darkblue", foreground="white", borderwidth=2)
deadline_entry = DateEntry(root,  width=12, background="darkblue", foreground="white", borderwidth=2)

tk.Label(root, text="To Do", font=("Arial", 12, "bold")).grid(row=1, column=0)
tk.Label(root, text="Doing", font=("Arial", 12, "bold")).grid(row=1, column=1)
tk.Label(root, text="Done", font=("Arial", 12, "bold")).grid(row=1, column=2)

todo_list = tk.Listbox(root, selectbackground="lightblue")
todo_list.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

doing_list = tk.Listbox(root, selectbackground="lightgreen")
doing_list.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

done_list = tk.Listbox(root, selectbackground="lightgray")
done_list.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)

tk.Button(root, text="→", command=lambda: move_task(todo_list, doing_list)).grid(row=3, column=0)
tk.Button(root, text="→", command=lambda: move_task(doing_list, done_list)).grid(row=3, column=1)

tk.Button(root, text="Delete", command=lambda: delete_task(todo_list)).grid(row=4, column=0, pady=5)
tk.Button(root, text="Delete", command=lambda: delete_task(doing_list)).grid(row=4, column=1, pady=5)
tk.Button(root, text="Delete", command=lambda: delete_task(done_list)).grid(row=4, column=2, pady=5)

for col in range(3):
    root.grid_columnconfigure(col, weight=1)
root.grid_rowconfigure(2, weight=1)

existed_tasks = selectTasks()
print("hhh")
print(existed_tasks)
for task in existed_tasks :
        print(task)
        todo_list.insert(tk.END, task)