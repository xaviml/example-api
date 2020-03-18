import logging

from fastapi import FastAPI

from . import version

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

# Logging version to se in production which version we are running
logging.info(f"Running example-api {version.__version__}")

app = FastAPI()


@app.get("/check", status_code=200)
async def check():
    """
    This endpoint is to check whether the service is up or not
    """
    return {"message": "example-api is alive!"}
