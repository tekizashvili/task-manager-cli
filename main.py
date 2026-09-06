import json
import sys
import os
from datetime import datetime

FILENAME = 'tasks.json'
COMMAND = sys.argv[1] if len(sys.argv) > 1 else None
TASK = ' '.join(sys.argv[2:])


def load_tasks() -> list:
    """Load tasks from tasks.json"""
    
    if not os.path.exists(FILENAME):
        return []
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        tasks = json.load(f)
        return tasks
    

def write_tasks(tasks: list) -> None:
    """Write tasks to a tasks.json"""
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4)
    
    
def now() -> str:
    """Returns current date and time"""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def add(task: str) -> None:
    """Add a task to the tasks.json"""
    tasks = load_tasks()
    
    # Return 1 if the tasks is empty, otherwise return the last ID + 1.
    id = len(tasks) + 1 if not tasks else tasks[-1]['id'] + 1
    
    new_task = {
                    'id': id,
                    'description': task,
                    'status': 'todo',
                    'createdAt': now(),
                    'updatedAt': ''
                }
    
    tasks.append(new_task)
    
    write_tasks(tasks)
    
    print(f'Task added successfully (ID: {id})')


def list_tasks() -> None:
    tasks = load_tasks()
    for task in tasks:
        print(task['description'] + ' -> ' + task['status'])
        

def delete_task(id: int) -> None:
    tasks = load_tasks()
    for index, task in enumerate(tasks):
        if task['id'] == id:
            tasks.pop(index)
            print(f'Task removed successfully (ID: {task['id']})')
    
    write_tasks(tasks)
    
    
def update_task(id: int, new_value: str) -> None:
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == id:
            task['description'] = new_value
            print(f"Task updated successfully (ID: {task['id']})")
    
    write_tasks(tasks)
    

def mark_as_in_progress(id) -> None:
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == id:
            task['status'] = 'in-progress'
            print(f'Task ID: {task['id']} marked as in-progress.')
            
    write_tasks(tasks)
    

def mark_as_done(id) -> None:
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == id:
            task['status'] = 'done'
            print(f'Task ID: {task['id']} marked as done.')
            
    write_tasks(tasks)

    
def main():
    command = COMMAND.lower()
    id = int(sys.argv[2])
    
    if command == 'add':
        add(TASK)
    elif command == 'list':
        list_tasks()
    elif command =='delete':
        delete_task(id)
    elif command == 'update':
        new_value = ' '.join(sys.argv[3:])
        update_task(id, new_value)
    elif command == 'mark-in-progress':
        mark_as_in_progress(id)
    elif command == 'mark-done':
        mark_as_done(id)

if __name__ == '__main__':
    while True:
        main()
        break