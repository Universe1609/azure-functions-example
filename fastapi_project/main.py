from fastapi import FastAPI, status
from fastapi.responses import JSONResponse



app = FastAPI()

@app.get("/root_index")
async def root_index():
    data = {'message': 'azure function is running'}
    return JSONResponse(status_code=status.HTTP_200_OK, content=data)

@app.get("/health")
async def health_check():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "ok"})