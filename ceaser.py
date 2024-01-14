#!/usr/bin/env python
# coding: utf-8

# ### Задача 1

# In[18]:


#реализация формулы Бине для расчета n-го числа Фибоначчи
def bine_formula(n):
    golden_ratio = (1 + 5 ** 0.5) / 2
    result = round((golden_ratio ** n - (-golden_ratio ** (-n))) / (2 * golden_ratio - 1))
    return result
#функция-генератор чисел Фибоначчи, при отрицательном значении генератор стартует с конечного значения и заканчивается на 1 
def fib_numbers_gen(amount = 100):
    if amount < 0:
        for n in range(amount, 0):
            yield bine_formula(n)
    if amount == 0:
            yield 0
    if amount > 0:
        for n in range(1, amount + 1):
            yield bine_formula(n)
#проверка корректности вводимых данных
try: 
    amount = input("Введите необходимое количество чисел Фибоначчи: ")
    fib_numbers = fib_numbers_gen(int(amount)) if amount else fib_numbers_gen()
except:
    print("Введенные данные не являются целым числом")
#вывод результата
for count, item in enumerate(fib_numbers):
    print(f"{count + 1} : {item}")


# ### Задача 2

# In[2]:


import math
import click
#функция-генератор разложения синусоидальной функции
def sin(x, row_length):
    for count in range(row_length):
        yield (-1) ** count * x ** (2 * count + 1) / math.factorial(2 * count + 1)
#функция-генератор разложения косинусоидальной функции
def cos(x, row_length):
    for count in range(row_length):
        yield (-1) ** count * x ** (2 * count) / math.factorial(2 * count)
#функция-генератор показательной функции
def exp(x, row_length):
    for count in range(row_length):
        yield x ** count / math.factorial(count)
#формирование списка созданных функций
functions = [sin, cos, exp]
#назначение атрибута name для функций
for function, name in zip(functions, ['sin', 'cos', 'exp']):
    setattr(function, 'name', name)
#функция сравнения значений, при помощи генератора формируется список, значения суммируются, вычисляется разность
def comparation(x, row_length, function):
    return getattr(math, function.name)(x) - sum(list(function(x, row_length)))
#ввод исходных данных и вывод результатов сравнения
x = click.prompt(f"Введите значение аргумента функции", type = float)
row_length = click.prompt(f"Введите количество элементов ряда", type = int)
print(f"Результат:")
for function in functions:
    print(f"math.{function.name}(x) - {function.name}(x) = {comparation(x, row_length, function):.2e}")


# ### Задача 3

# In[3]:


import math
import click
#функция конвертирования координат
def convert(x, y):
    r = math.sqrt(x**2 + y**2)
    fi = math.atan2(y, x)
    return r, fi
#ввод исходных данных и вывод результатов
x = click.prompt(f"Введите значение координаты х", type = float)
y = click.prompt(f"Введите значение координаты y", type = float)
polar = convert(x, y)
print(f"Результат в полярной системе координат: {chr(961)} = {polar[0]:.3f} , {chr(996)} = {polar[1]:.3f} ")


# ### Задача 4

# In[4]:


import string
molecules = ['H2-S-O4', 'H2-O', 'NA-CL', 'H-CL', 'K-CL']
element_molar_masses = {'H' : 1.008, 
                        'O' : 15.999,
                        'S' : 32.066,
                        'NA': 22.99,
                        'CL': 35.453,
                        'K' : 39.098}
#функция расчета молярной массы
def mass_calculate(molecule):
    elements = molecule.split('-')
    molecule_molar_mass = 0
    for element in elements:
        if element.isalpha(): #если в названии элемента нет цифр, то ищем в словаре значение массы и суммируем
            molecule_molar_mass += element_molar_masses[element]
        else: 
            letters = ''.join([item for item in element if item.isalpha()])       #если в названии цифры есть, то разделяем название 
            digits = ''.join([item for item in element if item.isdigit()])        #элемента и количество атомов в молекуле, массу одного атома 
            molecule_molar_mass += element_molar_masses[letters] * int(digits)    #берем из словаря, перемножаем и суммируем
    return molecule_molar_mass
#вывод результатов
results = {}
for molecule in molecules:
    results[mass_calculate(molecule)] = molecule #формируем словарь с результатами
print("Результат вычисления:") 
for result in sorted(results):  #запускаем цикл по отсортированным ключам, выводим ключ и значение
    print(f"{results[result]} {result:.3f}")


# ### Задача 5

# In[5]:


import click
import operator
import logging

logger = logging.getLogger('calc')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('calc_errors.log')
file_handler.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

