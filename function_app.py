import azure.functions as func

from fastapi import FastAPI
from blueprints.fast_blueprints import bp as http_endpoints

app = FastAPI(title="Azure functions fastapi example", description="Fastapi project for azure functions", version="0.1.0")

app.include_router(http_endpoints)

azure_app = func.AsgiFunctionApp(app=app, http_auth_level=func.AuthLevel.ANONYMOUS)