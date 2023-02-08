import config
import markup as nav
import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.utils import executor
from loguru import logger
from googlesheet_table import GoogleTable

logger.add(
    config.settings["LOG_FILE"],
    format="{time} {level} {message}",
    level="DEBUG",
    rotation="1 week",
    compression="zip",
)


class FreakTelegramBot(Bot):
    def __init__(
            self,
            token,
            parse_mode,
            google_table=None,
    ):
        super().__init__(token, parse_mode=parse_mode)
        self._google_table: GoogleTable = google_table


bot = FreakTelegramBot(
    token=config.settings["TOKEN"],
    parse_mode=types.ParseMode.HTML,
    google_table=GoogleTable("schoolbot-376418-a782ef8b9eb0.json",
                             "https://docs.google.com/spreadsheets/d/164w-RInL1sDz_WqKQ5LwwMl2_JH_wK8idbld7LDIM1o/edit#gid=0"),
)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привіт, вибери день тижня, на який ти хотів би подивитися розклад!", reply_markup=nav.mainMenu)

@dp.message_handler(filters.Regexp(regexp=r"((П|п)онеділок)"))
async def abonement_handler(message_from: types.Message) -> None:
    user_id: str = str(message_from.from_id)
    text_msg: str = message_from.md_text.strip(" @#")
    command = text_msg.lower()
    print(f"Вход: команда '{command}'")

    values: str = bot._google_table.search_abonement(command)

    if values == -1:
        message = f'Ви обрали неправильний день тижня!'
    else:
        firstlesson: str = values[0]
        secondlesson: str = values[1]
        thirdlesson: str = values[2]
        forlesson: str = values[3]
        fivelesson: str = values[4]
        sixlesson: str = values[5]
        message: str = f'1. {firstlesson}\n 2. {secondlesson}\n 3. {thirdlesson}' \
                       f'\n 4. {forlesson}\n 5. {fivelesson}\n 6. {sixlesson}'

    try:
        await message_from.reply(message)
    except Exception as send_error:
        logger.debug(f"{send_error.message}: Trouble id: {user_id}")
        return


@dp.message_handler(filters.Regexp(regexp=r"((В|в)івторок)"))
async def abonement_handler(message_from: types.Message) -> None:
    user_id: str = str(message_from.from_id)
    text_msg: str = message_from.md_text.strip(" @#")
    command = text_msg.lower()
    print(f"Вход: команда '{command}'")

    values: str = bot._google_table.search_abonement(command)

    if values == -1:
        message = f'Ви обрали неправильний день тижня!'
    else:
        firstlesson: str = values[0]
        secondlesson: str = values[1]
        thirdlesson: str = values[2]
        forlesson: str = values[3]
        fivelesson: str = values[4]
        sixlesson: str = values[5]
        message: str = f' 1. {firstlesson}\n 2. {secondlesson}\n 3. {thirdlesson}' \
                       f'\n 4. {forlesson}\n 5. {fivelesson}\n 6. {sixlesson}'

    try:
        await message_from.reply(message, reply_markup=nav.mainMenu)
    except Exception as send_error:
        logger.debug(f"{send_error.message}: Trouble id: {user_id}")
        return


@dp.message_handler(filters.Regexp(regexp=r"((С|с)ереда)"))
async def abonement_handler(message_from: types.Message) -> None:
    user_id: str = str(message_from.from_id)
    text_msg: str = message_from.md_text.strip(" @#")
    command = text_msg.lower()
    print(f"Вход: команда '{command}'")

    values: str = bot._google_table.search_abonement(command)

    if values == -1:
        message = f'Ви обрали неправильний день тижня!'
    else:
        firstlesson: str = values[0]
        secondlesson: str = values[1]
        thirdlesson: str = values[2]
        forlesson: str = values[3]
        fivelesson: str = values[4]
        sixlesson: str = values[5]
        message: str = f' 1. {firstlesson}\n 2. {secondlesson}\n 3. {thirdlesson}' \
                       f'\n 4. {forlesson}\n 5. {fivelesson}\n 6. {sixlesson}'

    try:
        await message_from.reply(message)
    except Exception as send_error:
        logger.debug(f"{send_error.message}: Trouble id: {user_id}")
        return


@dp.message_handler(filters.Regexp(regexp=r"((Ч|ч)етвер)"))
async def abonement_handler(message_from: types.Message) -> None:
    user_id: str = str(message_from.from_id)
    text_msg: str = message_from.md_text.strip(" @#")
    command = text_msg.lower()
    print(f"Вход: команда '{command}'")

    values: str = bot._google_table.search_abonement(command)

    if values == -1:
        message = f'Ви обрали неправильний день тижня!'
    else:
        firstlesson: str = values[0]
        secondlesson: str = values[1]
        thirdlesson: str = values[2]
        forlesson: str = values[3]
        fivelesson: str = values[4]
        sixlesson: str = values[5]
        message: str = f' 1. {firstlesson}\n 2. {secondlesson}\n 3. {thirdlesson}' \
                       f'\n 4. {forlesson}\n 5. {fivelesson}\n 6. {sixlesson}'

    try:
        await message_from.reply(message)
    except Exception as send_error:
        logger.debug(f"{send_error.message}: Trouble id: {user_id}")
        return


@dp.message_handler(filters.Regexp(regexp=r"((П|п)'ятниця)"))
async def abonement_handler(message_from: types.Message) -> None:
    user_id: str = str(message_from.from_id)
    text_msg: str = message_from.md_text.strip(" @#")
    command = text_msg.lower()
    print(f"Вход: команда '{command}'")

    values: str = bot._google_table.search_abonement(command)

    if values == -1:
        message = f'Ви обрали неправильний день тижня!'
    else:
        firstlesson: str = values[0]
        secondlesson: str = values[1]
        thirdlesson: str = values[2]
        forlesson: str = values[3]
        fivelesson: str = values[4]
        sixlesson: str = values[5]
        message: str = f' 1. {firstlesson}\n 2. {secondlesson}\n 3. {thirdlesson}' \
                       f'\n 4. {forlesson}\n 5. {fivelesson}\n 6. {sixlesson}'

    try:
        await message_from.reply(message)
    except Exception as send_error:
        logger.debug(f"{send_error.message}: Trouble id: {user_id}")
        return


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
