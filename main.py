from fastapi import FastAPI
from routes.players import router as router_player
from routes.games import router as router_game

app = FastAPI()


app.include_router(router_player)
app.include_router(router_game)


@app.get("/")
def read_root():
    return {"Hello": "Player"}
