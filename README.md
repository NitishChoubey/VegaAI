# VegaAI - AI-Powered Travel Planning Service

Assistive AI trip planning service powered by Google Gemini.

## Features

- 🤖 AI-powered activity suggestions using Google Gemini
- 🌍 Context-aware recommendations based on location, budget, and preferences
- 🛡️ Built-in safety rules and constraints
- 📱 REST API ready for mobile app integration
- ⚡ Fast and scalable FastAPI backend

## Local Development

### Prerequisites

- Python 3.11+
- Google Gemini API key

### Setup

1. Clone the repository
2. Create virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirement.txt
   ```

4. Create `.env` file (copy from `.env.example`):
   ```bash
   cp .env.example .env
   ```

5. Add your Gemini API key to `.env`:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

6. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`

## API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### `POST /api/ai/vega/suggest`

Generate AI travel suggestions.

**Request Body:**
```json
{
  "trip_id": "string",
  "city": "string",
  "country": "string",
  "day": 1,
  "time_slot": "morning",
  "remaining_budget": 1000,
  "preferences": ["culture", "food"]
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "suggestions": [
      {
        "activity": "Visit Temple",
        "location": "Downtown",
        "estimated_cost": 50,
        "estimated_duration": "2 hours",
        "reason": "Cultural experience...",
        "tips": ["Wear modest clothing"]
      }
    ]
  }
}
```

## Deployment on Render

1. Push your code to GitHub/GitLab
2. Connect repository to Render
3. Render will auto-detect `render.yaml` configuration
4. Add `GEMINI_API_KEY` environment variable in Render dashboard
5. Deploy!

Your service will be available at: `https://your-service.onrender.com`

## Environment Variables

- `GEMINI_API_KEY` - Your Google Gemini API key (required)
- `ALLOWED_ORIGINS` - Comma-separated list of allowed CORS origins (default: *)

## Architecture

- **FastAPI**: Modern, fast web framework
- **Google Gemini**: AI model for intelligent suggestions
- **Pydantic**: Data validation and schemas
- **Uvicorn**: ASGI server

## Security

- Never commit `.env` file or API keys
- Use environment variables for all secrets
- Restrict CORS origins in production
- Enable rate limiting for production use

## License

MIT
