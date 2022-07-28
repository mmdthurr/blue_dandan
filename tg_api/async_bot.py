import httpx


def sendMessage(
        chat_id,
        text,
        parse_mode=None,
        entities=None,
        disable_web_page_preview=True,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None
):
    param = {
        'chat_id': chat_id,
        'text': text
    }
    if parse_mode:
        param['parse_mode'] = parse_mode
    if entities:
        param['entities'] = entities
    if disable_web_page_preview:
        param['disable_web_page_preview'] = disable_web_page_preview
    if reply_to_message_id:
        param['reply_to_message_id'] = reply_to_message_id
        param['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup:
        param['reply_markup'] = reply_markup
    return param


def answerInlineQuery(
        inline_query_id: str,
        results: list,
        cache_time: int = 0,
        is_personal: bool = None,
        next_offset: str = None,
        switch_pm_text: str = None,
        switch_pm_parameter: str = None
):
    param = {
        'inline_query_id': inline_query_id,
        'results': results,
    }
    if cache_time:
        param['cache_time'] = cache_time
    if is_personal:
        param['is_personal'] = is_personal
    if next_offset:
        param['next_offset'] = next_offset
    if switch_pm_text and switch_pm_parameter:
        param['switch_pm_text'] = switch_pm_text
        param['switch_pm_parameter'] = switch_pm_parameter
    return param


def copyMessage(
        chat_id,
        from_chat_id,
        message_id: int,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = True,
        reply_markup=None
):
    param = {
        'chat_id': chat_id,
        'from_chat_id': from_chat_id,
        'message_id': message_id,
        'allow_sending_without_reply': allow_sending_without_reply
    }
    if reply_to_message_id:
        param['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        param['reply_markup'] = reply_markup
    return param


def getChat(
        chat_id
):
    param = {
        'chat_id': chat_id
    }
    return param


def deleteMessage(
        chat_id,
        message_id
):
    param = {
        'chat_id': chat_id,
        'message_id': message_id
    }
    return param


def answerCallbackQuery(
        callback_query_id: str,
        text: str = None,
        show_alert: bool = None,
        url: str = None,
        cache_time: int = None
):
    param = {
        'callback_query_id': callback_query_id
    }
    if text:
        param['text'] = text
    if show_alert:
        param['show_alert'] = show_alert
    if url:
        param['url'] = url
    if cache_time:
        param['cache_time'] = cache_time
    return param


def editMessageReplyMarkup(
        chat_id=None,
        message_id=None,
        inline_message_id=None,
        reply_mark=None,
):
    param = {}
    if chat_id and message_id:
        param['chat_id'] = chat_id
        param['message_id'] = message_id
    if inline_message_id:
        param['inline_message_id'] = inline_message_id
    if reply_mark:
        param['reply_markup'] = reply_mark
    return param

class Bot:
    def __init__(
            self,
            token,
            session=httpx.AsyncClient()
    ):
        self.token = token
        self.session = session

    async def request(
            self,
            method_dict,
            method_slug
    ):
        response = await self.session.post(
            f'https://api.telegram.org/bot{self.token}/{method_slug}',
            json=method_dict
        )
        # if response.status_code == 400:
        #     raise BadRequest
        # elif response.status_code == 401:
        #     raise Unauthorized
        # elif response.status_code == 403:
        #     raise Forbidden
        # elif response.status_code == 404:
        #     raise NotFound
        # elif response.status_code == 420:
        #     raise Flood
        # elif response.status_code in range(300, 600):
        #     raise SeeOther
        return response
