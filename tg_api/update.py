from .message import Message
from .inlinequery import InlineQuery
from .choseninlineresult import ChosenInlineResult
from .callbackquery import CallbackQuery


class Update:
    def __init__(
            self,
            update_id: int,
            message: Message,
            inline_query: InlineQuery,
            chosen_inline_result: ChosenInlineResult,
            callback_query: CallbackQuery
    ):
        self.update_id = update_id
        self.message = message
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query

    @property
    def current_update(self):
        if self.message:
            return self.message
        elif self.inline_query:
            return self.inline_query
        elif self.chosen_inline_result:
            return self.chosen_inline_result
        elif self.callback_query:
            return self.callback_query

    @property
    def current_user(self):
        if self.current_update:
            return self.current_update.from_user

    @classmethod
    def dec_update(cls, update: dict):
        return cls(
            update_id=update.get('update_id'),
            message=Message.message_dec(update.get('message')),
            inline_query=InlineQuery.inline_query_dec(update.get('inline_query')),
            chosen_inline_result=ChosenInlineResult.chosen_inline_result_dec(update.get('chosen_inline_result')),
            callback_query=CallbackQuery.callback_query_dec(update.get('callback_query'))
        )
