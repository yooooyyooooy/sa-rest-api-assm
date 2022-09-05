from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from routes import restaurant_member


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="REST API Assignment",
        version="1.0.0",
        description=f"API document for Software Architecture: Rest API Assignment [6231354721 Ratchanon]",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = FastAPI()
app.openapi = custom_openapi
app.include_router(restaurant_member.router)