path = "input_calc.txt"

def checking_string(count_string, raw_string):  #функция проверки корректности ввода строк с выражениями
    try:
        operators = '+-/*'  #используемые операторы
        input_list = list(raw_string) #преобразование входной строки в список
        output_list = []  #список для хранения выходного выражения
        symbol = ''
        for count, item in enumerate(input_list):
            if item.isdigit():   #если на входе число, то записываем в строку
                symbol += item
            elif item == '.':   #если точка
                if count == 0 or count == len(input_list) - 1: #проверка, чтобы точка не стояла в начале или конце выражения
                    logger.error(f"Строка {count_string + 1}: {raw_string} - В начале или конце строки использован символ \".\"")
                    raw_string = click.prompt("Попробуйте ввести выражение заново")
                    return checking_string(count_string, raw_string)
                elif not(input_list[count - 1].isdigit() and  input_list[count + 1].isdigit()): #слева и справа от точки должны быть числа
                    logger.error(f"Строка {count_string + 1}: {raw_string} - Некорректное положение символа \".\"")
                    raw_string = click.prompt("Попробуйте ввести выражение заново")
                    return checking_string(count_string, raw_string)
                else:
                    symbol += item
            elif item in operators: #если на входе оператор
                if  count == 0 or count == len(input_list) - 1: #не может быть первым и последним в выражении
                    logger.error(f"Строка {count_string + 1}: {raw_string} - В начале или конце строки использован оператор")
                    raw_string = click.prompt("Попробуйте ввести выражение заново")
                    return checking_string(count_string, raw_string)
                elif not(input_list[count - 1].isdigit() and  input_list[count + 1].isdigit()): #справа и слева долждны быть числа
                    logger.error(f"Строка {count_string + 1}: {raw_string} - Некорректное положение оператора")
                    raw_string = click.prompt("Попробуйте ввести выражение заново")
                    return checking_string(count_string, raw_string)
                else: #если все в порядке
                    output_list.append(float(symbol)) #в выходной список добавляется сформированный ранее элемент (число)
                    output_list.append(item) #оператор добавляется как отдельный элемент
                    symbol = '' #переменная symbol обнуляется для формирования следующего числа
            else: #если в строке не числа, точка или оператор
                logger.error(f"Строка {count_string + 1}: {raw_string} - Использован запрещенный символ")
                raw_string = click.prompt("Попробуйте ввести выражение заново")
                return checking_string(count_string, raw_string)
        output_list.append(float(symbol))
        return output_list
    except ValueError:  #исключение возникает если во входной строке записана десятичная дробь с двумя точками, например "12.3.4"
        logger.error(f"Строка {count_string + 1}: {raw_string} - Ошибка преобразования числа в формат float")
        raw_string = click.prompt("Попробуйте ввести выражение заново")
        return checking_string(count_string, raw_string)

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0

def infix_to_postfix(checked_string): #преобразование инфиксной нотации в постфиксную
    stack = []  #стек
    postfix_string = []  #выходное выражение
    for count, symbol in enumerate(checked_string):
        if type(symbol) is float:  #если на входе символ, то он помещается в стек
            postfix_string.append(symbol)
        else:     #если оператор
            while stack and precedence(symbol) <= precedence(stack[-1]):
                postfix_string.append(stack.pop())
            stack.append(symbol)
    while stack:
        postfix_string.append(stack.pop())
    return postfix_string

def RPN(postfix_string):  #вычисление выражений в постфиксной нотации
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = []
    for symbol in postfix_string:
        if type(symbol) is float: #числа помещаются в стек
            stack.append(symbol)
        else:   #если на входе оператор
            term_2, term_1 = stack.pop(), stack.pop() #то из стека достаются последние числа
            stack.append(operators[symbol](term_1, term_2)) #и над ними производится операция, результат помещется обратно в стек
    return stack.pop()
    
def calc(path):   #считывание данных из файла и запуск расчетов
    with open (path, "r", encoding = "utf-8") as raw_text:
        raw_strings = raw_text.readlines()
        for count, raw_string in enumerate(raw_strings):
            raw_string = raw_string.replace(" ", "").replace("\n", "")  #переместилось из checking_string сюда, чтобы сразу отсекать пустые строки
            if len(raw_string) == 0:
                logger.error(f"Строка {count + 1}: Пустая строка, вычисления не будут выполнены")
                continue
            checked_string = checking_string(count, raw_string) #проверка выражения
            postfix_string = infix_to_postfix(checked_string)   #преобразование в постфиксную нотацию
            result = RPN(postfix_string)                        #вычисление
            print(f"Строка {count + 1}: {result}")

