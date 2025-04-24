import subprocess
import re
import json
from jinja2 import Template
from memory.constants import GEMINI_MODELS
from memory.aimodel import AIModel

def execute_command(command: str, path: str):
    # command_set = str(command).split(" ")
    process = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True, 
        cwd=path,
        timeout=300
    )

    if process.returncode == 0:
        command_output = process.stdout.decode('utf-8') 
    else:
        command_output = f"ERROR: Command failed with exit code {process.returncode}\n{process.stderr.decode('utf-8')}"
    
    cleaned_output = re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', command_output)
    if cleaned_output == "":
        cleaned_output = "No output"
        
    return process.returncode, command_output, cleaned_output

def convert_to_single_word(text):
    # Split the text into words
    words = text.split()
    
    # Capitalize each word and join them without spaces
    single_word = ''.join(word.capitalize() for word in words)
    
    return single_word

def is_json(input_string):
    try:
        json.loads(input_string)
        return True
    except json.JSONDecodeError:
        return False
 
def extract_tag_content(response, tag):
    match = re.search(rf'<{tag}>(.*?)</{tag}>', response, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "Invalid input"

def extract_json_obj(response):
    # First try to find JSON in markdown code blocks
    match = re.search(r'```json(.*?)```', response, re.DOTALL)
    if match:
        json_str = match.group(1).strip()
        try:
            json_dict = json.loads(json_str)
            sanitized_dict = {k: (v if v is not None else "") for k, v in json_dict.items()}
            return sanitized_dict
        except json.JSONDecodeError:
            pass
    
    # If no markdown block or parsing failed, try to parse the entire response as JSON
    try:
        json_dict = json.loads(response.strip())
        sanitized_dict = {k: (v if v is not None else "") for k, v in json_dict.items()}
        return sanitized_dict
    except json.JSONDecodeError:
        # Try to find JSON-like structure without markdown
        match = re.search(r'(\{.*\})', response, re.DOTALL)
        if match:
            try:
                json_dict = json.loads(match.group(1))
                sanitized_dict = {k: (v if v is not None else "") for k, v in json_dict.items()}
                return sanitized_dict
            except json.JSONDecodeError:
                pass
    
    return {}

def render_jinja_template(template_str: str, data: dict):
    template = Template(template_str)
    return template.render(data)

def get_model_details(model_id: str) -> AIModel:
    for model in GEMINI_MODELS:
        if model.id == model_id:
            return model
    return None

def get_model_details_by_name(model_name: str) -> AIModel:
    for model in GEMINI_MODELS:
        if model.name == model_name:
            return model
    return None