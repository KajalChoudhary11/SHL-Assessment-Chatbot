from fastapi import FastAPI

from APP.controllers import router

app = FastAPI()

app.include_router(router)