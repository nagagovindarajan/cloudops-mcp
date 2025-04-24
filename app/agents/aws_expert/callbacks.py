"""Callback functions for FOMC Research Agent."""

import logging
import time
import base64
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest, LlmResponse
from typing import Any, Dict
from google.adk.tools import BaseTool
from google.adk.agents.invocation_context import InvocationContext
import google.genai.types as types
from common_util import extract_json_obj
from google.adk.tools.tool_context import ToolContext
from google.adk.sessions.state import State
from common_util import render_jinja_template
from time import sleep
from datetime import datetime
from google.adk.sessions.session import Session

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def create_prompt(agent_name : str, state : State) -> types.Content:
    template = None
    # if agent_name == "root_agent":
    #     template = ROOT_AGENT_PROMPT
    # elif agent_name == "post_plan_decider_agent":
    #     template = POST_PLAN_DECISION_AGENT_PROMPT
    # elif agent_name == "knowledable_agent":
    #     template = KNOWLEDGABLE_AGENT_PROMPT
    # elif agent_name == "task_manager_agent":
    #     template = TASK_MANAGER_PROMPT
    # elif agent_name == "orchestrator_agent":
    #     template = ORCHESTRATOR_PROMPT
    # elif agent_name == "agent_switcher":
    #     template = SWITCH_AGENT_PROMPT
    # elif agent_name == "action_agent":
    #     template = ACTION_AGENT_PROMPT
    # elif agent_name == "action_verification_agent":
    #     template = ACTION_VERIFICATION_PROMPT
    # elif agent_name == "plan_refiner_agent":
    #     template = PLAN_REFINER_PROMPT
    # elif agent_name == "agent_summarizer":
    #     template = AGENT_SUMMARIZER_PROMPT
    # elif agent_name == "message_to_user_agent":
    #     template = MESSAGE_TO_USER_PROMPT
    
    # if template:
    #     rendered_prompt = render_jinja_template(template, state.to_dict())
    #     return types.Content(parts=[types.Part(text=rendered_prompt)], role="user")
    return None

# checking that the customer profile is loaded as state.
def before_agent(callback_context: CallbackContext):
    agent_name = callback_context._invocation_context.agent.name
    # if agent_name == "root_agent":
    #     if "user_request" not in callback_context.state:
    #         print(f"User request: {callback_context._invocation_context.user_content.parts[0].text}")
    #         callback_context.state["user_request"] = callback_context._invocation_context.user_content.parts[0].text
   
    print(f"Before agent callback completed for {agent_name}")

def after_agent(callback_context: CallbackContext):
    agent_name = callback_context._invocation_context.agent.name
    print(f"After agent callback completed {agent_name}")

def before_model(callback_context: CallbackContext, llm_request: LlmRequest) -> None:
    agent_name = callback_context._invocation_context.agent.name  

    # prompt = create_prompt(agent_name,callback_context.state)
    # if prompt:
    #     llm_request.contents.append(prompt)
  
    content_texts = []
    for content in llm_request.contents:
        if content and content.parts:
            for part in content.parts:
                if hasattr(part, 'text') and part.text:
                    content_texts.append(part.text)
    print(f"LLM request text {content_texts}")

    print(f"Before model callback completed for {agent_name} {len(llm_request.contents)}")

def after_model(callback_context: CallbackContext, llm_response: LlmResponse):
    agent_name = callback_context._invocation_context.agent.name
    print(f"LLM response parts:")
    for i, part in enumerate(llm_response.content.parts):
        print(f"  Part {i}: {part.text}")
    print(f"After model callback completed for {agent_name}")

def before_tool(tool: BaseTool, args: Dict[str, Any], tool_context: ToolContext):
    print(f"Before tool callback started for {tool.name}")


def after_tool(tool: BaseTool, args: Dict[str, Any], tool_context: ToolContext, tool_response: dict):
    print(f"After tool callback completed for {tool.name}")

