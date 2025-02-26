# Command Launcher GUI

A simple Python GUI application built with Tkinter that allows users to run predefined terminal commands through a graphical interface with search functionality.

## Features

- Dark-themed interface
- Searchable command list
- Keyboard navigation (Enter to select/search, Esc to exit)
- Opens commands in a new terminal window

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




