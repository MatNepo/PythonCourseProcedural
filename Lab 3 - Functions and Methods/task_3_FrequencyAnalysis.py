def count_letters(text):
    """The function counts how many times each letter appears in the text, output in the
    form of a dictionary {letter -> amount}"""
    text_low = text.lower()  # make all letters low
    final_text = {}  # create empty dict
    # fill the dict with amount of each letter
    for current in text_low:
        if current.isalpha():  # check current character on letter
            counter = text_low.count(current)  # amount of current letter
            final_text[current] = float(counter)  # add to the dict
    return final_text


def calculate_frequency(text_):
    """The function counts frequency of each letter"""
    frequency = count_letters(text_)  # call function count_letters
    letters_amount = sum(frequency.values())  # total amount of letters
    # Take current letter in the dict and find its frequency
    frequency = [(key, frequency[key] / letters_amount) for key, value in frequency.items()]
    return frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

result = calculate_frequency(main_str)  # call function calculate_frequency
for index, amount in result:
    print(f"{index}:{amount: .2f}")  # round up the output to 2 characters after point
