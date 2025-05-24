# Python FastAPI Tutorial Deploy on Blossom

[![Blossom Badge](https://img.boltops.com/images/blossom/logos/blossom-readme.png)](https://blossom-cloud.com)

A ready-to-deploy Python FastAPI app to get you started quickly on [Blossom](https://blossom-cloud.com).

## Quick Start

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or `venv/Scripts/activate` on Windows
source venv/bin/activate.fish  # fish shell

# Install dependencies
pip install -r requirements.txt

# Run the app
fastapi dev main.py
# or
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000` in your browser to see the demo application.

<details>
<summary>Additional Information</summary>

### Environment Variables
- `PORT`: Change the port (default: 8000)

### API Endpoints
```bash
# Get a greeting
curl http://localhost:8000/api/hello?name=John

# Echo a message
curl -X POST -H "Content-Type: application/json" \
     -d '{"message":"Hello"}' http://localhost:8000/api/echo

# Get API Documentation
curl http://localhost:8000/docs  # Swagger UI
curl http://localhost:8000/redoc # ReDoc
```
</details>
