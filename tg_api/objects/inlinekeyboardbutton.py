class InlineKeyboardButton:
    def __init__(
            self,
            text: str,
            url: str = None,
            callback_data: str = None
    ):
        self.text = text
        self.url = url
        self.callback_data = callback_data

    @classmethod
    def inline_keyboard_button_dec(cls, keyboard: dict):
        return cls(
            text=keyboard.get('text'),
            url=keyboard.get('url'),
            callback_data=keyboard.get('callback_data')
        )

    def __repr__(self):
        button = {
            'text': self.text
        }
        if self.url:
            button['url'] = self.url
        if self.callback_data:
            button['callback_data'] = self.callback_data
        return button
