import uvicorn
from fastapi import FastAPI, APIRouter


def get_app():
    api_router = APIRouter(prefix="/api")

    app = FastAPI()
    app.include_router(api_router)

    return app


def main():
    uvicorn.run(
        "backend.main:get_app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        factory=True
    )


if __name__ == "__main__":
    main()
