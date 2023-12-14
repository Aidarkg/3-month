from aiogram import executor
from config import dp
from handlers import (
    start,
    questionnaire,
    chat_actions,
    ban_users
)
from database import sql_commands


async def on_startup(_):
    db = sql_commands.Database()
    db.sql_create_tables()


start.register_start_handlers(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)
chat_actions.register_chat_actions_handlers(dp=dp)
ban_users.register_ban_users_handlers(dp=dp)

if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )
