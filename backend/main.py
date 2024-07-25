import uvicorn
from fastapi import FastAPI, APIRouter

from backend.domain.question.api import router as question_router


def get_app():
    api_router = APIRouter(prefix="/api")
    api_router.include_router(question_router)

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
