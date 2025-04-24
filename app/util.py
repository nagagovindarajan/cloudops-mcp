import os
import subprocess
import re
import base64

def exec_command_in_terminal(command: str, path: str):
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

def get_current_diagram(path: str) -> str:
    try:
        # Find first PNG file in the project directory
        for file in os.listdir(path):
            if file.lower().endswith('.png'):
                diagram_path = os.path.join(path, file)
                with open(diagram_path, "rb") as f:
                    return base64.b64encode(f.read()).decode("utf-8")
    except (FileNotFoundError, OSError):
        return None

def main():
    print(get_current_diagram("./data"))

if __name__ == "__main__":
    main()