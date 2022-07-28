class InlineQueryResult:
    def __init__(self, inline_id):
        self.inline_id = inline_id

    def article(
            self,
            title,
            input_message_content,
            reply_markup=None,
            url=None,
            hide_url=None,
            description=None,
            thumb_url=None,
    ):
        result = {
            'type': 'article',
            'id': self.inline_id,
            'title': title,
            'input_message_content': input_message_content
        }
        if reply_markup:
            result['reply_markup'] = reply_markup
        if url:
            result['url'] = url
        if hide_url:
            result['hide_url'] = hide_url
        if description:
            result['description'] = description
        if thumb_url:
            result['thumb_url'] = thumb_url
        return result

    def photo(
            self,
            photo_url,
            thumb_url,
            photo_width=512,
            photo_height=512,
            title=None,
            description=None,
            caption=None,
            parse_mode=None,
            reply_markup=None,
            input_message_content=None
    ):
        result = {
            'type': 'photo',
            'id': self.inline_id,
            'photo_url': photo_url,
            'thumb_url': thumb_url,
            'photo_width': photo_width,
            'photo_height': photo_height
        }
        if title:
            result['title'] = title
        if description:
            result['description'] = description
        if caption:
            result['caption'] = caption
        if parse_mode:
            result['parse_mode'] = parse_mode
        if reply_markup:
            result['reply_markup'] = reply_markup
        if input_message_content:
            result['input_message_content'] = input_message_content
        return result

    def cached_voice(
            self,
            voice_file_id,
            title,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            reply_markup=None,
            input_message_content=None
    ):
        result = {
            'type': 'voice',
            'id': self.inline_id,
            'voice_file_id': voice_file_id,
            'title': title,
        }
        if caption:
            result['caption'] = caption
        if parse_mode:
            result['parse_mode'] = parse_mode
        if caption_entities:
            result['caption_entities'] = caption_entities
        if reply_markup:
            result['reply_markup'] = reply_markup
        if input_message_content:
            result['input_message_content'] = input_message_content
        return result

    def gif(
            self,
            gif_url,
            thumb_url,
            gif_width=512,
            gif_height=512,
            title=None,
            caption=None,
            parse_mode=None,
            reply_markup=None,
    ):
        result = {
            'type': 'gif',
            'id': self.inline_id,
            'gif_url': gif_url,
            'thumb_url': thumb_url,
            'gif_width': gif_width,
            'gif_height': gif_height
        }
        if title:
            result['title'] = title
        if caption:
            result['caption'] = caption
        if parse_mode:
            result['parse_mode'] = parse_mode
        if reply_markup:
            result['reply_markup'] = reply_markup
        return result

    def cached_video(
            self,
            video_file_id,
            title,
            description=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            reply_markup=None
    ):
        result = {
            'type': 'video',
            'id': self.inline_id,
            'video_file_id': video_file_id,
            'title': title
        }
        if description:
            result['description'] = description
        if caption:
            result['caption'] = caption
        if parse_mode:
            result['parse_mode'] = parse_mode
        if caption_entities:
            result['caption_entities'] = caption_entities
        if reply_markup:
            result['reply_markup'] = reply_markup
        return result

    def cached_audio(
            self,
            audio_file_id,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            reply_markup=None
    ):
        result = {
            'type': 'audio',
            'id': self.inline_id,
            'audio_file_id': audio_file_id,
        }
        if caption:
            result['caption'] = caption
        if parse_mode:
            result['parse_mode'] = parse_mode
        if caption_entities:
            result['caption_entities'] = caption_entities
        if reply_markup:
            result['reply_markup'] = reply_markup
        return result

    def cached_document(
            self,
            title,
            document_file_id,
            description=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            reply_markup=None,
    ):
        result = {
            'type': 'document',
            'id': self.inline_id,
            'title': title,
            'document_file_id': document_file_id,
        }
        if description:
            result['description'] = description
        if caption:
            result['caption'] = caption
        if parse_mode:
            result['parse_mode'] = parse_mode
        if caption_entities:
            result['caption_entities'] = caption_entities
        if reply_markup:
            result['reply_markup'] = reply_markup
        return result

    def cached_gif(
            self,
            gif_file_id,
            title=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            reply_markup=None
    ):
        result = {
            'type': 'gif',
            'id': self.inline_id,
            'gif_file_id': gif_file_id,
        }
        if title:
            result['title'] = title
        if caption:
            result['caption'] = caption
        if parse_mode:
            result['parse_mode'] = parse_mode
        if caption_entities:
            result['caption_entities'] = caption
        if reply_markup:
            result['reply_markup'] = reply_markup
        return result

    def cached_mpeg4_gif(
            self,
            mpeg4_file_id,
            title=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            reply_markup=None
    ):
        result = {
            'type': 'mpeg4_gif',
            'id': self.inline_id,
            'mpeg4_file_id': mpeg4_file_id
        }

        if title:
            result['title'] = title
        if caption:
            result['caption'] = caption
        if parse_mode:
            result['parse_mode'] = parse_mode
        if caption_entities:
            result['caption_entities'] = caption_entities
        if reply_markup:
            result['reply_markup'] = reply_markup

    def cached_photo(
            self,
            photo_file_id,
            title=None,
            description=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            reply_markup=None
    ):
        result = {
            'type': 'photo',
            'id': self.inline_id,
            'photo_file_id': photo_file_id
        }
        if title:
            result['title'] = title
        if description:
            result['description'] = description
        if caption:
            result['caption'] = caption
        if parse_mode:
            result['parse_mode'] = parse_mode
        if caption_entities:
            result['caption_entities'] = caption_entities
        if reply_markup:
            result['reply_markup'] = reply_markup
        return result

    def cached_sticker(
            self,
            sticker_file_id,
            reply_markup=None
    ):
        result = {
            'type': 'sticker',
            'id': self.inline_id,
            'sticker_file_id': sticker_file_id,
        }
        if reply_markup:
            result['reply_markup'] = reply_markup
        return result
