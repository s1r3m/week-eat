from fastapi import APIRouter, Response

router = APIRouter()


@router.get('/ping')
async def ping() -> Response:
    return Response(content='pong', status_code=200)
