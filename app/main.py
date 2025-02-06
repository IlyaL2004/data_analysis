from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse

from app.api.visits_router import visits_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

parser_microservice = FastAPI(
    title="Parser_microservice"
)

parser_microservice.include_router(visits_router, prefix="/visits")

parser_microservice.mount("/static", StaticFiles(directory="frontend/static"), name="static")


templates = Jinja2Templates(directory="frontend/static")

@parser_microservice.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})