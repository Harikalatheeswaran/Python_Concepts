# <div align='center'> *__🧠 Ruff in Python__* </div>

## 🚀 1. What is Ruff (explained like you're new)

Imagine you're writing Python code like writing an essay.

Now think:
- You might make grammar mistakes ❌  
- Your sentences might be inconsistent ❌  
- You may repeat things or leave unused words ❌  

👉 Ruff is like a **super-fast grammar + style checker for your Python code**

### In simple terms:
> **Ruff = A tool that scans your code, finds problems, and can fix many of them automatically**

---

## 🔎 What Ruff Actually Does

Ruff combines the work of multiple traditional Python tools:

- ✅ Finds errors (like flake8)
- ✅ Enforces coding style (like pycodestyle)
- ✅ Sorts imports (like isort)
- ✅ Formats code (like black)

👉 So instead of installing many tools, you install **just Ruff**

---

## ⚡ Why Ruff is Popular

- 🔥 Extremely fast (built in Rust)
- 🧹 Auto-fixes issues
- 📦 Replaces multiple tools
- 🧠 Easy to configure
- 🚀 Works great in modern workflows (CI/CD, editors, etc.)

---

## 📄 2. What is `ruff.toml`?

Think of Ruff like a machine 🏭  

It needs instructions on:
- How strict to be
- What rules to follow
- What to ignore

👉 `ruff.toml` is that **instruction file**

---

### Example `ruff.toml`

```toml
line-length = 88
target-version = "py311"

[lint]
select = ["E", "F", "I"]
ignore = ["E501"]

[format]
quote-style = "double"
indent-style = "space"
```

---

### What each part means

- `line-length = 88` → Maximum line length allowed
- `target-version` → Your Python version
- `select` → Rules you want Ruff to enforce
- `ignore` → Rules you want Ruff to skip
- `format` → Style preferences (quotes, indentation)

---

## 🧪 3. How to Use Ruff with `ruff.toml` (Standalone Setup)

### Step 1 — Install Ruff

```bash
pip install ruff
```

---

### Step 2 — Create config file

```bash
touch ruff.toml
```

---

### Step 3 — Add configuration

Paste the example config into `ruff.toml`

---

### Step 4 — Run Ruff

#### Check for issues:
```bash
ruff check .
```

#### Auto-fix issues:
```bash
ruff check . --fix
```

#### Format code:
```bash
ruff format .
```

👉 Ruff automatically detects and uses `ruff.toml`

---

## ⚠️ Important (Config Priority)

Ruff checks for configuration in this order:

1. ✅ `pyproject.toml` (most common)
2. ✅ `ruff.toml`
3. ✅ Command-line arguments

---

## 🔗 4. Using Ruff with `uv`

You're using `uv`, which is great ✅  

👉 `uv` automatically creates and uses `pyproject.toml`

So instead of creating a `ruff.toml`, we embed Ruff config inside `pyproject.toml`

---

### Example `pyproject.toml`

```toml
[project]
name = "my-project"
version = "0.1.0"

[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I"]
ignore = ["E501"]

[tool.ruff.format]
quote-style = "double"
```

---

## ✅ Installing Ruff with `uv`

```bash
uv add --dev ruff
```

👉 This adds Ruff as a development dependency

---

## 🔁 5. Typical Workflow: `uv + Ruff`

### 📦 Step 1 — Setup Project

```bash
uv init
uv add --dev ruff
```

---

### 🧑‍💻 Step 2 — Write Code

Example (bad code):

```python
import os, sys
```

---

### 🔍 Step 3 — Run Lint Check

```bash
ruff check .
```

Ruff might report:
- Multiple imports on one line
- Unused imports

---

### 🔧 Step 4 — Auto-fix Issues

```bash
ruff check . --fix
```

---

### 🎨 Step 5 — Format Code

```bash
ruff format .
```

---

### ✅ Final Result

```python
import os
import sys
```

---

## 🔄 Real Daily Workflow

```bash
# Sync dependencies
uv sync

# Write code

# Find problems
ruff check .

# Fix problems automatically
ruff check . --fix

# Format code
ruff format .
```

---

## 🔥 Useful Developer Tips

### ✅ Run before committing code

```bash
ruff check . --fix && ruff format .
```

---

### ✅ Use in CI/CD

```bash
ruff check .
```

👉 If code has issues → build fails ✅

---

## 🧠 Final Understanding (Feynman Summary)

- Ruff is a **code quality tool**
- It helps you:
  - ✅ Find mistakes
  - ✅ Fix them automatically
  - ✅ Keep code clean and consistent

- `ruff.toml` or `pyproject.toml` → tells Ruff how to behave

- If you're using `uv`:
  👉 Prefer `pyproject.toml` (single config file)

---

## 🏁 Final Recommendation

