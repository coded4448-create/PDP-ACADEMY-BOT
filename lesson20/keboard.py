from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    button = KeyboardButton(text="🏢 Kompaniya haqida")
    button2 = KeyboardButton(text="🧑‍🏫 Bizning Mentorlar")
    button3 = KeyboardButton(text="🎓 Kurslarimiz")
    button4 = KeyboardButton(text="📞 Kontaktlar/ Manzil")
    button5 = KeyboardButton(text="🇺🇿/🇷🇺 Til")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3],
            [button4, button5]
        ],
        resize_keyboard=True
    )
    return rkm

#
def course_menu():
    button = KeyboardButton(text="Python")
    button2 = KeyboardButton(text="Fronted")
    button3 = KeyboardButton(text="Robototexnika")
    button4 = KeyboardButton(text="Scratch")
    button5 = KeyboardButton(text="🔙 back.")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
            [button5],
        ],
        resize_keyboard=True
    )
    return rkm
#
def list_menu():
    button = KeyboardButton(text="uzbek")
    button2 = KeyboardButton(text="english")
    button3 = KeyboardButton(text="ortga")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3],

        ],
        resize_keyboard=True
    )
    return rkm
#
def main_menu2():
    button = KeyboardButton(text="about us")
    button2 = KeyboardButton(text="🧑‍🏫 our tutor")
    button3 = KeyboardButton(text="🎓 our course")
    button4 = KeyboardButton(text="📞 contact/location")
    button5 = KeyboardButton(text="🇺🇿/🇷🇺 language")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3],
            [button4, button5]
        ],
        resize_keyboard=True
    )
    return rkm
#     wg44444444444444444444444444444444444444444444444444444444444444444444444444


def main_menu3():
    button = KeyboardButton(text="🏢 Kompaniya haqida")
    button3 = KeyboardButton(text="🎓 Kurslarimiz")
    button4 = KeyboardButton(text="📞 Kontaktlar/ Manzil")
    button5 = KeyboardButton(text="🇺🇿/🇷🇺 Til")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button3],
            [button4],
            [  button5]
        ],
        resize_keyboard=True
    )
    return rkm

def defend():
    button = KeyboardButton(text="kurs davomi....")
    button2 = KeyboardButton(text="modullar soni")
    button3 = KeyboardButton(text="video darslar ...")
    button4 = KeyboardButton(text=""
                                  "")
    button5 = KeyboardButton(text="ortga")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2,button3],
            [button4],
            [button5]

        ],
        resize_keyboard=True
    )
    return rkm