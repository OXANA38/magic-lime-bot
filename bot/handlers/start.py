# bot/handlers/start.py
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

from bot.data.messages import START_MESSAGE, MAIN_MENU

router = Router()

# Главное меню
def get_main_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=MAIN_MENU["screenshots"])],
            [KeyboardButton(text=MAIN_MENU["algorithm"])],
            [KeyboardButton(text=MAIN_MENU["calculate"])],
            [KeyboardButton(text=MAIN_MENU["faq"])],
            [KeyboardButton(text=MAIN_MENU["demo"])],
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard

# Команда /start
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        START_MESSAGE,
        reply_markup=get_main_keyboard()
    )

# Обработка кнопок главного меню
@router.message(F.text == MAIN_MENU["screenshots"])
async def show_screenshots(message: Message):
    from bot.data.messages import SCREENSHOTS_MESSAGE
    await message.answer(SCREENSHOTS_MESSAGE)

@router.message(F.text == MAIN_MENU["algorithm"])
async def show_algorithm(message: Message):
    await message.answer("🤖 *Раздел «Алгоритм» в разработке*\n\nСкоро здесь будет подробное объяснение работы алгоритма клонирования.")

@router.message(F.text == MAIN_MENU["calculate"])
async def show_calculate(message: Message):
    await message.answer("🧮 *Раздел «Расчет дохода» в разработке*\n\nСкоро здесь будет калькулятор твоего потенциального дохода.")

@router.message(F.text == MAIN_MENU["faq"])
async def show_faq(message: Message):
    await message.answer("❓ *Раздел «Вопросы о рисках» в разработке*\n\nСкоро здесь будут ответы на все острые вопросы.")

@router.message(F.text == MAIN_MENU["demo"])
async def show_demo(message: Message):
    await message.answer("🚀 *Раздел «Демо-доступ» в разработке*\n\nСкоро здесь можно будет получить тестовый доступ к личному кабинету.")
