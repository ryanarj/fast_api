from routers.core.FastApiService import FastApiService
from routers.players import players

app = FastApiService().app()
app.include_router(players.router)
