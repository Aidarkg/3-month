import os
from aiogram import types
from aiogram.dispatcher import Dispatcher
from pytube import YouTube
from config import bot
import logging
from pytube.exceptions import AgeRestrictedError

logging.basicConfig(level=logging.INFO)


async def process_audio(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Пожалуйста, отправьте мне ссылку на видео с YouTube.")


async def download_yt_audio(message: types.Message):
    video_url = message.text

    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        save_path = 'C:/Users/adija/OneDrive/Рабочий стол/3 - month/media/audio'
        audio_stream.download(output_path=save_path, filename=f'{yt.title}.mp4')

        audio_file = os.path.join(save_path, f"{yt.title}.mp4")
        with open(audio_file, "rb") as audio:
            await bot.send_audio(
                chat_id=message.chat.id,
                audio=audio
            )
        os.remove(audio_file)

    except AgeRestrictedError:
        await bot.send_message(
            chat_id=message.chat.id,
            text="Видео ограничено по возрасту и не может быть загружено без аутентификации. Пожалуйста, предоставьте мне другую ссылку."
        )


def register_audio_handler(dp: Dispatcher):
    dp.register_callback_query_handler(
        process_audio,
        lambda call: call.data == "audio_download_button")
    dp.register_message_handler(
        download_yt_audio, content_types=types.ContentTypes.TEXT)
