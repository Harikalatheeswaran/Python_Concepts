# Python Workflows

Reference material for setting up Python projects, managing virtual environments, and maintaining dependencies with [uv](https://docs.astral.sh/uv/).

## Folder Structure

```text
002_Python_Workflows/
│
├── README.md
└── 001_UV_workflow/
    └── 001_UV_WorkFlow.md
```

## Available Guide

| Resource | Coverage |
| --- | --- |
| [uv workflow guide](./001_UV_workflow/001_UV_WorkFlow.md) | Installation, project initialization, virtual environments, dependency management, lock files, working with existing projects, migration from pip and venv, and an illustrative API-based example. |

## Using the Guide

1. Review the installation options and choose the method appropriate for your operating system.
2. Follow the new-project workflow for a fresh project, or the existing-project workflow for a project that already includes uv configuration.
3. Use the dependency-management sections to understand how project metadata, lock files, and environments fit together.
4. Consult the [official uv documentation](https://docs.astral.sh/uv/) for current commands and platform-specific instructions.

The guide is a reference, not a configured uv project. This folder does not contain a project manifest, lock file, or standalone example application. Adapt its example paths, package choices, and shell commands to your own project.

## Related Resources

- [Git workflow helpers](../001_Git_WorkFlows/): Bash scripts for pulling and pushing repository changes.
- [Repository overview](../../README.md): The complete topic guide and repository structure.
