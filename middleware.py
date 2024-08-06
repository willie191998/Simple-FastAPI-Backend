from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import logging
import pip._vendor.requests as requests
import os
import time

# Create FastAPI application
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Slack webhook URL from environment variable
SLACK_WEBHOOK_URL = os.getenv('SLACK_URL')


def notify_slack(message: str):
    """Send a notification to Slack."""
    payload = {
        "text": message
    }
    requests.post(SLACK_WEBHOOK_URL, json=payload)


async def log_errors(request: Request, call_next):
    """Middleware to log errors and notify Slack."""
    try:
        response = await call_next(request)
        return response
    except Exception as exc:
        # Log the error
        logger.error(f"Error occurred: {exc}, Path: {request.url.path}")
        
        # Send notification to Slack
        #notify_slack(f"Error occurred: {exc}, Path: {request.url.path}")
        
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"}
        )


class ProcessTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Start the process time
        start_time = time.time()

        # Call the next middleware or endpoint
        response = await call_next(request)

        # Calculate the process time
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)

        return response


# Add middlewares to the app
app.add_middleware(ProcessTimeMiddleware)
app.middleware("http")(log_errors)