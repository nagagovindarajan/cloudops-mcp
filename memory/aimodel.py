from typing import List
from pydantic import BaseModel

class AIModel:
    def __init__(self, name: str, model_id: str, inputs: List[str] = ["text"], outputs: List[str] = ["text"],
                 structured_output: bool = False, function_calling: bool = False, search: bool = False, code_execution: bool = False, think: bool = False, live: bool = False):
        self.name = name
        self.id = model_id
        self.inputs = inputs
        self.outputs = outputs
        self.structured_output = structured_output
        self.function_calling = function_calling
        self.search = search
        self.code_execution = code_execution
        self.can_use_image_ip = "image" in inputs
        self.can_use_audio_ip = "audio" in inputs
        self.can_use_video_ip = "video" in inputs
        self.can_get_image_op = "image" in outputs
        self.can_get_audio_op = "audio" in outputs
        self.can_get_video_op = "video" in outputs
        self.can_think = think
        self.can_live = live

    def __repr__(self):
        return f"AIModel(name={self.name}, id={self.id})"

class ClientCommand(BaseModel):
    command: str
    details: str

class AgentPlan(BaseModel):
    plan: list = None
    status: str = None # waiting_for_input, ready
    message: str = None
    scratchpad: str = None

class AgentResponse(BaseModel):
    task_description: str = None
    current_action: str = None
    current_action_details: str = None
    status: str = None # waiting_for_input, in_progress, completed
    scratchpad: str = None

class AgentOrchestratorResponse(BaseModel):
    updated_plan: list = None
    next_task_description: str = None
    status: str = None # completed, in_progress
    summary: str = None
