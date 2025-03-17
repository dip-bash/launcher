# Command Launcher GUI

A simple Python GUI application built with Tkinter that allows users to run predefined terminal commands through a graphical interface with search functionality.

## Features

### Predefined Command Execution
- Provides a list of predefined commands (e.g., `ls -l`, `pwd`, `date`, `neofetch`, etc.) mapped to option numbers (1-6).
- Users can execute these commands by typing the option number and pressing Enter.

### Custom Command Support
- Allows execution of arbitrary custom commands by prefixing them with "~" (e.g., `~whoami` runs "whoami" in the terminal).
- Without the "~" prefix, non-matching inputs trigger a "Command is not in the list" message.

### Terminal Integration
- Executes commands in a new `gnome-terminal` window using `subprocess`, keeping the terminal open after execution for result viewing (`read -p "Press enter to continue..."`).

### Autocomplete Functionality
- Supports basic autocompletion with the Tab key:
  - **Single match**: Completes to the option number (e.g., "neo" → "4" for "neofetch").
  - **Multiple matches**: Filters the displayed options list without altering the input.
  - Ignores "~" prefixed inputs to avoid interfering with custom commands.

### Keyboard Shortcuts
- Offers quick access to predefined commands via `Ctrl+1` through `Ctrl+6` hotkeys, directly executing the corresponding command.

### Interactive GUI
- Built with Tkinter, featuring a dark-themed interface (background: `#2f2f2f`, text: `#ffffff`).
- Displays a searchable list of command options that updates based on user input (e.g., filtering on Tab with multiple matches).
- Includes an entry field with focus on startup for immediate typing.

### Error Handling
- Catches and displays execution errors in a messagebox (e.g., if a command fails or is invalid).
- Provides feedback for unrecognized commands via a "Not Found" messagebox.

### Exit Functionality
- Closes the application with the Escape key, enhancing usability.
## Prerequisites

- Python 3.x
- Tkinter (usually comes with Python)
- GNOME Terminal (for Linux systems)
- Required Python modules:
  - tkinter
  - subprocess

## To modify the available commands, edit the commands dictionary in run_command() and the options dictionary in the main code:
```python
commands = {
    '1': 'ls -l',
    '2': 'pwd',
    '3': 'date',
    '4': 'neofetch'
}

options = {
    '1': 'Run ls -l',
    '2': 'Run pwd',
    '3': 'Run date',
    '4': 'neofetch'
}




