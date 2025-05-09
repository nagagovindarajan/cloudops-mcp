from typing import Dict, List
# from google.genai.types import Tool
# from google.genai import types

from logger import Logger

import json
import time
import platform
import tiktoken
import asyncio
from .aws_expert.awsexpert_agent import AwsExpertAgent

class Agent:

    def __init__(self, name: str = "DefaultAgent"):
        self.logger = Logger()
        self.name = name
        self.aws_expert_agent = AwsExpertAgent()

    def invoke_agent(self, message: str):
        return self.aws_expert_agent.run(message)
    
