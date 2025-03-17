import tkinter as tk
from tkinter import messagebox
import subprocess

def run_command(option):
    """
    Opens a terminal, runs a specific command based on the option chosen or custom input, 
    and keeps the terminal open.
    """
    commands = {
        '1': 'ls -l',  # Command for Option 1
        '2': 'pwd',    # Command for Option 2
        '3': 'date',
        '4': 'neofetch',
        '5': 'uptime -s && systemd-analyze time',
        '6': 'systemd-analyze critical-chain'   
    }

    try:
        # If option is in predefined commands, use that, otherwise treat as custom command
        if option in commands:
            cmd = commands[option]
        else:
            cmd = option  # Treat as custom command
        
        # Open a terminal, run the command, and keep the terminal open
        subprocess.run(['gnome-terminal', '--', 'bash', '-c', f'{cmd}; read -p "Press enter to continue..."'])
        # Close the tkinter window
        root.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to execute command: {str(e)}")

def search_option():
    """
    Handles command execution or search based on the input prefix.
    """
    search_query = search_entry.get().strip()
    
    if not search_query:
        update_options(options)
        return
    
    # If input starts with "~", run it directly as a custom command
    if search_query.startswith("~"):
        run_command(search_query[1:])  # Remove the "~" and execute
    else:
        # Search predefined commands
        commands = {
            '1': 'ls -l',
            '2': 'pwd',
            '3': 'date',
            '4': 'neofetch',
            '5': 'uptime -s && systemd-analyze time',
            '6': 'systemd-analyze critical-chain'
        }
        
        # Check if it's a valid option number
        if search_query in commands:
            run_command(search_query)
        else:
            # Check if it matches any command text
            matches = [opt for opt, cmd in commands.items() if search_query.lower() in cmd.lower()]
            if matches:
                if len(matches) == 1:
                    run_command(matches[0])
                else:
                    update_options({opt: options[opt] for opt in matches if opt in options})
            else:
                messagebox.showinfo("Not Found", "Command is not in the list")

def autocomplete(event):
    """
    Autocompletes the command based on partial input when Tab is pressed, ignoring "~" prefix.
    """
    current_text = search_entry.get().strip().lower()
    if not current_text or current_text.startswith("~"):
        return
    
    commands = {
        '1': 'ls -l',
        '2': 'pwd',
        '3': 'date',
        '4': 'neofetch',
        '5': 'uptime -s && systemd-analyze time',
        '6': 'systemd-analyze critical-chain'
    }
    
    # Look for matching commands
    matches = []
    for option, command in commands.items():
        if current_text in command.lower():
            matches.append(option)
    
    if len(matches) == 1:
        # If there's exactly one match, autocomplete to the option number
        search_entry.delete(0, tk.END)
        search_entry.insert(0, matches[0])
    elif len(matches) > 1:
        # If multiple matches, show options but don't change input
        update_options({opt: options[opt] for opt in matches if opt in options})
    else:
        # No matches, show all options
        update_options(options)

def update_options(options_dict):
    """
    Updates the options displayed in the tkinter window.
    """
    global current_options
    current_options = options_dict
    for widget in options_frame.winfo_children():
        widget.destroy()
    for option, command in options_dict.items():
        tk.Label(options_frame, text=f"{option}. {command}", bg="#2f2f2f", fg="#ffffff").pack()

def cancel(event):
    """
    Closes the tkinter window.
    """
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Run Command")

# Set dark mode
root.configure(bg="#2f2f2f")

# Create the popup window with options
options = {
    '1': 'ls -l',
    '2': 'pwd',
    '3': 'date',
    '4': 'neofetch',
    '5': 'boot_time',
    '6': 'boot_chain'
}

# Search box
search_entry = tk.Entry(root, bg="#3f3f3f", fg="#ffffff", insertbackground="#ffffff")
search_entry.pack()
search_entry.focus_set()  # Set focus to the search box

# Bind keys
search_entry.bind("<Return>", lambda event: search_option())
search_entry.bind("<Tab>", autocomplete)  # Add Tab key binding for autocomplete
root.bind("<Escape>", cancel)

# Add keyboard shortcuts (Ctrl+1 through Ctrl+6)
for i in range(1, 7):
    root.bind(f"<Control-Key-{i}>", lambda e, opt=str(i): run_command(opt))

# Frame for options
options_frame = tk.Frame(root, bg="#2f2f2f")
options_frame.pack()

# Display initial options
for option, command in options.items():
    tk.Label(options_frame, text=f"{option}. {command}", bg="#2f2f2f", fg="#ffffff").pack()

root.mainloop()
