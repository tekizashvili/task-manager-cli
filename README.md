# Task Tracker

A simple command line task tracker written in Python. Tasks are stored in a
`tasks.json` file next to the script, so nothing else is needed to run it.

Project idea from [roadmap.sh](https://roadmap.sh/projects/task-tracker).

## Requirements

- Python 3.14+ (no external dependencies)

## Usage

```bash
python main.py <command> [arguments]
```

### Add a task

```bash
python main.py add "Buy groceries"
# Task added successfully (ID: 1)
```

### List tasks

```bash
python main.py list                 # all tasks
python main.py list todo            # only tasks with status "todo"
python main.py list in-progress
python main.py list done
```

### Update a task description

```bash
python main.py update 1 "Buy groceries and cook dinner"
```

### Mark a task

```bash
python main.py mark-in-progress 1
python main.py mark-done 1
```

### Delete a task

```bash
python main.py delete 1
```

## Task statuses

| Status | Meaning |
| --- | --- |
| `todo` | Default status for a new task |
| `in-progress` | Task has been started |
| `done` | Task is finished |

## How tasks are stored

Tasks live in `tasks.json` as a list of objects:

```json
{
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2026-09-06 15:38:02",
    "updatedAt": ""
}
```

The file is created automatically the first time a task is added.
