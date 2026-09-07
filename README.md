# Task Tracker

A simple command line task tracker written in Python. Tasks are kept in a
plain `tasks.json` file, and there are no third-party dependencies.

Project idea from [roadmap.sh](https://roadmap.sh/projects/task-tracker).

## Installation

Install straight from GitHub with pip:

```bash
pip install git+https://github.com/tekizashvili/task-manager-cli.git
```

That gives you a `trask` command.

```bash
$ trask add "My first task"
Task added successfully (ID: 1)
```

Requires Python 3.9 or newer.

### With uv

If you use [uv](https://docs.astral.sh/uv/), one command installs `trask` into
its own isolated environment and puts it on your PATH:

```bash
uv tool install git+https://github.com/tekizashvili/task-manager-cli.git
```

The executable is symlinked into `~/.local/bin`, and the environment itself
lives in `~/.local/share/uv/tools/trask`. If uv warns that the directory is not
on your PATH, run `uv tool update-shell` and reopen your terminal. uv also
downloads a suitable Python for you if you don't have one.

### With pipx

```bash
pipx install git+https://github.com/tekizashvili/task-manager-cli.git
```

### Updating and uninstalling

| | pip | uv | pipx |
| --- | --- | --- | --- |
| Update | `pip install --upgrade git+https://github.com/tekizashvili/task-manager-cli.git` | `uv tool upgrade trask` | `pipx upgrade trask` |
| Uninstall | `pip uninstall trask` | `uv tool uninstall trask` | `pipx uninstall trask` |

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

A full session looks like this:

```bash
$ trask add "Buy groceries"
Task added successfully (ID: 1)

$ trask add "Wash the dishes"
Task added successfully (ID: 2)

$ trask mark-in-progress 2
Task ID: 2 marked as in-progress.

$ trask list
Buy groceries -> todo
Wash the dishes -> in-progress

$ trask list todo
Buy groceries -> todo

$ trask update 1 "Buy groceries and cook dinner"
Task updated successfully (ID: 1)

$ trask mark-done 1
Task ID: 1 marked as done.

$ trask delete 2
Task removed successfully (ID: 2)
```

Use the ID printed by `add` (or shown by `list`) to update, mark or delete a
task.

## Task statuses

| Status | Meaning |
| --- | --- |
| `todo` | Default status for a new task |
| `in-progress` | Task has been started |
| `done` | Task is finished |

## Where tasks are stored

Tasks are saved to `tasks.json` **in the directory you run `trask` from**, and
the file is created on the first `add`. Run `trask` from the same place each
time to see the same list, or keep a separate list per project directory.

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

## Development

```bash
git clone https://github.com/tekizashvili/task-manager-cli.git
cd task-manager-cli
python main.py list
```

The script only uses the standard library, so `python main.py` needs no setup
at all. To work on it as an installed package instead:

```bash
pip install -e .      # or, with uv: uv sync && uv run trask list
```