calc(path) #инициализация вычислений

logger.removeHandler(file_handler)      #если handler не удалить, то при повторном запуске скрипта записи в логах
logger.removeHandler(console_handler)   #повторяются столько раз, сколько запускалась программа


# ### Задача 6

# In[2]:


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

key = click.prompt(f"Введите смещение", type = int)
message = click.prompt(f"Введите сообщение")

crypted_message = ''.join([shift(key, symbol) for symbol in message]) #формируем массив из зашифрованных символов и объединяем его в строку
print(f"Шифрованное сообщение: {crypted_message}")
decrypted_message = ''.join([shift(-key, symbol) for symbol in crypted_message]) #здесь для меня стало полной неожиданностью, что все заработало в "обратную" сторону
print(f"Расшифрованное сообщение: {decrypted_message}")                          #без допиливания, как-то раньше не сталкивался с делением по модулю отрицательных чисел


# ### Задача 7

# In[7]:


from datetime import datetime
from datetime import timedelta
import pandas as pd
import logging

logger = logging.getLogger('visits')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('visits.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def timing(in_out_pairs):    #функция расчета продолжительности интервалов посещения
    time_format = "%d/%m/%Y %H:%M:%S"
    time_delta = timedelta(days=0, hours=0, minutes=0, seconds=0)
    for in_out_pair in in_out_pairs:
        if all(in_out_pair):
            time_delta += datetime.strptime(in_out_pair[1], time_format) - datetime.strptime(in_out_pair[0], time_format)
    result = f"Общее время посещения: {time_delta}" if time_delta != timedelta(days=0, hours=0, minutes=0, seconds=0) else "Данные некорректны"
    print(result)

def intervals(athlete_location):  #функция формирования интервалов посещения 
    if athlete_location.empty:
        print(f"Данные отсутствуют")
    else:    
        in_out_pairs = []  #массив для записи интервалов посещения
        time_in, time_out = False, False #время входа, время выхода
        for index, row in athlete_location.iterrows(): #перебираем все записи по локации
            # print(f"{row['Type']}")
            if row['Type'] == "In" and time_in == False and time_out == False: #массив интервалов пуст, найдено время входа
                time_in = row['Date'] #переменной time_in присваивается значение из текущей строки
            elif row['Type'] == "Out" and time_in == False and time_out == False: #массив интервалов пуст, найдено время выхода
                time_out = row['Date'] #присваиваем переменной time_out значение
                in_out_pairs.append([time_in, time_out]) #в массив записывается некорректная пара, в которой отсутвует время входа
                time_in, time_out = False, False #значения обнуляются для поиска новой пары
                logger.info(f"{athlete}, {location}: Найдено время выхода, время входа отсутствует")
            elif row['Type'] == "In" and time_in and time_out == False: #время входа зафиксировано на одном из предыдущих шагов, повторно найдено время входа
                in_out_pairs.append([time_in, time_out])  #в массив записывается некорректная пара, в которой отсутвует время выхода
                time_in = row['Date'] #переменной time_in присваиваем новое значение, переменная time_out сохраняет значение False
                logger.info(f"{athlete}, {location}: Найдено два времени входа подряд")
            elif row['Type'] == "Out" and time_in and time_out == False: #время входа зафиксировано на одном из предыдущих шагов, найдено время выхода
                time_out = row['Date'] #присваиваем переменной time_out значение
                in_out_pairs.append([time_in, time_out]) #в массив записывается корректная пара
                time_in, time_out = False, False #значения обнуляются для поиска новой пары
        if time_in and not time_out: in_out_pairs.append([time_in, time_out]) #записываем в массив некорректную пару с "подвисшим" входом без выхода
        logger.info(f"{athlete}, {location}: Не найдено время выхода")
        timing(in_out_pairs) #функция расчета продолжительности интервалов посещения

path = 'activity.csv'
df = pd.read_csv(path)

location_dict = {'Center' : 'комплекса',       #словарь замены для вывода информации
                 'Pool-1' : 'бассейна № 1',
                 'Pool-2' : 'бассейна № 2'}

for athlete in df['Athlete ID'].unique():    #перебираем всех спортсменов 
    athlete_info = df[df['Athlete ID'] == athlete] #формируем датафрейм по спортсмену
    print(f"-------------------------------------")
    print(f"Информация о спортсмене с id = {athlete}")
    # print(athlete_info)
    for location in df['Location'].unique():  #перебираем локации для спортсмена
        print(f"Статистика по посещению {location_dict[location]}:")
        athlete_location = athlete_info[athlete_info['Location'] == location]  #формируем датафрейм по каждой локации для спортсмена
        intervals(athlete_location)   #запускаем функцию формирования интервалов посещения


# ### Задача 8

# In[15]:


import crc8
import click
import logging

logger = logging.getLogger('crc8_log')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('crc8.log')
file_handler.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def compute_crc8(symbol):  #функция расчета crc8
    hash_crc8 = crc8.crc8()
    hash_crc8.update(symbol.encode("utf-8"))
    binary_code = bin(int(hash_crc8.hexdigest(), 16))[2:]
    hash_crc8.reset()
    while len(binary_code) < 8:   #заолнение 0-ями до 8-ми символов в группе
        binary_code = '0' + binary_code
    return binary_code

def encode():
    message = input("Введите сообщение: ")
    print(f"Кодированное сообщение:", end = ' ')
    for symbol in message:
        print(compute_crc8(symbol), end = ' ')

def decode():
    crc8_message = input("Введите закодированное сообщение: ")
    message = input("Введите сообщение: ")
    crc8_list = crc8_message.split() #закодированное сообщение "разбирается" на список
    results = []
    for binary_code, symbol in zip(crc8_list, message):  
        if binary_code == compute_crc8(symbol): #сравнение переданного и рассчитанного кодовых последовательностей для символов
            results.append(False) #если совпадает присваивается значение False, немного нелогично, 
        else:                     #но так легче потом осуществить проверку корректности принятых символов
            results.append([message.index(symbol) + 1, symbol, binary_code]) #если не совпадает, то в массив записываются данные 
    if any(results):                                                         #для вывода в лог
        for result in results:
            if result is not False:
                logger.warning(f"Ошибка в символе {result[1]} с индексом {result[0]}\n"
                               f"CRC8 (полученное): {hex(int(result[2], 2))}\n"
                               f"CRC8 (расcчитанное): {hex(int(compute_crc8(result[1]), 2))}") 
    else:
        print("Все контрольные суммы верны")

def input_type():  #функция ввода строк и вывода типа преобразования
    device_type = click.prompt(f"Введите тип (1 — кодер, 2 — декодер): ", type = int)
    if device_type != 1 and device_type != 2:
        return input_type()
    elif device_type == 1:
        encode()
    elif device_type == 2:
        decode()
        
input_type()
logger.removeHandler(file_handler)      #если handler не удалить, то при повторном запуске скрипта записи в логах
logger.removeHandler(console_handler)   #повторяются столько раз, сколько запускалась программа


# ### Задача 9

# In[17]:


import click

def input_sequence():
    sequence = click.prompt(f"Введите последовательность из нулей и единиц")
    if set(sequence) == {'0', '1'} or set(sequence) == {'0'} or set(sequence) == {'1'}: #преобразование строки в set и проверка на наличие только 0 и 1
        return sequence                                                                 #наверное здесь логическое выражение более компактно можно написать,
    else:                                                                               #но я пока не придумал как
        return input_sequence()

def invert(symbol):  #вспомогательная функция инвертирующая 0 в 1 и наоборот
    if symbol == '0':
        return '1'
    elif symbol == '1':
        return '0'
    else:
        print("Запрещенный символ")

def rz_coder(sequence):   
    encoded_dictionary = {'0' : '00', '1' : '10'}
    encoded_sequence = ''.join([encoded_dictionary[symbol] for symbol in sequence])
    return encoded_sequence

def rz_decoder(sequence):
    decoded_dictionary = {'00' : '0', '10' : '1'}
    decoded_sequence = ''.join([decoded_dictionary[sequence[symbol_index:symbol_index + 2]] for symbol_index in range(0, len(sequence), 2)])
    return decoded_sequence

def nrz_coder(sequence):
    return sequence

def nrz_decoder(sequence):
    return sequence

def nrzi_1(input_sequence, decode = False): #вариант 1: 0 - изменение уровня, 1 - уровень прежний
    previous_symbol = '0'
    output_sequence = ''
    for symbol in input_sequence:
        encoded_symbol = invert(previous_symbol) if symbol == '0' else previous_symbol
        output_sequence += encoded_symbol
        previous_symbol = symbol if decode else encoded_symbol
    return output_sequence

def nrzi_2(input_sequence, decode = False): #вариант 2: 0 - уровень прежний, 1 - изменение уровня
    previous_symbol = '0'
    output_sequence = ''
    for symbol in input_sequence:
        encoded_symbol = invert(previous_symbol) if symbol == '1' else previous_symbol
        output_sequence += encoded_symbol
        previous_symbol = symbol if decode else encoded_symbol
    return output_sequence

def manchester_thomas(input_sequence, decode = False):  #манчестерское кодирование по Томасу
    encoded_dictionary = {'0' : '01', '1' : '10'}
    decoded_dictionary = {'01' : '0', '10' : '1'}
    if decode:
        output_sequence = ''.join([decoded_dictionary[input_sequence[symbol_index:symbol_index + 2]] for symbol_index in range(0, len(input_sequence), 2)])
    else:
        output_sequence = ''.join([encoded_dictionary[symbol] for symbol in input_sequence])
    return output_sequence

def manchester_802_3(input_sequence, decode = False):   #манчестерское кодирование по стандарту 802.3
    encoded_dictionary = {'0' : '10', '1' : '01'}
    decoded_dictionary = {'10' : '0', '01' : '1'}
    if decode:
        output_sequence = ''.join([decoded_dictionary[input_sequence[symbol_index:symbol_index + 2]] for symbol_index in range(0, len(input_sequence), 2)])
    else:
        output_sequence = ''.join([encoded_dictionary[symbol] for symbol in input_sequence])
    return output_sequence

def manchester_diff(input_sequence, decode = False):  #дифференциальное (разностное) манчестерское кодирование
    previous_symbol = '1'
    output_sequence = ''
    if decode:
        output_sequence = '1' if previous_symbol == input_sequence[0] else '0' 
        for symbol_index in range(2, len(input_sequence), 2):
            if input_sequence[symbol_index] == input_sequence[symbol_index - 1]:
                output_sequence += '1'
            else:
                output_sequence += '0'
    else:
        for symbol in input_sequence:
            if symbol == '0' and previous_symbol == '0':
                output_sequence += '10'
            elif symbol == '0' and previous_symbol == '1':
                output_sequence += '01'
            elif symbol == '1' and previous_symbol == '0':
                output_sequence += '01'
            elif symbol == '1' and previous_symbol == '1':
                output_sequence += '10'
            previous_symbol = output_sequence[-1]
    return output_sequence


sequence = input_sequence()

rz_coded = rz_coder(sequence)
rz_decoded = rz_decoder(rz_coded)
print(f"Исх. послед.: {sequence}\n"
      f"Закодировано с использованием RZ кода: {rz_coded}\n"
      f"Декодировано с использованием RZ кода: {rz_decoded}\n"
     )

nrz_coded = nrz_coder(sequence)
nrz_decoded = nrz_decoder(nrz_coded)
print(f"Исх. послед.: {sequence}\n"
      f"Закодировано с использованием NRZ кода: {nrz_coded}\n"
      f"Декодировано с использованием NRZ кода: {nrz_decoded}\n"
     )

nrzi_1_coded = nrzi_1(sequence)
nrzi_2_coded = nrzi_2(sequence)
nrzi_1_decoded = nrzi_1(nrzi_1_coded, True)
nrzi_2_decoded = nrzi_2(nrzi_2_coded, True)
print(f"Исходная последовательность: {sequence}\n"
      f"Закодировано 1-ым вариантом кода NRZI: {nrzi_1_coded}\n"
      f"Закодировано 2-ым вариантом кода NRZI: {nrzi_2_coded}\n"
      f"Декодировано 1-ым вариантом кода NRZI: {nrzi_1_decoded}\n"
      f"Декодировано 2-ым вариантом кода NRZI: {nrzi_2_decoded}\n"
     )

manchester_thomas_coded = manchester_thomas(sequence)
manchester_thomas_decoded = manchester_thomas(manchester_thomas_coded, True)
manchester_802_3_coded = manchester_802_3(sequence)
manchester_802_3_decoded = manchester_802_3(manchester_802_3_coded, True)
manchester_diff_coded = manchester_diff(sequence)
manchester_diff_decoded = manchester_diff(manchester_diff_coded, True)
print(f"Исходная последовательность:                                {sequence}\n"
      f"Закодировано манчестерским кодированием по Томасу:          {manchester_thomas_coded}\n"
      f"Закодировано манчестерским кодированием по стандарту 802.3: {manchester_802_3_coded}\n"
      f"Закодировано дифференциальным манчестерским кодированием:   {manchester_diff_coded}\n"
      f"Декодировано манчестерским кодированием по Томасу:          {manchester_thomas_decoded}\n"
      f"Декодировано манчестерским кодированием по стандарту 802.3: {manchester_802_3_decoded}\n"
      f"Декодировано дифференциальным манчестерским кодированием:   {manchester_diff_decoded}\n"
     )

