from aiogram.fsm.state import State,StatesGroup

class ChangePrice(StatesGroup):
    PRICE = State()