👉 Modern Python setup:

- ✅ `uv` → dependency management  
- ✅ `ruff` → linting + formatting  
- ✅ `pyproject.toml` → central configuration  

---

## Sample ruff.toml configuration : 

```toml
# Exclude a variety of commonly ignored directories. This means Ruff will not lint or format files with these names
exclude = [
  ".bzr",
  ".direnv",
  ".eggs",
  ".git",
  ".git-rewrite",
  ".hg",
  ".ipynb_checkpoints",
  ".mypy_cache",
  ".nox",
  ".pants.d",
  ".pyenv",
  ".pytest_cache",
  ".pytype",
  ".ruff_cache",
  ".svn",
  ".tox",
  ".venv",
  ".vscode",
  "__pypackages__",
  "_build",
  "buck-out",
  "build",
  "dist",
  "node_modules",
  "site-packages",
  "venv",
]

indent-width = 4 # each indent is 4 spaces, equivalent to using "tab" 
line-length = 100 # max no of characters in a line. Black default is 88 characters
target-version = "py310" # Assumes Python 3.10 and above

[lint]
select = [
  "A", # flake8-builtins
  "B", # flake8-bugbear
  "D", # pydocstyle
  "E", # pycodestyle errors
  "F", # pyflakes
  "G", # flake8-logging-format
  "I", # isort
  "N", # pep8-naming
  "S", # flake8-bandit
  "W", # pycodestyle warnings
  "C4", # flake8-comprehensions
  "EM", # flake8-errmsg
  "PD", # pandas-vet
  "PL", # Pylint
  "UP", # pyupgrade - auto-upgrade syntax for current version of Python
  "ANN", # flake8-annotations
  "BLE", # flake8-blind-except
  "C90", # McCabe complexity checker
  "ERA", # eradicate - removes commented out code
  "FBT", # flake8-boolean-trap
  "FLY", # flynt
  "ICN", # flake8-import-conventions
  "LOG", # flake8-logger
  "NPY", # numpy-specific rules
  "PGH", # pygrep-hooks
  "PIE", # flake8-pie
  "RET", # flake8-return
  "RSE", # flake8-raise
  "SIM", # flake8-simplify
  "RUF", # ruff-specific rules
  "TCH", # flake8-type-checking
  "TID", # flake8-tidy-imports
  "TRY", # tryceratops
  "ASYNC", # flake8-async
]

ignore = [
  "W191", # lint rule that may clash with Ruff Formatter: tab-indentation
  "E111", # lint rule that may clash with Ruff Formatter: indentation-with-invalid-multiple
  "E114", # lint rule that may clash with Ruff Formatter: indentation-with-invalid-multiple-comment
  "E117", # lint rule that may clash with Ruff Formatter: over-indented
  "D206", # lint rule that may clash with Ruff Formatter: indent-with-spaces
  "D300", # lint rule that may clash with Ruff Formatter: triple-single-quotes      
  "D1", # ignore this to match google docstring convention
  "G004", # ignore this to allow f-strings in logging
  "UP007", # ignore to avoid auto-fixes which lead to incompatibility with pydantic 
  "UP015", # ignore this to allow "with open" statements to have modes explicitly stated
  "SIM102", # ignore this to avoid changing nested if statements to single if statements, potentially confusing
  "ANN101", # ignore this to avoid needing to annotate "self" in class methods
  "ANN102", # ignore this to avoid needing to annotate "cls" in class methods
]

fixable = ["ALL"] # Allow fix for all enabled rules (when using "Fix all" or when `--fix` is provided to ruff check in CLI)
unfixable = ["F401"] # disable autofix for unused-imports

dummy-variable-rgx = "^(_+\\w*)$" # Allow unused variables when underscore-prefixed
flake8-bugbear.extend-immutable-calls = [
  "fastapi.Depends", 
  "fastapi.Query"] 
# Allow default arguments like, e.g., `data: List[str] = fastapi.Query(None)`
isort.force-single-line = true # force each import to be in its own line
pycodestyle.max-doc-length = 100 # max line-length for docstrings
pydocstyle.convention = "google" # docstring convention. Options: "google", "numpy", or "pep257"
pylint.max-args = 10 # max no of args in a function

[format]
docstring-code-format = true # Enable auto-formatting of code examples in docstrings. Markdown, reStructuredText code/literal blocks and doctests are all supported
docstring-code-line-length = "dynamic" # Set line length limit used when formatting code snippets in docstrings. This only has an effect when the `docstring-code-format` setting is enabled
indent-style = "space" # indent with spaces, rather than "tab"
line-ending = "lf" # options: "auto", "lf", "cr-lf", "native"
quote-style = "double" # Use double quotes as voted by majority
skip-magic-trailing-comma = false # respects magic trailing commas

```
