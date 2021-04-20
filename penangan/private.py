from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEJX5NgelpPxIp7TxBi31AWY0e6awyNoAACrwIAAiZaqFetusa6iC_gHx8E")
    await message.reply_text(
        f"""**❖ Hy kamu, saya adalah __[Mighty Music Assistant Bot](https://t.me/MightyMusic_bot)__ 🎶**

❖ Saya bisa memutar musik di VCG GROUP atau panggilan suara grup Anda. Dikembangkan Oleh** __[Yunus](https://t.me/ZendYNS)__

❖ Tambahkan** __[Mighty Music Assistant](https://t.me/MightyMusic_Assistant)__ **dan** __[Mighty Music Bot](https://t.me/MightyMusic_bot)__ **ke grup Anda, dan rasakan sensasi mendengar musik di VCG Group anda!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Info Penting 📚", url="https://telegra.ph/Mighty-Music-Assistant-04-20")
                  ],[
                    InlineKeyboardButton(
                        "🧸 Tele Story", url="Https://t.me/telee_story"
                    ),
                    InlineKeyboardButton(
                        "Quotes Official 🧸", url="https://t.me/Quotes_Channel_Official"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "💠 Pemilik 💠", url="Https//t.me/ZendYNS"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💠 Pemilik 💠", url="https://t.me/ZendYNS")
                ]
            ]
        )
   )


