# 🐍 Python Concepts I've Wrestled With (And Somehow Survived)

Welcome to my personal Python battlefield : a collection of concepts I've battled, debugged, cried over, and eventually tamed during my transition from bug hunter (System Test Engineer) to bug creator (Python Developer).

This repo is basically my therapy session in code form. Each file/folder is a hard-won victory against confusion, late-night Stack Overflow dives, and that one time I thought `==` and `is` were best friends forever.

⭐ Star if you've also lost sleep over scope rules. Fork if you want to fix my mistakes.

### `Mimikyu says Hi 👋`

```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠿⠋⠛⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠉⠉⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠃⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⠉⠀⠀⠀⠀     ⣠⣴⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠱⣄⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣤⣤⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠋⣠⣦⣟⣻⣦    ⣼⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢶⠒⠛⠉⠉⠀⠀⠀⠀⠀⣹⣿⣿⣿⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⡏⠿⣎⣿⠏⠹   ⠟⠿⠟⠁⠀⠀⠀⠀⠀⢀⣴⣶⣶⣤⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣷⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⡆⠛⠷⠟⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣀⡠⠜⠛⠛⢯⣙⠿⣿⣷⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⡿⠃⠀⠀⡀⠀⣠⠴⠊⠁⠀⠀⠀⠀⠀⠈⠓⢽⣿⣿⣷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠘⢿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⠈⠻⢿⠿⠛⠡⣄⠀⢠⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡀⠀⠀⠀⠀⠀⠸⣿⣤⣤⡀⠀⠀⠀⣤⣲⣖⠢⡀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⣀⣤⢄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⡀⠀⠀⠀⠀⠈⠉⠻⣿⣤⣤⣿⣶⠆⣩⠿⠅⠀⠀⡜⠁⠀⠀⠀⢀⡤⠖⠋⠀⣾⠈⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠑⠦⢀⠀⠀⠀⠀⠙⠻⣋⣩⣭⣶⣞⠋⠀⢀⡞⠀⠀⠀⣠⠖⠉⠀⠀⠀⠀⢻⡀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠐⢲⡤⠀⠈⠉⠉⠁⣀⡠⠴⠋⠀⠀⡠⠎⠁⠀⢀⡠⠄⠀⠀⠸⡀⢸⠄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢙⡏⠉⠉⠉⠁⠀⠀⠀⣠⠞⠁⢀⣤⠞⣉⠄⠀⢀⡠⢔⡳⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⢰⠁⠀⠀⠛⠐⠋⣀⠤⣒⡭⠒⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⠀⠀⠀⠀⠈⢦⡀⠀⢠⠴⠟⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⣾⣇⠀⠀⠀⠀⠈⢷⠀⠀⢀⡴⠋⠀⠀⠈⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⢸⡗⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⢧⠀⢏⠀⠈⢳⡶⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⣳⠄⠀⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⡞⢁⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠻⣗⣒⠒⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⠤⠖⠛⣛⡻⢶⣄⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣄⣀⣀⣈⣱⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠉⠉⠉⠉⠉⠗⠚⠹⣤⡖⠊⠉⠻⠿⠋⠑⢦⣄⣴⠿⣽⣿⠒⠲⣤⣤⣀⣈⡷⠤⠤⠵⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
```

## Repository Structure

The tree below lists the learning resources and supporting files. Regular-expression screenshots are grouped for readability.

```text
Python_Concepts/
│
├── 001_WorkFlows/
│   ├── 001_Git_WorkFlows/
│   │   ├── git_pull
│   │   └── git_push
│   └── 002_Python_Workflows/
│       ├── README.md
│       └── 001_UV_workflow/
│           └── 001_UV_WorkFlow.md
│
├── 002_REgeX_Concepts/
│   ├── Regex_Comcepts.ipynb
│   └── Screenshot (...).png (31 reference images)
│
├── 003_DSA_Concepts/
│   ├── DSA_Python_By_Elshad_Udemy.ipynb
│   └── DSA_Udacity_from_Google.ipynb
│
├── 004_Turtle_Concepts/
│   ├── Free_Draw.py
│   ├── Square_Pattern.py
│   ├── Turtle_Byte_Design.py
│   ├── Turtle_Playgound_1.py
│   └── Tutle_Concepts.ipynb
│
├── 005_Socratica_Python/
│   ├── Python_Socratica.ipynb
│   ├── Python_Socratica_2.ipynb
│   └── socratica.db
│
├── 006_Code_Visualization_Concepts/
│   ├── README.md
│   └── 001_Code2flow/
│       └── Code2Flow_Usage_Summary.md
│
├── 007_DataBases/
│   └── 001_SQL_Socratica/
│       ├── README.md
│       ├── SQL_Socratica.md
│       ├── image.png
│       └── image-1.png
│
├── Excel_stuff.ipynb
├── FIle_handling.ipynb
├── Mouse_&_Keyboard_Simulation.ipynb
├── PDF.ipynb
├── PyQt-GUI.ipynb
├── Strings_Stuff.ipynb
├── tkinter_arena.ipynb
├── git_pull
├── git_push
└── README.md
```

