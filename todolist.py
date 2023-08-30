import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []
        
        self.task_title = tk.StringVar()
        
        self.create_widgets()

    def create_task(self):
        title = self.task_title.get()
        
        self.tasks.append(title)
        self.update_task_listbox()
        
        self.task_title.set("")
        
    def update_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            new_title = self.task_title.get()
            self.tasks[index] = new_title
            self.update_task_listbox()
            self.task_title.set("")
    
    def delete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_listbox()
    
    def update_task_listbox(self):
        self.listbox.delete(0, tk.END)
        for idx, title in enumerate(self.tasks):
            self.listbox.insert(tk.END, f"{idx+1}. {title}")

    def create_widgets(self):
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(padx=10, pady=10, fill=tk.BOTH)
        
        tk.Label(entry_frame, text="Task Title:", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
        tk.Entry(entry_frame, textvariable=self.task_title, font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
        
        button_frame = tk.Frame(self.root)
        button_frame.pack(padx=10, pady=5, fill=tk.BOTH)
        
        tk.Button(button_frame, text="Add Task", command=self.create_task, font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Update Task", command=self.update_task, font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Task", command=self.delete_task, font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
        
        self.listbox = tk.Listbox(self.root, font=("Helvetica", 12))
        self.listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
