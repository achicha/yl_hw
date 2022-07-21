import redis
import uvicorn
from fastapi import FastAPI

from src.posts.api import router as posts_router
from src.users.api import router as users_router
from src.auth.api import router as auth_router
from src.core import config
from src.db import cache, redis_cache

app = FastAPI(
    # Конфигурируем название проекта. Оно будет отображаться в документации
    title=config.PROJECT_NAME,
    version=config.VERSION,
    # Адрес документации в красивом интерфейсе
    docs_url="/api/openapi",
    redoc_url="/api/redoc",
    # Адрес документации в формате OpenAPI
    openapi_url="/api/openapi.json",
)


@app.get("/")
def root():
    return {"service": config.PROJECT_NAME, "version": config.VERSION}


@app.on_event("startup")
def startup():
    """Подключаемся к базам при старте сервера"""
    cache.cache = redis_cache.CacheRedis(
        cache_instance=redis.Redis(
            host=config.REDIS_HOST, port=config.REDIS_PORT, max_connections=10
        )
    )
    # cache.active_tokens = redis_cache.CacheRedis(
    #     cache_instance=redis.Redis(
    #         host=config.REDIS_HOST, port=config.REDIS_PORT, db=1, max_connections=10, decode_responses=True
    #     )
    # )
    # cache.blocked_tokens = redis_cache.CacheRedis(
    #     cache_instance=redis.Redis(
    #         host=config.REDIS_HOST, port=config.REDIS_PORT, db=2, max_connections=10, decode_responses=True
    #     )
    # )


@app.on_event("shutdown")
def shutdown():
    """Отключаемся от баз при выключении сервера"""
    cache.cache.close()


# Подключаем роутеры к серверу
app.include_router(router=auth_router, prefix="/api/v1")
app.include_router(router=users_router, prefix="/api/v1/users")
app.include_router(router=posts_router, prefix="/api/v1/posts")

if __name__ == "__main__":
    # Приложение может запускаться командой
    # `uvicorn main:app --host 0.0.0.0 --port 8000`
    # но чтобы не терять возможность использовать дебагер,
    # запустим uvicorn сервер через python
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
    )
