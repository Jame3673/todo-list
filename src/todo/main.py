import json
from os import path
import sys
from pathlib import Path


FILE = Path("todos.json")

def load():
    if not FILE.exists():
        return[]
    return json.loads(FILE.read_text())

def save(todos):
    FILE.write_text(json.dumps(todos, indent=2))

def add(task):
    todos = load()
    new_id = 1 if not todos else todos[-1]["id"]+1
    todos.append({"id":new_id,"task":task,"done":False})
    save(todos)
    print(f"Task added")

def list_tasks():
    todos = load()
    for t in todos:
        status = "/" if t["done"] else "X"
        print(f"{t['id']}. [{status}] {t["task"]}")

def done(id_):
    todos = load()
    for t in todos:
        if t["id"] == id_:
            t["done"] = True
            save(todos)
            print("task ticked")
            return
        print("task not found")

def remove(id_):
    todos = load()
    original_len = len(todos)                       #count to know the number of tasks
    todos = [t for t in todos if t["id"] != id_]    #remove the task

    for index, t in enumerate(todos, start=1):
        t["id"] = index

    save(todos)
    if len(todos) < original_len:                   #check if the number of tasks again to make
        print("Task removed")                       #sure it removed
    else:
        print("Task not found")

def reset():
    todos = load()
    todos = []
    save(todos)
    if len(todos) == 0:
        print("list reset")
    else:
        print("<reset function got error>")


if len(sys.argv) < 2:
    print("Missing command. Usage:")
    print("  python main.py add <task>")
    print("  python main.py list")
    print("  python main.py done <id>")
    print("  python main.py remove <id>")
    sys.exit(1)




def main():
    if len(sys.argv) < 2:
        print("Commands: add, list, del, delete, res, reset")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        add(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "done":
        if len(sys.argv) < 3:
            print("Missing ID. Usage: python main.py done <id>")
        else:
            done(int(sys.argv[2]))

    elif command in ("rem", "remove"):
        if len(sys.argv) < 3:
            print('Missing ID. Usage: python main.py del <id>')
        else:
            try:
                id_to_remove = int(sys.argv[2])
            except ValueError:
                print("ID must be a number")
            else:
                remove(id_to_remove)

    elif command in ("res", "reset"):
        reset()

    else:
        print("command not found")

if __name__ == "__main__":
    main()

# Magit testing
# Magit testing 2
