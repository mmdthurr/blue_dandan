from fastapi import FastAPI, Body
import motor.motor_asyncio
from beanie import init_beanie
from handlers import User, BlueDandan, Recent, Bot, Update, dispatcher, Statics


class Context:
    def __init__(self):
        self.user_data = dict()
        self._updates_ids = list()

    def update_id_is_used(self, update_id):
        if update_id in self._updates_ids:
            if len(self._updates_ids) == 10:
                self._updates_ids.clear()
            return True
        else:
            self._updates_ids.append(update_id)
            return False


app = FastAPI()
context = Context()


@app.on_event('startup')
async def init_db():
    await init_beanie(
        database=motor.motor_asyncio.AsyncIOMotorClient("mongodb://127.0.0.1:27017").bluedandan,
        document_models=[User, BlueDandan, Recent]
    )


@app.get("/")
async def root():
    return {'blue': 1}


@app.post('/tg/hook/{token}', status_code=200)
async def hook_dispatcher(token: str, up: dict = Body()):
    if token == Statics.Token:
        update = Update.dec_update(up)
        if not context.update_id_is_used(update_id=update.update_id):
            await dispatcher(
                update=update,
                bot=Bot(token=token),
                context=context.user_data
            )
        return 200
