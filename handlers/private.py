from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Merhaba Ben **{bn}** !!
Grubunuzun sesli sohbetinde müzik çalabilrim 😉
Şu anda desteklediğim komutlar şunlardır:
🍀 /o - __Yanıtlanan ses dosyasını veya YouTube videosunu bağlantı üzerinden çalar.__
🍀 /d - __Sesli Sohbet Müziğini Duraklat.__
🍀 /s - __Sesli Sohbet Müziğine Devam Et.__
🍀 /a - __Sesli Sohbette Çalan Geçerli Müziği Atlar.__
🍀 /b - __Sırayı temizler ve Sesli Sohbet Müziği'ni sona erdirir.__
🍀 /i - __Müziği indirip gruba gönderir. Örnek /i tuğkan kusura bakma.__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🇹🇷 Gruba Ekle", url="https://t.me/NetdVoicebot?startgroup=true"
                    ),
                    InlineKeyboardButton(
                        "Kanal 📣", url="https://t.me/NetdBots"
                    )
                ]
            ]
        )
    )
