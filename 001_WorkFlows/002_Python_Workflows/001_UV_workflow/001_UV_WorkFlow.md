
---

# <center> *__UV WorkFlow in Python__*

---

## Contents
1. [Introduction to UV](#1-introduction-to-uv)
2. [Installation](#2-installation)
3. [The Core Workflow Pillars](#3-the-core-workflow-pillars)
4. [Starting a New Project](#4-starting-a-new-project)
5. [Managing Dependencies and Reproducibility](#5-managing-dependencies-and-reproducibility)
6. [Loading an Existing Project](#6-loading-an-existing-project)
7. [Migration from Pip and Venv](#7-migration-from-pip-and-venv)
8. [Example Project: Programmer Joke Fetcher](#8-example-project-programmer-joke-fetcher)

---

## 1. Introduction to UV
- **UV** is an extremely fast Python package manager and project tool that handles virtual environments, installations, and command execution in a single place. 
- It is designed to be a more consistent alternative to the traditional combination of `pip` and `venv`. 
- If you have experience with **Rust’s Cargo**, UV will feel familiar because it uses a `pyproject.toml` file for dependencies and lock files to ensure reproducibility across different machines.

---

## 2. Installation
To get started, you can install UV using simple terminal commands found on the official documentation site, `docs.astral.sh`.

```bash
# For macOS and Linux users
curl -LsSf https://astral.sh/uv/install.sh | sh
```
### ⚠️ Avoid running the below command as it runs the script directly from web without prior verfication.
```bash
# For Windows users (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
 - ✅ You can instead run the below one : 
 ```bash
 winget install --id=astral-sh.uv -e
 ```
- If you have python installed, then you can directly install it as below :
```bash
pip install uv
```

--- 

## 3. The Core Workflow Pillars
The sources define the UV workflow through four primary pillars:
*   **Project Creation**: UV builds a structured layout for you, so you don't start with a blank folder.
*   **Virtual Environments**: UV manages environments directly, meaning you don't need to manually create or activate them.
*   **Dependency Installation**: It installs packages quickly and consistently while supporting the standard Python ecosystem.
*   **Running Commands**: UV executes Python scripts or commands directly inside the environment without requiring manual activation.

--- 

## 4. Starting a New Project
When starting a new project, UV automates the directory setup and environment initialization.

```bash
# 1. Initialize a new project directory
uv init demo_uv
cd demo_uv

# 2. Create the managed virtual environment
uv venv

# you can activate with:
.venv\Scripts\activate
# deactivate with :
deactivate
# Note - you can run without actiavation too!

# 3. Verify the installation (no activation required)
uv run python --version

# to sync
uv sync


# 4. Run a simple Python command to test the environment
uv run python -c "print('Hello from UV')"
```

---

## 5. Managing Dependencies and Reproducibility
UV simplifies library management by automatically updating your configuration and locking versions for your team.

*   **`uv add`**: Adds a library and automatically updates the `pyproject.toml` file.
*   **`uv sync`**: Ensures your environment is synchronized and all dependencies are correctly installed.
*   **`uv lock`**: Generates a lock file to ensure repeatable and consistent installs for everyone on the team.

```bash
# Add new libraries to the project (e.g., requests and rich)
uv add requests rich

# Synchronize the environment state
uv sync

# Lock dependencies for production or team use
uv lock
```
---

## 6. Loading an Existing Project
If you clone a project that already uses UV, the setup process is simplified through the lock file.

*   **The `uv sync` Workflow**: When a new developer clones a project, they simply run `uv sync`.
*   **Predictability**: UV ensures the local environment is set up exactly as defined in the `uv.lock` file, reducing "works on my machine" bugs.

```bash
# Enter the cloned repository
cd cloned-project-folder

# Set up the environment exactly as defined in the lock file
uv sync

# Run the project script immediately
uv run python main.py
```

---

## 7. Migration from Pip and Venv
Transitioning to UV does not require you to rewrite your code. You can adopt it gradually for existing projects.

*   **Using Requirements Files**: You can use UV’s fast resolver to install from an existing `requirements.txt` file by running `uv pip install -r requirements.txt`.
*   **Full Migration**: You can convert an existing project by running `uv init` in the directory to create a `pyproject.toml` file and then using `uv add` to manage your dependencies.

---

## 8. Example Project: Programmer Joke Fetcher
The following script demonstrates how UV handles dependencies. Once you have added `requests` and `rich` via `uv add`, you can run this script directly with `uv run`.

```python
import requests
from rich.console import Console
from rich.panel import Panel

def fetch_joke():
    """
    Fetches a random programmer joke from a public API.
    Uses 'requests' for the network call and 'rich' for the terminal UI.
    """
    url = "https://official-joke-api.appspot.com/jokes/programming/random"
    try:
        # Perform the GET request to the API
        response = requests.get(url)
        data = response.json()
        
        # The API returns a list, we take the first item
        setup = data['setup']
        punchline = data['punchline']
        
        # Display the joke using Rich's Panel for a nice UI
        console = Console()
        console.print(Panel(f"[bold cyan]{setup}[/bold cyan]\n\n[green]{punchline}[/green]", 
                            title="UV Joke Demo"))
        
    except Exception as e:
        print(f"Error fetching joke: {e}")

if __name__ == "__main__":
    fetch_joke()
```

To execute the code with all dependencies handled automatically:
```bash
uv run python main.py
```

- For advance `uv` usages watch - [indently.io](https://www.youtube.com/watch?v=5nw_H7oqrIk)