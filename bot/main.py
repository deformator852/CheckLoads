from create_bot import dp, bot
import router
import asyncio
import logging
import sys


async def main():
    dp.include_router(router.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
