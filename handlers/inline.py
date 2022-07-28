from beanie.operators import RegEx
from .statics import Statics
from . import (
    BlueDandan,
    Recent,
    User,
    Bot,
    answerInlineQuery,
    Update,
    InlineQueryResult,
    inline_markup,
)


class InlineTemp:
    def __init__(self,
                 file_id: str,
                 file_unique_id: str,
                 type_of: str,
                 title,
                 description
                 ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.type_of = type_of
        self.title = title
        self.description = description


class InlineHandler:
    def __init__(self, update: Update, bot: Bot, user: User):
        self.update = update
        self.bot = bot
        self.user = user
        self.st = Statics(self.user.lang)

    @property
    def current_skip(self):
        if offset := self.update.inline_query.offset:
            return int(offset)
        else:
            return 0

    async def parse_query(self):
        q = self.update.inline_query.query
        raw_res = list()

        fil_lis = []
        if q.startswith('.id'):
            fil_lis.append(BlueDandan.file_unique_id == q[3:].strip())
        elif q.startswith('.d'):
            fil_lis.extend(
                [
                    RegEx('description', q[2:].strip()),
                    BlueDandan.active == True
                ]
            )
        else:
            if q:
                if q.startswith('+'):
                    q = q[1:].strip()
                fil_lis.append(RegEx('title', q))
            fil_lis.append(BlueDandan.active == True)

        if self.current_skip == 0 and not q:
            recent_ojb = Recent.find(
                Recent.owner_id == self.update.current_user.user_id,
                Recent.active == True
            ).sort(
                '-last_use_date'
            ).limit(5)
            raw_res.extend(
                [InlineTemp(
                    file_id=r.yadeh.get('file_id'),
                    file_unique_id=r.yadeh.get('file_unique_id'),
                    type_of=r.yadeh.get('type_of'),
                    title=r.yadeh.get('title'),
                    description=r.yadeh.get('description')
                ) async for r in recent_ojb]
            )
        raw_res.extend(
            [InlineTemp(file_id=y.file_id,
                        file_unique_id=y.file_unique_id,
                        type_of=y.type_of,
                        title=y.title,
                        description=y.description
                        )
             async for y in
             BlueDandan.find(*fil_lis).sort(self.user.order).skip(self.current_skip).limit(20)]
        )

        return raw_res

    @staticmethod
    def make_result(raw_res: list[InlineTemp], verbose: bool = False):
        result = []
        if raw_res:
            for y in raw_res:
                if y.type_of == 'audio':
                    audio_obj = InlineQueryResult(y.file_unique_id).cached_audio(
                        audio_file_id=y.file_id
                    )
                    if audio_obj not in result:
                        result.append(audio_obj)

                elif y.type_of == 'document':
                    document_obj = InlineQueryResult(y.file_unique_id).cached_document(
                        title=y.title,
                        document_file_id=y.file_id,
                        reply_markup=inline_markup(
                            [[{'text': '▶️', 'switch_inline_query': f'.id {y.file_unique_id}'}]]
                        ) if verbose else None
                    )
                    if document_obj not in result:
                        result.append(document_obj)

                elif y.type_of == 'animation':
                    animation_obj = InlineQueryResult(y.file_unique_id).cached_gif(
                        gif_file_id=y.file_id,
                        reply_markup=inline_markup(
                            [[{'text': '▶️', 'switch_inline_query': f'.id {y.file_unique_id}'}]]
                        ) if verbose else None
                    )
                    if animation_obj not in result:
                        result.append(animation_obj)

                elif y.type_of == 'photo':
                    photo_obj = InlineQueryResult(y.file_unique_id).cached_photo(
                        photo_file_id=y.file_id,
                        title=y.title if verbose else None,
                        reply_markup=inline_markup(
                            [[{'text': '▶️', 'switch_inline_query': f'.id {y.file_unique_id}'}]]
                        ) if verbose else None
                    )
                    if photo_obj not in result:
                        result.append(
                            photo_obj
                        )

                elif y.type_of == 'sticker':
                    sticker_obj = InlineQueryResult(y.file_unique_id).cached_sticker(
                        sticker_file_id=y.file_id,
                        reply_markup=inline_markup(
                            [[{'text': '▶️', 'switch_inline_query': f'.id {y.file_unique_id}'}]]
                        ) if verbose else None
                    )
                    if sticker_obj not in result:
                        result.append(
                            sticker_obj
                        )

                elif y.type_of == 'video':
                    video_obj = InlineQueryResult(y.file_unique_id).cached_video(
                        video_file_id=y.file_id,
                        title=y.title,
                        reply_markup=inline_markup(
                            [[{'text': '▶️', 'switch_inline_query': f'.id {y.file_unique_id}'}]]
                        ) if verbose else None
                    )
                    if video_obj not in result:
                        result.append(
                            video_obj
                        )

                elif y.type_of == 'voice':
                    voice_obj = InlineQueryResult(y.file_unique_id).cached_voice(
                        voice_file_id=y.file_id,
                        title=y.title,
                        reply_markup=inline_markup(
                            [[{'text': '▶️', 'switch_inline_query': f'.id {y.file_unique_id}'}]]
                        ) if verbose else None
                    )
                    if voice_obj not in result:
                        result.append(
                            voice_obj
                        )
        return result

    async def answer_inline(self):
        await self.bot.request(
            method_dict=answerInlineQuery(
                inline_query_id=self.update.inline_query.inline_query_id,
                cache_time=1,
                results=InlineHandler.make_result(
                    raw_res=await self.parse_query(),
                    verbose=True if self.update.inline_query.query.startswith('+') else False),
                is_personal=True,
                next_offset=str(self.current_skip + 20),
                switch_pm_text=self.st.query('switch_pm_txt'),
                switch_pm_parameter='mine'
            ),
            method_slug='answerInlineQuery'
        )
