from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMonday = KeyboardButton('Понеділок')
btnTuesday = KeyboardButton('Вівторок')
btnWednesday = KeyboardButton('Середа')
btnThursday = KeyboardButton('Четвер')
btnFriday = KeyboardButton('Пятниця')
mainMenu = ReplyKeyboardMarkup()
mainMenu.add(btnMonday,btnTuesday, btnWednesday, btnThursday, btnFriday)