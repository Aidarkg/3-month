# keyboards/inline_buttons.py
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire 🔥",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup


async def start_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Python 🐍",
        callback_data="python_answer"
    )
    javascript_button = InlineKeyboardButton(
        "JavaScript 💻",
        callback_data="javascript_answer"
    )
    cpp_button = InlineKeyboardButton(
        "C++ 💡",
        callback_data="cpp_answer"
    )
    markup.add(python_button)
    markup.add(javascript_button)
    markup.add(cpp_button)
    return markup
