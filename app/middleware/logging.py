from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware que loggea el método y ruta de cada petición HTTP."""
    
    async def dispatch(self, request: Request, call_next):
        # Log antes de procesar la petición
        print(f"{request.method} {request.url.path}")
        
        # Procesar la petición
        response = await call_next(request)
        
        return response