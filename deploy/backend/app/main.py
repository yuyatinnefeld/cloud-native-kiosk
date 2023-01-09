from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.routes.info import routes as info_routes
from app.routes.item import routes as item_routes


app = FastAPI(
    title = "cloud native kiosk backend",
    version = "1.0.0",
    redoc_url = None,
    openaip_url = None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://backend.c-native-kiosk.com"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"hello": "world"}

app.include_router(info_routes.router)
app.include_router(item_routes.router)