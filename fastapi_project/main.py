from fastapi import FastAPI
from fastapi_project.api import health, root_index


app = FastAPI()

app.include_router(root_index.router)
app.include_router(health.router)
    