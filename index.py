from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.note import note 

app = FastAPI()


app.include_router(note)