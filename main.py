from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
import json
from pydantic import BaseSettings
from dotenv import load_dotenv
from scrapper import Scrapper

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

class Settings(BaseSettings):
    app_name: str = "Sinouns API"
    port_default: int = 8000

settings = Settings()
app = FastAPI()

print("       SERVICE: {}".format(settings.app_name))


@app.get("/")
async def route():
    try:
        return JSONResponse(status_code=200, content={"message": "Hello World"})

    except ValueError as e:
        return JSONResponse(status_code=500, content={"message": "Error: {}".format(e)})

    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Error: {}".format(e)})

@app.post("/word/")
async def get_word(request: Request, country: str):
    try:
        body = await request.body()
        body = json.loads(body)

        if country == "" or country == None:
            return JSONResponse(status_code=400, content={"message": "País não informado"})

        if body["word"] == "" or body["word"] == None:
            return JSONResponse(status_code=400, content={"message": "Palavra não informada"})

        scrapper = Scrapper(body["word"], country)

        if scrapper.sinons == []:
            return JSONResponse(status_code=404, content={"message": "Não existem sinonimos para a palavra informada"})
        else:
            return JSONResponse(status_code=200, content={"message": scrapper.sinons})

    except ValueError as e:
        return JSONResponse(status_code=500, content={"message": "Error: {}".format(e)})

    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Error: {}".format(e)})


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)