from a2wsgi import ASGIMiddleware

# Import your FastAPI app.
from app.main import app

application = ASGIMiddleware(app)
