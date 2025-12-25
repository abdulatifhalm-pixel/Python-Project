# ============================================================
#  TO-DO LIST PRO - GUI VERSION 💻
#  Author: Levi / Streamlined by AI Assistant
# ============================================================

import json
import os
from tkinter import messagebox

import customtkinter as ctk

DATA_FILE = "tasks.json"


# --- Helper Functions ---
def generate_new_id(tasks):
    """Generates a unique ID."""
    if not tasks: return 1
    max_id = max(task.get('id', 0) for task in tasks)
    return max_id + 1


def load_tasks():
    """Loads tasks safely."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                if isinstance(data, list): return data
        except (json.JSONDecodeError, IOError):
            print("Error loading tasks. Starting fresh.")
    return []


def save_tasks(tasks):
    """Saves tasks safely."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
    except IOError as e:
        messagebox.showerror("Save Error", f"Could not save tasks: {e}")


# --- App Class ---
class ToDoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("✨ To-Do List Pro ✨")
        self.geometry("500x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.tasks = load_tasks(
            # UI Layout
            ctk.CTkLabel(self, text="📝 To-Do List Pro", font=("Segoe UI", 28, "bold")).pack(pady=20)

        self.entry_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.entry_frame.pack(pady=10, padx=10, fill="x")

        self.task_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Enter new task...", height=40)
        self.task_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.task_entry.bind('<Return>', lambda e: self.add_task())
        ctk.CTkButton(self.entry_frame, text="Add Task", width=100, command=self.add_task).pack(side="right")

        self.task_frame = ctk.CTkScrollableFrame(self, width=450, height=400, fg_color="#1a1a1a")
        self.task_frame.pack(pady=15, padx=10, fill="both", expand=True)

        self.bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_frame.pack(pady=10)

        ctk.CTkButton(self.bottom_frame, text="🧹 Clear Done Tasks", width=120, fg_color="orange",
                      command=self.clear_done_tasks).grid(row=0, column=0, padx=10)
        ctk.CTkButton(self.bottom_frame, text="💾 Save & Exit", width=120, fg_color="green",
                      command=self.save_and_exit).grid(row=0, column=1, padx=10)

        self.display_tasks()

        # --- Methods ---

    def display_tasks(self):
        """Renders tasks, clearing previous display."""
        for widget in self.task_frame.winfo_children(): widget.destroy()

        for task in self.tasks:
            row = ctk.CTkFrame(self.task_frame, fg_color="#333333", corner_radius=8)
            row.pack(fill="x", pady=4, padx=5)

            font_style = ("Segoe UI", 14, "overstrike") if task["done"] else ("Segoe UI", 14)
            text_color = "gray" if task["done"] else "white"

            check_var = ctk.BooleanVar(value=task["done"])
            checkbox = ctk.CTkCheckBox(row, text=task["title"], variable=check_var,
                                       font=font_style, text_color=text_color,
                                       command=lambda tid=task['id']: self.toggle_done(tid))
            checkbox.pack(side="left", padx=10, pady=10)

            ctk.CTkButton(row, text="❌", width=30, fg_color="red",
                          command=lambda tid=task['id']: self.delete_task(tid)).pack(side="right", padx=10)

    def add_task(self):
        title = self.task_entry.get().strip()
        if not title:
            messagebox.showwarning("Warning", "Please enter a task.")
            return

        new_task = {"id": generate_new_id(self.tasks), "title": title, "done": False}
        self.tasks.append(new_task)
        save_tasks(self.tasks)
        self.task_entry.delete(0, "end")
        self.display_tasks()

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        save_tasks(self.tasks)
        self.display_tasks()

    def toggle_done(self, task_id):
        # Find task by ID and flip status
        for task in self.tasks:
            if task['id'] == task_id:
                task["done"] = not task["done"]
                break
        save_tasks(self.tasks)
        self.display_tasks()  # Redraw to update visual styling

    def clear_done_tasks(self):
        if messagebox.askyesno("Confirm Clear Done", "Clear all *completed* tasks?"):
            self.tasks = [task for task in self.tasks if not task["done"]]
            save_tasks(self.tasks)
            self.display_tasks()

    def save_and_exit(self):
        save_tasks(self.tasks)
        self.destroy()


# --- Run ---
if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()
