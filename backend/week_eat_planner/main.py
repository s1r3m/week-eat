from fastapi import FastAPI

from week_eat_planner.api.routes import router


app = FastAPI()
app.include_router(router)
