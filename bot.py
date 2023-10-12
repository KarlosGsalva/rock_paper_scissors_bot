import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers

# инициализация логгера
logger = logging.getLogger(__name__)


# функция конфигурирования и запуска бота
async def main():
    # конфигурируем логгер
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levellname)-8s'
               '[%(asctime)s] - %(name)s - %(message)s')

    # вывод в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # загружаем конфиг в переменную config
    config = load_config()

    # инициализация бота и диспетчера
    bot = Bot(config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()

    # регистрация роутеров в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())



