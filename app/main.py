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

app = FastAPI(title="Weather API", description="API for getting current weather information")

# Get API key from environment variables
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")

class WeatherResponse(BaseModel):
    location: str
    temperature: float  # in Celsius
    description: str
    humidity: int  # percentage
    wind_speed: float  # in m/s

class DiagramRequest(BaseModel):
    diagram_code: str

class NestedDiagramRequest(BaseModel):
    json_body: DiagramRequest

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Weather API. Use /weather endpoint to get weather data."}

# @app.get("/weather/{city}", response_model=WeatherResponse)
# def get_weather(city: str, country_code: Optional[str] = None):
#     """
#     Get current weather for a specific city.
    
#     - **city**: Name of the city
#     - **country_code**: Optional ISO 3166 country code
#     """
#     if not OPENWEATHER_API_KEY:
#         raise HTTPException(status_code=500, detail="API key not configured")
    
#     location_query = city
#     if country_code:
#         location_query = f"{city},{country_code}"
    
#     url = f"https://api.openweathermap.org/data/2.5/weather"
#     params = {
#         "q": location_query,
#         "appid": OPENWEATHER_API_KEY,
#         "units": "metric"  # for Celsius
#     }
    
#     try:
#         response = requests.get(url, params=params)
#         response.raise_for_status()
#         data = response.json()
        
#         weather_data = WeatherResponse(
#             location=f"{data['name']}, {data['sys']['country']}",
#             temperature=data['main']['temp'],
#             description=data['weather'][0]['description'],
#             humidity=data['main']['humidity'],
#             wind_speed=data['wind']['speed']
#         )
#         return weather_data
        
#     except requests.RequestException as e:
#         raise HTTPException(status_code=503, detail=f"Error fetching weather data: {str(e)}")
#     except (KeyError, IndexError) as e:
#         raise HTTPException(status_code=500, detail=f"Error parsing weather data: {str(e)}")

# @app.post("/generate_diagram")
# async def generate_diagram(request: Request) -> str:
#     """
#     Instructions to AI:
#     - Use only the Python DIAGRAM library for generating the architecture diagram. Do not use or suggest any other libraries. 
#     - Provide only the Python Diagram code in the request body.
#     - You dont need to install any libraries in the terminal.
#     - You can just provide the code to this tool and get the base64 encoded diagram.
#     - Generate a diagram from the given diagram library code.
#     - Generating architecture diagrams for AWS cloud, GCP cloud, Azure cloud, on-premises, private cloud, and Kubernetes flows. 


#     Request body format:
#     ```json
#     {
#         "diagram_code": "your Python Diagram code here"
#     }
#     ```

#     Example code for the diagram_code field:
#     ```python
#     from diagrams import Diagram
#     from diagrams.aws.compute import EC2
#     from diagrams.aws.database import RDS
#     from diagrams.aws.network import ELB

#     with Diagram("Web Service", show=False):
#         ELB("lb") >> EC2("web") >> RDS("userdb")
#     ```

#     Returns:
#         - **base64_diagram**: The base64 encoded diagram
#     """
#     # Get the request body and log it for debugging
#     json_data = await request.json()
#     print("Received JSON data:", json_data)
    
#     # Extract diagram_code from various possible structures
#     diagram_code = None
#     if isinstance(json_data, dict):
#         if "diagram_code" in json_data:
#             diagram_code = json_data["diagram_code"]
#         elif "json_body" in json_data and isinstance(json_data["json_body"], dict):
#             if "diagram_code" in json_data["json_body"]:
#                 diagram_code = json_data["json_body"]["diagram_code"]
    
#     if not diagram_code:
#         # Log the structure we received for debugging
#         print("Could not find diagram_code in:", json_data)
#         raise HTTPException(status_code=400, detail=f"diagram_code not found in request body. Received: {json_data}")
    
#     path = "./data"
#     diagram_path = f"{path}/diagram.py"
#     os.makedirs(os.path.dirname(diagram_path), exist_ok=True)

#     # Delete all PNG files in the project directory
#     for file in os.listdir(path):
#         if file.lower().endswith('.png'):
#             os.remove(os.path.join(path, file))
    
#     # Extract code from markdown code block if necessary
#     import re
#     code_block_match = re.search(r"```python\s*(.*?)\s*```", diagram_code, re.DOTALL)
#     if code_block_match:
#         diagram_code = code_block_match.group(1).strip()
    
#     with open(diagram_path, "w") as f:
#         f.write(diagram_code)

#     return_code, output, cleaned_output = exec_command_in_terminal(f"python diagram.py", path)

#     base64_diagram = None
#     if return_code != 0:
#        base64_diagram = get_current_diagram(path)
#     else:
#         raise HTTPException(status_code=500, detail=f"Error generating diagram: {cleaned_output}")
    
#     return base64_diagram

# @app.get("/current_diagram")
# async def fetch_current_diagram():
#     """
#     Get the current diagram from the data directory.
#     """
#     path = "./data"
#     print("path", path)

#     result = {
#         "image": get_current_diagram(path)
#     }
#     return result

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