from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import json
from pydantic import BaseSettings
from dotenv import load_dotenv

class Settings(BaseSettings):
    app_name: str = "Sinouns API"
    port_default: int = 8000

settings = Settings()
app = FastAPI()

print("       SERVICE: {}".format(settings.app_name))


@app.get("/")
def route():
    try:
        return JSONResponse(status_code=200, content={"message": "Hello World"})

    except ValueError as e:
        return JSONResponse(status_code=500, content={"message": "Error: {}".format(e)})

    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Error: {}".format(e)})

@app.post("/word/")
async def get_word(request: Request, country: str | None = None):
    try:
        body = await request.body()
        body = json.loads(body)

        return JSONResponse(status_code=200, content={"message": body, "country": country})

    except ValueError as e:
        return JSONResponse(status_code=500, content={"message": "Error: {}".format(e)})

    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Error: {}".format(e)})