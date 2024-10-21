from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/root_index")
async def root_index():
    data = {'message': 'azure function is running'}
    return JSONResponse(status_code=status.HTTP_200_OK, content=data)
