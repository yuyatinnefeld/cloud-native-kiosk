from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.routes.info import routes as info_routes

# from app.routes.items import routes as items_routes
# from app.routes.users import routes as users_routes


app = FastAPI(
    title="cloud native kiosk backend",
    version="1.0.0",
    redoc_url=None,
    openaip_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://backend.ckn.com"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"hello": "backend world"}


@app.get("/health")
def health_check():
    return "Health check backend👌"


app.include_router(info_routes.router)

# sqlite db with k8s not working
# app.include_router(items_routes.router)
# app.include_router(users_routes.router)