Folder and file names above match the repository, including existing capitalization and spelling.

## Topic Guide

| Area | Contents |
| --- | --- |
| [Development workflows](./001_WorkFlows/) | Bash helpers for Git operations and a [Python workflow guide](./001_WorkFlows/002_Python_Workflows/README.md) for uv-based project and dependency management. |
| [Regular expressions](./002_REgeX_Concepts/) | A Python regex notebook and supporting reference screenshots. |
| [Data structures and algorithms](./003_DSA_Concepts/) | Course-based notebooks covering topics such as recursion, linked lists, stacks, searching, and hashing. |
| [Turtle graphics](./004_Turtle_Concepts/) | A notebook and standalone scripts for drawing, patterns, and keyboard-controlled graphics. |
| [Socratica Python](./005_Socratica_Python/) | Python study notebooks and a companion SQLite database file. |
| [Code visualization](./006_Code_Visualization_Concepts/README.md) | Guidance for generating call graphs with code2flow and rendering them with Graphviz. |
| [SQL and databases](./007_DataBases/001_SQL_Socratica/README.md) | Socratica-based SQL notes, PostgreSQL setup guidance, query examples, and supporting images. |

### Root-Level Notebooks

| Notebook | Focus |
| --- | --- |
| [Excel_stuff.ipynb](./Excel_stuff.ipynb) | Spreadsheet manipulation and examples using pandas, openpyxl, and XlsxWriter. |
| [FIle_handling.ipynb](./FIle_handling.ipynb) | File and directory handling, pathlib, JSON, and folder-structure visualization. |
| [Mouse_&_Keyboard_Simulation.ipynb](./Mouse_%26_Keyboard_Simulation.ipynb) | Mouse and keyboard control and event-listening examples using pynput. |
| [PDF.ipynb](./PDF.ipynb) | PDF creation examples using ReportLab. |
| [PyQt-GUI.ipynb](./PyQt-GUI.ipynb) | Exploratory PyQt5 desktop-interface examples. |
| [Strings_Stuff.ipynb](./Strings_Stuff.ipynb) | Python string operations and examples. |
| [tkinter_arena.ipynb](./tkinter_arena.ipynb) | Tkinter desktop-interface experiments. |

## Getting Started

1. Clone or download the repository.
2. Select a topic from the guide above.
3. Open notebooks in Jupyter Notebook, JupyterLab, or VS Code with Python and Jupyter support.
4. Select a Python environment and install the third-party packages required by the examples you intend to run. The repository does not include a shared dependency manifest or lock file.
5. Review cells for local paths, file writes, database operations, or desktop interactions before executing them. Run the required setup cells before dependent examples.

For environment and dependency-management guidance, see the [Python workflows README](./001_WorkFlows/002_Python_Workflows/README.md).

### Standalone Scripts and External Tools

- Run Turtle scripts from a terminal with Python, for example: `python .\004_Turtle_Concepts\Square_Pattern.py`. Turtle and GUI examples require a desktop session and the corresponding GUI support in your Python installation.
- Mouse and keyboard examples can affect the active desktop. Run them only in a controlled environment after reviewing their behavior.
- SQL examples require the database system and sample data described in the notes. Use a disposable practice database for statements that modify or delete data.
- The code2flow guide uses a separate Graphviz installation for rendering diagrams.

## Git Helpers

The root-level [git_pull](./git_pull) and [git_push](./git_push) files, along with the helpers in [001_Git_WorkFlows](./001_WorkFlows/001_Git_WorkFlows/), are Bash scripts. On Windows, use a Bash-compatible shell such as Git Bash rather than running them directly in PowerShell.

Review these scripts before use: the push helper stages all changes, creates a commit, pulls remote changes, and pushes to the configured remote. They are convenience scripts, not prerequisites for using the learning material.

## `Happy Coding !`
