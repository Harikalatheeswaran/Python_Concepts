# Code Visualization Concepts

Reference material for exploring source-code relationships through call graphs. The current guide focuses on code2flow for source analysis and Graphviz for rendering diagrams.

## Folder Structure

```text
006_Code_Visualization_Concepts/
│
├── README.md
└── 001_Code2flow/
    └── Code2Flow_Usage_Summary.md
```

## Available Guide

| Resource | Coverage |
| --- | --- |
| [code2flow usage guide](./001_Code2flow/Code2Flow_Usage_Summary.md) | Installing code2flow and Graphviz, analyzing files or directories, generating DOT files, rendering SVG or PNG diagrams, focusing on functions, and adjusting layouts for larger graphs. |

## Tools and Requirements

- **Python and code2flow:** Used to analyze source code and generate call graphs.
- **Graphviz:** Installed separately to render DOT graphs with tools such as `dot` and `sfdp`.
- **Source files:** Supply the file or project directory you want to inspect. This folder contains documentation, not a sample application or pre-generated graphs.

## Suggested Workflow

1. Follow the guide to install code2flow and Graphviz.
2. Select a source file or directory and generate a DOT graph.
3. Render the graph as SVG for scalable viewing or PNG for a raster image.
4. Focus on a function or adjust the graph layout if the result is too dense.

Treat generated call graphs as an aid to understanding code, not a complete runtime trace. Dynamic calls and other language features can limit static analysis. Keep analysis and rendering local when working with private source code.

## References

- [code2flow repository](https://github.com/scottrogowski/code2flow)
- [Graphviz documentation](https://graphviz.org/documentation/)
- [Repository overview](../README.md)
