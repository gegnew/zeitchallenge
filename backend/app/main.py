from app.api import api_router
from app.config.settings import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_app(settings):
    app = FastAPI(
        title=settings.PROJECT_NAME, openapi_url=f"{settings.API_VERSION}/openapi.json"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix=settings.API_VERSION)

    return app


app = get_app(settings)
