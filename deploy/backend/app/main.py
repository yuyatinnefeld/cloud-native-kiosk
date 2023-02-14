from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.routes.info import routes as info_routes

# from app.routes.items import routes as items_routes
# from app.routes.users import routes as users_routes


app = FastAPI(
    title="cloud native kiosk backend",
    version="1.1.0",
    redoc_url=None,
    openaip_url=None,
)

origins = [
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
    return {"service": "backend application"}


@app.get("/health_backend")
def health_check():
    """This function is used for the k8s health check and returns a string that says "Health check backend👌"""
    return "Health check backend👌"


app.include_router(info_routes.router)

# sqlite db with k8s not working
# app.include_router(items_routes.router)
# app.include_router(users_routes.router)
