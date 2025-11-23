# TODO-LIST
This is a cli app use to create a list of works

## Feature
Command:
- "add" to add new task
- "list" to show a whole list
- "remove" or "rem" + ID(from 1 to n) to delete a task
- "reset" or "res" to clear whole list

## installation

from source code
```bash
git clone https://github.com/Jame3673/todo-list
cd todo-list
pip install .
```

## Uasge
```bash
# Add order
todo add

# Show order
todo list

# Delete order with ID
todo remove <id>
todo rem <id>

# Delete table
todo reset
todo res
```