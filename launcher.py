import tkinter as tk
from tkinter import messagebox
import subprocess

def run_command(option):
    """
    Opens a terminal, runs a specific command.
    """
    commands = {
        '1': 'ls -l',  # Commands for Options
        '2': 'pwd',    
        '3': 'date',
        '4': 'neofetch'    
    }

    try:
        # Open a terminal, run the command, and keep the terminal open
        subprocess.run(['gnome-terminal', '--', 'bash', '-c', commands[option] + '; read -p "Press enter to continue..."'])
        # Close the tkinter window
        root.destroy()
    except KeyError:
        messagebox.showerror("Invalid Option", "Please choose a valid option.")

def search_option():
    """
    Searches for an option based on the search query.
    """
    search_query = search_entry.get()
    filtered_options = {option: command for option, command in options.items() if search_query.lower() in command.lower()}
    update_options(filtered_options)

def update_options(options):
    """
    Updates the options displayed in the tkinter window.
    """
    global current_options
    current_options = options
    for widget in options_frame.winfo_children():
        widget.destroy()
    for option, command in options.items():
        tk.Label(options_frame, text=f"{option}. {command}", bg="#2f2f2f", fg="#ffffff").pack()
    if len(options) == 1:
        search_entry.bind("<Return>", lambda event: run_command(next(iter(options))))

def cancel(event):
    """
    Closes the tkinter window.
    """
    root.destroy()

root = tk.Tk()
root.title("Run Command")

# Set dark mode
root.configure(bg="#2f2f2f")

# Create the popup window with options
options = {
    '1': 'Run ls -l',
    '2': 'Run pwd',
    '3': 'Run date',
    '4': 'neofetch'
}

# Search box
search_entry = tk.Entry(root, bg="#3f3f3f", fg="#ffffff", insertbackground="#ffffff")
search_entry.pack()
search_entry.focus_set()  # Set focus to the search box

# Bind the Enter key to the search_option function
search_entry.bind("<Return>", lambda event: search_option())

# Bind the Esc key to the cancel function
root.bind("<Escape>", cancel)

# Frame for options
options_frame = tk.Frame(root, bg="#2f2f2f")
options_frame.pack()

# Display options
for option, command in options.items():
    tk.Label(options_frame, text=f"{option}. {command}", bg="#2f2f2f", fg="#ffffff").pack()

root.mainloop()
