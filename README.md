# Weather API

A FastAPI application that provides current weather information.

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

4. Get an API key from [OpenWeatherMap](https://openweathermap.org/api)
5. Create a `.env` file in the root directory with your API key:
```
OPENWEATHER_API_KEY=your_api_key_here
```

## Running the application

Start the application with:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Endpoints

- `GET /`: Welcome message
- `GET /weather/{city}`: Get current weather for a city
  - Query Parameters:
    - `country_code` (optional): ISO 3166 country code

### Example

```
GET /weather/London?country_code=GB
```

Response:
```json
{
  "location": "London, GB",
  "temperature": 15.5,
  "description": "scattered clouds",
  "humidity": 72,
  "wind_speed": 3.6
}
```

## Documentation

Interactive API documentation is available at:
- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)


brew install graphviz