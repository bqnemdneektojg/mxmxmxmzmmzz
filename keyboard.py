from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton as ib
kbadmin = ReplyKeyboardMarkup(resize_keyboard=True)
kbadmin.row("💣 Статистика","🐦‍⬛ Рассылка")

kbsend = ReplyKeyboardMarkup(resize_keyboard=True)
kbsend.row("С фото","Без фото"," 🐍Назад")

kbsub = InlineKeyboardMarkup()
kbsub.row(ib('🕷️ Подписаться', url='https://t.me/+JI-8OuLfufU5ZGU1'))
kbsub.row(ib('🕷️' Подписаться, url='https://t.me/+o9usEqFR1eNmMWZi'))
kbsub.row(ib('🐦‍⬛ Подписался', callback_data='subbed'))

kbmenu = InlineKeyboardMarkup()
kbmenu.add(ib('🕷️ IP-адрес', callback_data='checkip'))
kbmenu.add(ib('🐦‍⬛ BTC-адрес', callback_data='checkbtc'))
kbmenu.add(ib('🪰 MAC-адрес', callback_data='checkmac'))
kbmenu.add(ib('🥷 Никнейм', callback_data='checknick'))
kbmenu.add(ib('💣 Номер', callback_data='checknum'))
kbmenu.add(ib('🕸️ BIN карты', callback_data='checkbin'))
kbmenu.add(ib('🪨 VK', callback_data='checkvk'))

kbback = InlineKeyboardMarkup().row(ib('Назад', callback_data='back'))