from aiogram import types, Dispatcher
from config import bot, GROUP_ID
from database.sql_commands import Database


async def ban_users_db(message: types.Message):
    db = Database()
    user = db.sql_select_ban_user(message.from_user.id)

    if user:
        text = (f"Hello {message.from_user.first_name}!\n"
                f"You are in the database. Total violations: {user['count']}")
    else:
        text = f"Hello {message.from_user.first_name}!\nYou are not in the database. Don't worry."

    await bot.send_message(
        chat_id=GROUP_ID,
        text=text,
    )


def register_ban_users_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(ban_users_db,
                                       lambda call: call.data == "ban_users")
