# TODO  Напишите функцию count_letters
def count_letters(text):
    global keys, dict, letters
    seen = set()
    dict = {}
    keyss = []
    f = text.lower()
    letters = list(f)

    index = 0
    while index <= (len(letters) - 1):
        if not (letters[index].isalpha()):
            letters.pop(index)
        else:
            index += 1

    for let in letters:
        if let not in seen:
            seen.add(let)
            keyss.append(let)

    keys = keyss

    for i in range(0, len(keys)):
        dict[keys[i]] = None



def calculate_frequency(slovar, bykvi):
    global value, letter
    dict_ = {}
    for key, value in enumerate(dict):
        letter = bykvi.count(value)
        dict_[value] = round(letter / len(bykvi), 2)
        x = "%.2f" % dict_[value]
        print(f'{value}: {x}')













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
Свои мне сказки говорил."""

count_letters(main_str)
calculate_frequency(dict, letters)