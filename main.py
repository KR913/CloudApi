from fastapi import *
from inroute import in_api
from outroute import out_api

app = FastAPI()

app.include_router(in_api.router)
app.include_router(out_api.router)

