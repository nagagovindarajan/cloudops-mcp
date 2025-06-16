# Cloud Ops MCP

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/yourusername/cloudops-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/cloudops-mcp/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## Overview

Cloud Ops MCP is an open-source Model Context Protocol (MCP) server that leverages AI to analyze user queries. It then interfaces with cloud environments, using AWS CLI for AWS account analysis and kubectl for Kubernetes cluster interactions, to provide comprehensive details and insights.

## Features

- **Natural Language Interface**: Query your AWS resources using plain English
- **AWS CLI Integration**: Automatically converts natural language to AWS CLI commands
- **Kubernetes Support (Coming Soon)**: Analyze and manage Kubernetes clusters
- **FastAPI Backend**: Robust API server with MCP support
- **Multi-Model Support**: Configurable to use various AI models for different tasks
- **VS Code Copilot Integration**: Works with GitHub Copilot in Agent mode

## Setup

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Get an API key from Google Gemini AI studio (Use your personal account for free tier)
5. Create a `.env` file in the root directory with your API key:
```
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=your_api_key_here
```

6. Create a new AWS profile with limited access and add it to the `.env` file:
```
AWS_PROFILE=your_profile_name
```

## Running the application

Start the application with:
```bash
uvicorn app.main:app --reload

or

python run.py
```

The MCP server API will be available at http://127.0.0.1:8000/mcp

## Add MCP endpoint in VSCode - Copilot 

1. Open VSCode
2. Open Copilot settings
3. Add the following endpoint:
```
http://127.0.0.1:8000/mcp
```

Check the video below for the steps:

Note: This will work only with Agent mode in Copilot. Also use Claude Sonnet 3.5 and above or equivalent for best results.


https://github.com/user-attachments/assets/4f3d98d7-7b4b-48d6-9728-65a6263e6d61

### API Endpoints

- `GET /ask_cli_agent?message=your-query-here`: Query AWS resources using natural language
- `/mcp`: MCP protocol endpoint for tool discovery and execution

## Example use cases 

- "What are my top 5 most expensive AWS services this month?"
- "List all EC2 instances with high CPU usage in the last 1 hour."
- "Give me the latest 10 AWS Health events"
- "List all users with admin privileges and their last login."
- "Why is pod xyz in crashloopbackoff?" (Kubernetes)
- "Any 5xx errors in the last 15 minutes from radio-laravel-stg ecs cluster?"
- "Which S3 buckets had public access in the last week?"

## Example video:

https://github.com/user-attachments/assets/21b1dd3c-99e7-4517-beef-c7286771fcd4

## Architecture

CloudOps-MCP consists of:

- **FastAPI Application**: Core API server with MCP support
- **AWS Expert Agent**: Processes natural language and generates AWS commands
- **Command Generator**: Translates user requests to AWS CLI commands
- **Command Executor**: Safely executes AWS CLI commands

## Development

### Project Structure

```
cloudops-mcp/
├── app/
│   ├── agents/
│   │   ├── aws_expert/
│   │   │   ├── awsexpert_agent.py
│   │   │   ├── callbacks.py
│   │   │   └── prompt.py
│   │   └── agent.py
│   ├── main.py
│   └── util.py
├── memory/
│   ├── aimodel.py
│   ├── chroma_db.py
│   ├── constants.py
│   ├── inmem_storage.py
│   ├── knowledge_base.py
│   └── utils.py
├── common_util.py
├── config.py
├── logger.py
├── requirements.txt
├── run.py
└── LICENSE
```

### Quick Start for Developers

```bash
# Set up development environment
./scripts/setup_dev.sh

# Run tests
pytest

# Start the server
python run.py
```

## Contributing

We welcome contributions from the community! Please see our [Contributing Guide](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Google ADK for agent development infrastructure
- FastAPI-MCP for Model Context Protocol implementation
- All our contributors and users

## Security

For sensitive security issues, please follow our [Security Policy](SECURITY.md).

## Disclaimer

<p style="color:red;">
<b>Important: This is a proof-of-concept application and is NOT production-ready.</b> It is intended for demonstration and testing purposes only.
<br><br>
<b>Security Risk:</b> Do NOT provide AWS profiles with administrative privileges to this MCP server. Always create and use a new AWS profile with the minimum necessary permissions.
<br><br>
<b>Potential for Harm:</b> There is currently no robust framework in place to prevent the execution of destructive commands. Use with extreme caution.
</p>

## TODO

- [ ] Add kubernetes support
- [ ] Add more tests
- [ ] Add more examples
- [ ] Add more documentation
- [ ] Add more error handling
- [ ] Add more logging
