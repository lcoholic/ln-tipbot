import logging
import re
import time
import qrcode
from pyln.client import LightningRpc
from aiogram import Bot, Dispatcher, executor, types

from config import BOT_TOKEN, RPC_PATH, HELP_MSG

logging.basicConfig(filename='bot.log', encoding='utf-8', level=logging.INFO,
                    format='%(asctime)s : %(module)s : %(message)s')
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
l = LightningRpc(RPC_PATH)

@dp.message_handler(commands=['start', 'help', 'h'])
async def welcome(message: types.Message):
    await message.answer(HELP_MSG)


@dp.message_handler()
async def answer_invoice_qrcode(message: types.Message):
    amountSatMatch = re.search(r'\d+', message.text)
    if amountSatMatch is None:
        await message.answer('You have to enter a number')
    else:
        amountmSat = int(amountSatMatch.group()) * 1000
        now = time.time()
        invoice = l.invoice(amount_msat=amountmSat, label='lbl{}'.format(now), 
                         description=f'from {message.from_user.username} via my tip bot')
        bolt11 = invoice['bolt11']
        qrcode.make(bolt11).save('qrcode.png')
        await message.answer_photo(photo=open('qrcode.png', 'rb'), caption=bolt11)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
