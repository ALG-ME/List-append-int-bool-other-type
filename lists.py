# =================================================
# Задание 1
# =================================================
# Работа со списками и срезами.
# Создайте список из 10 элементов с разными типами данных (строки, числа и булевы значения)
# выведите его на экран.
# Используя срезы, выведите на экран первые 5 элементов списка
# последние 3 элемента списка
# каждый второй элемент списка.
# Измените 3 элемент списка на новое значение и выведите измененный список на экран.

map_list = []
map_stop_key = ['rjytw', 'stop', 'всё','конец']
while True:
    user_input = input(f'''
    =============================
    Введите 10 значений, Текущее колл-во: {len(map_list)}
    
    ''')

    if user_input.lower() in map_stop_key or len(map_list) == 10:
        break
    else:
        if user_input.lower() == 'true':
            map_list.append(True)
        elif user_input.lower() == 'false':
            map_list.append(False)
        else:
            try:
                value = int(user_input)
                map_list.append(value)
            except ValueError:
                try:
                    value = float(user_input)
                    map_list.append(value)
                except ValueError:
                    map_list.append(str(user_input))

print(f'''
Список: {map_list}
Кол-во элементов: {len(map_list)}

Используем срез списка:
Вывод первых 5-ти элементов
{map_list[:5]}

Вывод последних 3-х элементов
{map_list[-3:]}

Вывод каждого второго элемента
{map_list[::2]}

''')
new_vacue3 = input('Измените третий элемент списка: ')

map_list[2] = new_vacue3
print(f'''
Изменённый список 
{map_list}''')



# =================================================
# Задание 2
# =================================================
# Работа с условиями и циклами.
# Попросите пользователя ввести число с клавиатуры.
# Если число делится на 3 без остатка, выведите сообщение "Число делится на 3".
# Если число больше 10, выведите сообщение "Число больше 10".
# Если число не удовлетворяет ни одному из условий, выведите сообщение "Число не соответствует условиям".

num = int(input('Ведите число: '))

if num % 3 == 0:
    print('Число делится на 3')
elif num > 10:
    print('Число больше 10')
else:
    print('Число не соответствует условию')
