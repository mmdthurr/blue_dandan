class InlineKeyboardMarkup:
    def __init__(self, inline_keyboard: list):
        self.inline_keyboard = inline_keyboard

    @classmethod
    def inline_keyboard_markup_dec(cls, inline_keyboard_buttons: dict):
        if inline_keyboard_buttons:
            return cls(
                inline_keyboard=inline_keyboard_buttons.get('inline_keyboard')
            )
