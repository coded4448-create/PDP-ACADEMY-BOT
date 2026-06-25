# 1. Kutubxonalarni chaqirish
from aiogram import Bot, Dispatcher, types,F
from aiogram.filters import Command
from keboard import *
import asyncio
from config import BOT_TOKEN

from lesson19.keybard import menu, about


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
# 3. Botni uzluksiz ishga tushirish

image_logo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQz0fj6e2bltOwszWk-IbO4hLqPd8okt2zVrQ&s"
company_image = "https://avatars.mds.yandex.net/get-altay/11873493/2a0000018d7cd4ff0b0f0ded0574df9b24bd/L_height"

mentor_images = {"Bunyod Naimov": "https://framerusercontent.com/images/kXVV58GAu8fRErxTCCErYzk0i4.webp",
                 "Shohruh Abdurahmon": "https://framerusercontent.com/images/YqHAVasnW1eTKymnTB5dqiUMA.webp",
                 "Muhammadaziz To'lqinboyev": "https://framerusercontent.com/images/QzA0DHsPdTOxQ62dFyWslK4mT1Y.webp",
                 "Daler Badiyev": "https://framerusercontent.com/images/KNPILEJeDuGPQhkVMZY35hsyltg.webp",
                 "Asilbek Mamadaliyev": "https://framerusercontent.com/images/YxvMJWtMDSRGPD2IabC9CQdlBiU.webp",
                 "Habibulloh Nuriddin": "https://framerusercontent.com/images/rTCJHxT1yCe2LsYwsfZFrrBDds.webp",
                 "Asliddin Abdullayev": "https://framerusercontent.com/images/s6j0WzUvfog8RJHmnTeOurwR4.webp"}

python_image = "https://framerusercontent.com/images/842SsoUmQMhdORw9rDC5e1EyO1U.png?scale-down-to=512"
robototexnika_image = "https://framerusercontent.com/images/kx3nFOZSgvqHlhAejBBHdTNyI.png"
scratch_image = "https://framerusercontent.com/images/GbPBaWtopR178MP8DQSZzc8h8.png?scale-down-to=1024"
frontend_image = "https://framerusercontent.com/images/kkNJyRECmT2kslWfE5JM8lluQg.png?scale-down-to=512"

address_image = "https://media.istockphoto.com/id/1409911141/vector/red-map-pin-vector-icon-clipart-location-symbol.jpg?s=612x612&w=0&k=20&c=zIyeXjdLDZzqO9y69ZfdpQRjscaRGCCMgSaBcJxeVk0="





@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer_photo(photo=image_logo,
                               caption="salom bizning pdp academi botimizga hush kelib siz sizga qanday yordam bera olamn",
                               reply_markup=main_menu3())


@dp.message(F.text=="🏢 Kompaniya haqida")
async def sent(message: types.Message):
    await message.answer_photo(photo=company_image,
                               caption="lkgoiyflflflflj  kljgkglkhkllh",
                               reply_markup=main_menu3())

@dp.message(F.text=="🎓 Kurslarimiz")
async def back(message: types.Message):
    await message.answer(text="biz haqimizda",
                               reply_markup=course_menu())

@dp.message(F.text=="📞 Kontaktlar/ Manzil")
async def back(message: types.Message):
    await message.answer_photo(text="biz haqimizda", caption="yunsobod 15 kvartel minor metroo",photo=address_image,
                               reply_markup=main_menu3())
@dp.message(F.text == "🇺🇿/🇷🇺 Til")
async def back(message: types.Message):
    await message.answer(text="language selected",
                         reply_markup=list_menu())
@dp.message(F.text=="Python")
async def back(message: types.Message):
    await message.answer_photo( photo=python_image, caption="biz haqimizda",
                               reply_markup=defend())
@dp.message(F.text=="Fronted")
async def back(message: types.Message):
    await message.answer_photo( photo=python_image, caption="biz haqimizda",
                               reply_markup=defend())


@dp.message(F.text == "Robototexnika")
async def back(message: types.Message):
    await message.answer_photo(photo=python_image, caption="biz haqimizda",
                               reply_markup=defend())
@dp.message(F.text=="Scratch")
async def back(message: types.Message):
    await message.answer_photo( photo=python_image, caption="biz haqimizda",
                               reply_markup=defend())

@dp.message(F.text=="ortga")
async def back(message: types.Message):
    await message.answer(text="ortga olindi",
                               reply_markup=course_menu())
@dp.message(F.text=="🔙 back.")
async def back(message: types.Message):
    await message.answer(text="ortga olindi",
                               reply_markup=main_menu3())

@dp.message(F.text=="kurs"
                    "....")
async def back(message: types.Message):
    await message.answer( text="sizni talabingizga  qarab kurslarni jozishimiz mumkin",
                               reply_markup=defend())
@dp.message(F.text=="modullar soni")
async def back(message: types.Message):
    await message.answer( text="asosiy modullar soni bizda 9 ta ",
                               reply_markup=defend())
@dp.message(F.text=="video darslar ...")
async def back(message: types.Message):
    await message.answer( text="video darslar kursga tolov qilganingizda tashlab beriladi",
                               reply_markup=defend())
@dp.message(F.text=="kursga yozilish...")
async def back(message: types.Message):
    await message.answer( text="browserlardan pdpd academiy registrate deb yozing yoki +998949967088 ishonchli "
                               "raqamlaringa telefon qilingh",
                               reply_markup=defend())



async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())