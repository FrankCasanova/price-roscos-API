from fastapi import APIRouter

from .views import get_prices
from .views import index

router = APIRouter(prefix="/api")

router.add_api_route(
    path="/",
    endpoint=index,
    name="index",
    status_code=200,
    response_description="Welcome to the API",
    methods=["GET"],
    summary="Welcome to the API",
    tags=["index"],
)

router.add_api_route(
    path="/prices",
    endpoint=get_prices,
    name="get_prices",
    status_code=200,
    response_description="Prices",
    methods=["GET"],
    summary="Get prices",
    tags=["prices"],
)
