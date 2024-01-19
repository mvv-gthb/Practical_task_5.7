import click
#функция шифрования символа на основе использования таблицы Unicode
def shift(key, symbol):
    alphabets = {"upper_russian" : range(ord("А"), ord("Я") + 1), #формируются используемые алфавиты, в русском отсутствует буква "ё",
                 "lower_russian" : range(ord("а"), ord("я") + 1), #ее можно попробовать добавить, но тогда наверное все будет не так красиво :(
                 "upper_english" : range(ord("A"), ord("Z") + 1),
                 "lower_english" : range(ord("a"), ord("z") + 1)}
    dec_symbol = ord(symbol) #входной символ преобразуется в Unicode в десятичном формате
    for alphabet in alphabets.values(): #поиск алфавита, в который входит символ
        if dec_symbol in alphabet:
            direction = 1 if dec_symbol + key % len(alphabet) <= max(alphabet) else -1  #определяем направление смещения и количество символов. Изначально здесь было немного
            crypted_dec_symbol = dec_symbol + key % (direction * len(alphabet))         #по-другому. Для меня стало полной неожиданностью когда расшифрование сработало без
            crypted_symbol = chr(crypted_dec_symbol)                                    #допиливания, все дело оказалось в делении по модулю отрицательных чисел, я, честно
            break                                                                       #признаться, думал, что его результат не зависит от знака
        else:
            crypted_symbol = symbol
    return crypted_symbol
