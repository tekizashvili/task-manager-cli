import json
import sys
import os
from datetime import datetime

FILENAME = 'tasks.json'
COMMAND = sys.argv[1] if len(sys.argv) > 1 else None
TASK = ' '.join(sys.argv[2:])


def load_tasks() -> dict:
    """Load tasks from tasks.json"""
    
    if not os.path.exists(FILENAME):
        return []
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        tasks = json.load(f)
        return tasks
    
    
def now():
    """Returns current date and time"""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def add(task) -> None:
    """Add a task to the tasks.json"""
    tasks = load_tasks()
    
    id = len(tasks) + 1
    
    new_task = {
                    'id': id,
                    'description': task,
                    'status': 'todo',
                    'createdAt': now(),
                    'updatedAt': ''
                }
    
    tasks.append(new_task)
    
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4)


def list_tasks() -> None:
    tasks = load_tasks()
    for task in tasks:
        print(task['description'])
            
            
def main():
    if COMMAND.lower() == 'add':
        add(TASK)
    elif COMMAND.lower() == 'list':
        list_tasks()
            
if __name__ == '__main__':
    while True:
        main()
        break