class Filter:
    def __init__(self, update):
        self.update = update

    def user_filter(self, users):
        if self.update.current_user.user_id in users:
            return True

    def command_filter(self, command=None):
        if self.update.message.entities:
            for entity in self.update.message.entities:
                if entity.get('type') == 'bot_command':
                    if command:
                        if self.update.message.text.startswith(command):
                            return True
                    else:
                        return True
                    break

    def text_message_filter(self, txt=None):
        if self.update.message.text:
            if txt:
                if txt == self.update.message.text:
                    return True
            else:
                return True

    @property
    def video(self):
        if self.update.message:
            if self.update.message.video:
                return True

    @property
    def photo(self):
        if self.update.message:
            if self.update.message.photo:
                return True

    @property
    def audio(self):
        if self.update.message:
            if self.update.message.audio:
                return True

    @property
    def voice(self):
        if self.update.message:
            if self.update.message.voice:
                return True
