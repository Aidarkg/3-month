from aiogram import types, Dispatcher
from config import bot, MEDIA
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from keyboards.inline_buttons import start_menu_keyboard, referral_program_keyboard
from const import PROFILE_TEXT
from database.sql_commands import Database


async def callback_referral_program(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text='Welcome to the Referral Program! Choose an option below:',
        reply_markup=await referral_program_keyboard()
    )


async def callback_referral_link(call: types.CallbackQuery):
    db = Database()
    referral_link = db.get_referral_link(user_id=call.from_user.id)
    if referral_link:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=f"Your referral link: {referral_link}"
        )
    else:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text="You don't have a referral link yet."
        )


async def callback_referral_list(call: types.CallbackQuery):
    db = Database()
    referral_list = db.get_referral_list(user_id=call.from_user.id)
    if referral_list:
        message = "Your referral list:\n"
        for user in referral_list:
            message += f"- {user['username']} ({user['telegram_id']})\n"
    else:
        message = "You don't have any referrals yet."

    await bot.send_message(
        chat_id=call.message.chat.id,
        text=message
    )


def register_reference_users(dp: Dispatcher):

    dp.register_callback_query_handler(
        callback_referral_program,
        lambda call: call.data == "referral_program"
    )

    dp.register_callback_query_handler(
        callback_referral_link,
        lambda call: call.data == "referral_link"
    )

    dp.register_callback_query_handler(
        callback_referral_list,
        lambda call: call.data == "referral_list"
    )
