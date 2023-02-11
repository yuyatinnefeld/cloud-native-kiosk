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
    "http://ckn.com/api",
    "http://localhost:8080",
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
    return {"service": "backend application"}


@app.get("/health_backend")
def health_check():
    return "Health check backend👌"


app.include_router(info_routes.router)

# sqlite db with k8s not working
# app.include_router(items_routes.router)
# app.include_router(users_routes.router)
