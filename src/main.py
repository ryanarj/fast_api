from routers.core.FastApiService import FastApiService
from routers.prompts import prompts
#from routers.players import players

app = FastApiService().app()
app.include_router(prompts.router)
