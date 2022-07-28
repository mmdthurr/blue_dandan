class Handler:
    def __init__(
            self,
            bot,
            update
    ):
        self.update = update
        self.bot = bot

    def update_handler(self, fil, callback):
        if fil:
            callback(
                update=self.update,
                bot=self.bot
            )
            return True

    def conv_handler(self, fil_callback: dict):
        self.update_handler(
            fil=fil_callback.get('fil'),
            callback=fil_callback.get('callback')
        )
