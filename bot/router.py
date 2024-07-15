from aiogram import Router, types
from create_bot import ROOT_ADMIN
from states import ChangePrice
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(Command("start"))
async def start(message: types.Message):
    if message.from_user.id == ROOT_ADMIN:
        builder = ReplyKeyboardBuilder()
        builder.button(text="/change_price")
        await message.answer("Hi!", reply_markup=builder.as_markup())


@router.message(Command("change_price"))
async def change_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ROOT_ADMIN:
        await message.answer("Provide new price: ")
        await state.set_state(ChangePrice.PRICE)


@router.message(ChangePrice.PRICE)
async def get_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ROOT_ADMIN:
        price = message.text
        if price.isdigit():
            with open("price.json", "w") as file:
                file.write(price)
            await message.answer("Price successfully changed!")
            await state.clear()
        else:
            await message.answer("It's not number!Please provide again:")
