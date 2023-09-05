"""Создаем функцию которая позволяет найти студентов из трех групп чаще всего встречается человек с именем Павел"""

def find_name():
    line1 = input("Введите список имен группы1:").split()  # Преобразуем строку в список
    line2 = input("Введите список имен группы2:").split()
    line3 = input("Введите список имен группы3:").split()
    counter1 = {} # Создаем пустой словарь
    counter2 = {}
    counter3 = {}

    for word in line1: # Перебираем список
        counter1[word] = counter1.get(word, 0) + 1 # counter[word] В словарь counter мы помещаем ключ со значением word. counter.get(word, 0) смотрим какое значение сейчас хранится под ключем word, по умолчанию ставим 0 . Далее прибавляем +1 "ключ": 0, +1 = "ключ": 1,. Если у ключа есть значение те прибавляем к нему 1 "ключ": 1 -> "ключ": 2
        max_count = max(counter1.values())  # Находим максимальное значение из значения ключа в словаре с помощью метода values()

    for word in line2:
        counter2[word] = counter2.get(word, 0) + 1
        max_count1 = max(counter2.values())

    for word in line3:
        counter3[word] = counter3.get(word, 0) + 1
        max_count2 = max(counter3.values())
    groups = (['goroup1', max_count], ['group2', max_count1], ['group3', max_count2]) # Создаем кортеж
    max_word = 0

    for k, v in groups:  # Перебераем кортеж ключ и значение
        if v > max_word:  # Сравниваем число с max_word = 0. Если больше 0 то
            max_word = v  # Передаем значение ключа в max_word
            group = (k, "Количество повторений:", v)  # Выводим группу с наибольшим значением ключа
            count = ', '.join(map(str, group)) # Преобразовываем кортеж в строку
    return count

print(find_name())

