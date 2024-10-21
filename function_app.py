import azure.functions as func
from fastapi.responses import JSONResponse
from fastapi import FastAPI, status

fastapi_app = FastAPI()
app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)

@fastapi_app.get("/root_index")
async def root_index():
    data = {'message': 'azure function is running'}
    return JSONResponse(status_code=status.HTTP_200_OK, content=data)

@fastapi_app.get("/health")
async def health_check():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "ok"})