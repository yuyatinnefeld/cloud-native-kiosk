import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import make_asgi_app
from prometheus_fastapi_instrumentator import Instrumentator

from app.routes.info import routes as info_routes


instrumentator = Instrumentator(
    should_group_status_codes=True,
    should_ignore_untemplated=True,
    should_respect_env_var=True,
    should_instrument_requests_inprogress=True,
    excluded_handlers=["/metrics"],
    env_var_name="ENABLE_METRICS",
    inprogress_name="fastapi_inprogress",
    inprogress_labels=True,
)

DB_TYPE = os.getenv("DB_TYPE")
APP_NAME = os.getenv("APP_NAME")

app = FastAPI(
    title="simple fastapi backend service",
    version="1.0.0",
    redoc_url=None,
    openaip_url=None,
)

instrumentator.instrument(app).expose(app, include_in_schema=False, should_gzip=False)
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

origins = [
    "http://test-yuya.com",
    "http://ckn.com",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    """
    This function returns a dictionary with a single key-value pair.
    The key is "service" and the value is "backend application".
    This function is used to test the API documentation.
    """
    if APP_NAME:
        return {"service": APP_NAME}
    else:
        return {"service": "python fastapi simple app"}


@app.get("/health_backend")
def health_check():
    """
    This function is used for the k8s health check
    and returns a string that says "Health check backend👌
    """
    return "Health check backend👌"


app.include_router(info_routes.router)

if DB_TYPE == "LOCAL_POSTGRES":
    from app.routes.items import routes as items_routes
    from app.routes.users import routes as users_routes

    app.include_router(items_routes.router)
    app.include_router(users_routes.router)
