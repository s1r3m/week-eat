from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get('/ping', response_class=JSONResponse)
async def ping() -> JSONResponse:
    return JSONResponse({'state': 'pong'}, headers={'content-type': 'application/json'})
