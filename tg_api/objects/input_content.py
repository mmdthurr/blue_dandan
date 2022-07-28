def text(
        message_text: str,
        parse_mode: str = None,
        entities: list = None,
        disable_web_page_preview: bool = None
):
    input_text = {
        'message_text': message_text,
    }
    if parse_mode:
        input_text['parse_mode'] = parse_mode
    if entities:
        input_text['entities'] = entities
    if disable_web_page_preview:
        input_text['disable_web_page_preview'] = disable_web_page_preview

    return input_text
