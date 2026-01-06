
# Complete Guide: Using code2flow for Python Call Graphs (No Images)

This guide walks you through generating a `.dot` file from Python code using **code2flow**, then rendering it to **SVG** – all via command line, with clear steps for single files, whole folders, normal rendering, and handling large/overlapping graphs.

### 1. Installation

#### Install code2flow
Open Command Prompt (or terminal) and run:
```bash
pip install code2flow
```
This installs the tool that analyzes your Python code and produces call graphs.

#### Install Graphviz (for rendering)
On Windows 10/11 (recommended easy way):
```bash
winget install graphviz
```
- After installation, **close and reopen Command Prompt** (or restart your PC) so the system recognizes `dot`, `sfdp`, etc.
- Test it: Run `dot -V` → should display the Graphviz version (e.g., "dot - graphviz version 12.x.x").

(Alternative: Download installer from https://graphviz.org/download/ and check "Add to PATH" during setup.)

### 2. Generating the .dot File

#### For a Single Python File
To create a call graph from one file (e.g., `main.py`):
```bash
code2flow main.py --output single_graph.dot
```
- Creates `single_graph.dot` showing functions and calls within that file.

#### For an Entire Folder (Multiple Files)
To analyze a complete project directory (recursively scans all `.py` files):
```bash
code2flow path/to/your/project_folder/ --output project_graph.dot
```
- Example: `code2flow src/ --output full_project.dot`
- This shows inter-module dependencies and cross-file function calls – perfect for understanding large tools with many files and database interactions (via code).

### 3. Rendering .dot to SVG

#### Normal Rendering (Small to Medium Graphs)
Use the default hierarchical layout (good for clear, tree-like structures):
```bash
dot -Tsvg your_graph.dot -o your_graph.svg
```
- Open the resulting `.svg` file in any web browser (Chrome, Firefox, Edge) – you can zoom and pan smoothly.

#### For Large Graphs (Prevent Node Overlapping)
Large projects often produce dense graphs with overlapping nodes when using default settings. Use the **sfdp** engine instead – it's specifically designed for big graphs and gives much cleaner results:
```bash
sfdp -Tsvg project_graph.dot -o project_graph.svg -Goverlap=prism
```
- Key options explained:
  - `sfdp`: Better layout engine for large/dense graphs.
  - `-Goverlap=prism`: Actively removes node overlaps (very effective).
- If nodes are still too close, add more spacing:
```bash
sfdp -Tsvg project_graph.dot -o project_graph.svg -Goverlap=prism -Goverlap_scaling=20
```
  (Increase the number like 30–50 if needed.)

Alternative way (using `dot` command but forcing sfdp engine):
```bash
dot -Ksfdp -Tsvg project_graph.dot -o project_graph.svg -Goverlap=prism
```

### Summary of Commands
| Task                              | Command                                                                 |
|-----------------------------------|-------------------------------------------------------------------------|
| Install code2flow                 | `pip install code2flow`                                                 |
| Install Graphviz (Windows)        | `winget install graphviz`                                               |
| Single file → .dot                | `code2flow myfile.py --output myfile.dot`                               |
| Whole folder → .dot               | `code2flow src/ --output project.dot`                                   |
| Normal SVG render                 | `dot -Tsvg graph.dot -o graph.svg`                                      |
| Large graph SVG (no overlap)      | `sfdp -Tsvg graph.dot -o graph.svg -Goverlap=prism`                     |
| Extra spread (if needed)          | Add `-Goverlap_scaling=20` (or higher)                                  |

werbsite to render small graphs : https://dreampuf.github.io/GraphvizOnline/
---
---
---

# Code2Flow Usage Summary

**Code2flow** is a Python tool (available on PyPI) that generates interactive call graphs (flowcharts) from source code in dynamic languages like Python, JavaScript, Ruby, and PHP. It maps functions/classes and their call relationships, outputting a Graphviz DOT file (and optionally a rendered image if Graphviz is installed).

The primary repo is: https://github.com/scottrogowski/code2flow

## Installation
```bash
pip install code2flow
```

For rendering images directly (PNG/SVG), install Graphviz separately (from graphviz.org) and add it to your PATH.

## Basic Command-Line Usage
```bash
code2flow [options] <source_files_or_directories>...
```

- Provide one or more files, or a directory (it will recursively scan for supported files).
- By default, outputs `out.gv` (DOT file) and `out.png` (if Graphviz available).

### Examples
- Single file (Python assumed if no language specified):
  ```bash
  code2flow myfile.py
  pip install code2flow
code2flow your_file.py --output output.dot
  ```

- Multiple files or directory:
  ```bash
  code2flow src/ myfile.py another.js
  ```

- Whole project directory:
  ```bash
  code2flow path/to/project/
  ```

- Specify output file:
  ```bash
  code2flow src/ --output diagram.dot
  ```

- Focus on a specific function (subgraph centered on it):
  ```bash
  code2flow src/ --target-function main_function --upstream-depth=2 --downstream-depth=3
  ```

## Key Command-Line Options
Run `code2flow --help` for the full list. Common ones include:

- `--output OUTFILE` or `-o OUTFILE`: Specify output file (e.g., `diagram.dot` or `diagram.png`).
- `--language LANGUAGE`: Explicitly set language (`py`, `js`, `ruby`, `php`). Auto-detected otherwise.
- `--target-function FUNCTION`: Generate a focused graph around this function.
- `--upstream-depth N`: Levels of callers to include.
- `--downstream-depth N`: Levels of callees to include.
- `--quiet`: Suppress logs.
- `--no-grouping`: Disable grouping by modules/classes.
- Others: Options for excluding patterns, hiding legends, etc.

## Rendering the DOT File
If no auto-render:
```bash
dot -Tpng diagram.dot -o diagram.png
dot -Tsvg diagram.dot -o diagram.svg  # Recommended for scalable vectors
```

Or use online tools like https://dreampuf.github.io/GraphvizOnline/ by pasting DOT content.

## As a Python Library
```python
from code2flow import code2flow

code2flow(['file1.py', 'dir/'], 'output.dot', language='py')
```

## Limitations
- Best for static analysis; misses dynamic/lambda calls, some imports, inheritance.
- Approximates structure—great for overview, not perfect for complex/dynamic code.

This tool is excellent for understanding module interlinks in larger projects!


Use this website to download/render : https://dreampuf.github.io/GraphvizOnline/?referrer=grok.com

Alternatives if it hangs on very large files:
- https://edotor.net/ (rich features, good for big ones).
- https://magjac.com/graphviz-visual-editor/ (interactive, highlights nodes).
- https://www.devtoolsdaily.com/graphviz/ (AI-powered, live preview).


---

Dot renders : 

- sfdp -Tsvg "D:\Docs\01_Projects\002_PSS_HEP_Dashboard\HEP_OSS_RM_ETM_Report_Generator05-01-26\HEP_OSS_RM_ETM_Report_Generator\DOT_renders\output_full_folder.dot" -o better_graph.svg -Goverlap=prism -Goverlap_scaling=20

```text 
dot -Tsvg -Ksfdp large.dot -o large_graph.svg   # Try sfdp for large graphs
# Or alternatives:
dot -Tsvg -Kfdp large.dot -o large_graph.svg
dot -Tsvg -Kneato large.dot -o large_graph.svg
```

---
---
---
Yes, buddy! Since you have **Graphviz** installed (and `dot` works), the **`sfdp`** command should absolutely work—it's one of the standard layout engines included in every full Graphviz installation (along with dot, neato, fdp, circo, twopi, etc.).

`sfdp` is a separate executable (like `dot.exe` on Windows), so you can run it directly.

### How to Use It
Just replace `dot` with `sfdp` in your command:

```bash
sfdp -Tsvg yourfile.dot -o output.svg -Goverlap=prism
```

- This uses the **sfdp** engine (great for large graphs with less overlapping).
- `-Goverlap=prism` helps remove any remaining node overlaps (highly recommended!).
- Add `-Goverlap_scaling=10` (or higher) if needed for more spreading.

Example full command for your case:
```bash
sfdp -Tsvg large.dot -o better_graph.svg -Goverlap=prism -Goverlap_scaling=20
```

### Quick Test
Run this to confirm sfdp is available:
```bash
sfdp -V
```
It should print the Graphviz version, just like `dot -V` does.

### If It Says "sfdp not recognized" (Rare, but Possible)
- On some older or minimal installs (especially certain Linux packages or very old Windows builds), sfdp might be missing certain dependencies for advanced overlap removal (like prism mode needing a triangulation library).
- But basic sfdp almost always works—try without `-Goverlap=prism` first:
  ```bash
  sfdp -Tsvg yourfile.dot -o output.svg
  ```

Alternative (if direct sfdp fails): Force any command to use sfdp engine:
```bash
dot -Ksfdp -Tsvg yourfile.dot -o output.svg -Goverlap=prism
```

This uses the `dot` executable but switches to sfdp layout—works even if the standalone sfdp command is quirky.

Give `sfdp -V` a try and let me know what it says—it'll confirm everything! This should finally give you a clean, non-overlapping diagram. 😊


---
---
---

