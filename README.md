# Cloud Ops MCP

A MCP server that leverages AI to analyze user queries. It then interfaces with cloud environments, using AWS CLI for AWS account analysis and kubectl for Kubernetes cluster interactions, to provide comprehensive details and insights.

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

4. Get an API key from Google Gemini AI studio
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

Note: This will work only with Agent mode in Copilot. Also use Claude Sonnet 3.7 for best results.

<p align="center">
  <video controls width="80%" title="Setup Video">
    <source src="assets/mcp-setup.mp4" type="video/mp4">
    Your browser does not support the video tag. 
    You can <a href="assets/mcp-setup.mp4">download the video here</a>.
  </video>
</p>

## Example use cases 

What are my top 5 most expensive AWS services this month?

List all EC2 instances with high CPU usage in the last 1 hour.

Give me the latest 10 AWS Health events

List all users with admin privileges and their last login.

Why is pod xyz in crashloopbackoff? (Kubernetes)

Any 5xx errors in the last 15 minutes from radio-laravel-stg ecs cluster?

Which S3 buckets had public access in the last week?


## Example video:

<p align="center">
  <video controls width="80%" title="Demo Video">
    <source src="assets/mcp-demo.mp4" type="video/mp4">
    Your browser does not support the video tag. 
    You can <a href="assets/mcp-demo.mp4">download the video here</a>.
  </video>
</p>



## Disclaimer

This is a proof of concept and not production ready. It is not intended to be used in production environments. It is only for demonstration purposes.

Also dont give aws profile with admin access to this mcp server. Create a new profile with limited access and use that profile to run the agent.

## TODO

- [ ] Add kubernetes support
- [ ] Add more tests
- [ ] Add more examples
- [ ] Add more documentation
- [ ] Add more error handling
- [ ] Add more logging
