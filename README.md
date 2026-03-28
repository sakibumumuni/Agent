# Sakibu's Agent

A Claude-powered AI agent with a Flask web UI for interactive chat.

## Overview

This project uses the [Claude Agent SDK](https://github.com/anthropics/claude-code-sdk-python) to create an autonomous AI agent that can read, write, edit files, run shell commands, search the web, and more. It includes a simple web interface built with Flask and Bootstrap for sending prompts and viewing responses.

## Project Structure

```
Agent/
├── agent.py              # Claude Agent SDK script
├── templates/
│   └── agentui.html      # Flask/Bootstrap web UI
└── .gitignore
```

## Features

- **Claude Agent SDK integration** -- streams agent responses including text output and tool usage
- **Tool access** -- the agent can use Read, Write, Edit, Bash, Glob, Grep, and WebSearch tools
- **Web UI** -- a Bootstrap-styled chat interface with a prompt input and response display area

## Prerequisites

- Python 3.10+
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed and authenticated
- `claude_agent_sdk` package

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```

2. Install dependencies:

   ```bash
   pip install claude-agent-sdk flask
   ```

## Usage

### CLI Agent

Run the agent script directly:

```bash
python agent.py
```

This sends a hardcoded prompt to the Claude agent and streams the response to the terminal.

### Web UI

The web interface (served via Flask) provides a chat form at `/chat` where you can type a prompt and see the agent's response rendered in the browser.

## License

MIT
