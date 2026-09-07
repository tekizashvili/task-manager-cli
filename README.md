# Task Tracker

A simple command line task tracker written in Python. Tasks are kept in a
plain `tasks.json` file, and there are no third-party dependencies.

Project idea from [roadmap.sh](https://roadmap.sh/projects/task-tracker).

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/) (optional, but the easiest way to install)

## Installation

First get the code:

```bash
git clone git@github.com:tekizashvili/task-manager-cli.git
cd task-manager-cli
```

Then pick one of the following.

### Option 1: install the `trask` command (recommended)

```bash
uv tool install .
```

This puts a `trask` command on your PATH, so you can track tasks from any
directory. If uv warns that the install directory is not on your PATH, run:

```bash
uv tool update-shell
```

### Option 2: run it inside the project

```bash
uv sync
uv run trask list
```

`uv sync` creates a `.venv` with the right Python version and installs the
project into it. Prefix every command with `uv run`.

### Option 3: no installation at all

The script only uses the standard library, so you can run the file directly:

```bash
python main.py list
```

Anywhere below you see `trask`, `python main.py` works the same way.

You can also install it with pip if you prefer:

```bash
pip install .
```

## Usage

```bash
trask <command> [arguments]
```

| Command | What it does |
| --- | --- |
| `add <description>` | Add a new task |
| `list` | List every task |
| `list <status>` | List only tasks with that status |
| `update <id> <description>` | Change a task's description |
| `mark-in-progress <id>` | Mark a task as in-progress |
| `mark-done <id>` | Mark a task as done |
| `delete <id>` | Delete a task |

### Add a task

```bash
$ trask add "Buy groceries"
Task added successfully (ID: 1)
```

### List tasks

```bash
$ trask list
Buy groceries -> todo
Wash the dishes -> in-progress

$ trask list todo
Buy groceries -> todo
```

### Update a task

Use the ID that `add` printed:

```bash
$ trask update 1 "Buy groceries and cook dinner"
Task updated successfully (ID: 1)
```

### Mark a task as in-progress or done

```bash
$ trask mark-in-progress 1
Task ID: 1 marked as in-progress.

$ trask mark-done 1
Task ID: 1 marked as done.
```

### Delete a task

```bash
$ trask delete 1
Task removed successfully (ID: 1)
```

## Task statuses

| Status | Meaning |
| --- | --- |
| `todo` | Default status for a new task |
| `in-progress` | Task has been started |
| `done` | Task is finished |

## Where tasks are stored

Tasks are saved to `tasks.json` **in the directory you run the command from**,
and the file is created on the first `add`. Run `trask` from the same place
each time to see the same list, or keep a separate list per project directory.

Each task looks like this:

```json
{
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2026-09-06 15:38:02",
    "updatedAt": ""
}
```

## Notes

Commands expect valid input: give `add` and `update` a description, and give
`update`, `delete` and the `mark-` commands an existing task ID. Input
validation and friendlier error messages are not implemented yet.
