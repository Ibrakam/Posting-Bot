from aiogram import Bot, Dispatcher
import asyncio
from dotenv import dotenv_values
from bot.handlers.bot_commands import route

env_vars = dotenv_values(".env")

api_token = env_vars.get("API_TOKEN")


async def main() -> None:
    token = api_token

    dp = Dispatcher()
    bot = Bot(token=token)
    dp.include_router(route)

    # await bot.delete_webhook()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
