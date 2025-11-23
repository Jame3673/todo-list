# TO DO terminal app

- This is a simple project make by Python
- For short, it a terminal app can create a list tasks
- I'm an freshman so if someone saw this project I hope you guys will like it

## Features

This is all feature the app can do:
1. add -> add new task
2. list -> list all task
3. done -> tick the task
4. remove -> remove a task
5. reset -> clear the list

## How to use

NOTE: I don't know how to call the app with short name at anywhere so it will have a little inconvenient

Command:

- python main.py add "TASK" --> python main.py add "buy milk"

- python main.py list

- python main.py done ID --> the ID start from 1. For instance, python main.py done 1

- python main.py remove ID --> the ID start from 1. For instance, python main.py remove 1
- python main.py rem ID --> for short

- python main.py reset
- python main.py res --> for short


# CAFE-TABLE
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