from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel
import os
from typing import Optional, Dict, Any
from dotenv import load_dotenv
from fastapi_mcp import FastApiMCP
from app.util import exec_command_in_terminal, get_current_diagram
from fastapi import Body, Request
from app.agents.agent import Agent
# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="Cloud Ops MCP", description="MCP for AWS accounts")

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Cloud Ops MCP. Use /mcp endpoint to list available tools."}


@app.get("/ask_cli_agent")
async def ask_cli_agent(message: str):
    """
    Get details from the CLI agent about the AWS resources managed by the user.

    - **message**: The message to ask the CLI agent.

    Example:
    What are my top 5 most expensive AWS services this month?
    """
    agent = Agent()
    print("message", message)
    response = agent.invoke_agent(message)
    return response


# Add the MCP server to your FastAPI app
mcp = FastApiMCP(app)

# Mount the MCP server to your FastAPI app
mcp.mount()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True) 