from fastapi import APIRouter, status, Query
from fastapi.responses import Response, JSONResponse

import logging
from typing import Annotated, Optional

bp = APIRouter()


@bp.get("/hello_world", tags=["template"])
def hello_world(
    name: Annotated[
        Optional[str],
        Query(
            description="The name of the person to say hello to.",
        ),
    ] = None
):
    logging.info("FastAPI function processed a request.")

    name = name or "world"

    return Response(f"Hello {name}", status_code=200)

@bp.get("/root_index")
async def root_index():
    data = {'message': 'azure function is running'}
    return JSONResponse(status_code=status.HTTP_200_OK, content=data)

@bp.get("/health")
async def health_check():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "ok"})