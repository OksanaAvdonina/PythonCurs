# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко 
# он их придумывает, Вам стоит написать программу. Винни-Пух считает, что 
# ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе 
# стихотворения одинаковое. Фраза может состоять из одного слова, если 
# во фразе несколько слов, то они разделяются дефисами. Фразы отделяются 
# друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с 
# клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам  
'''
letters_list = ["а", "у", "е", "о", "э", "я", "и", "ю"]

new_string = list(input('Введи считалочку: ').lower().split())

result_array = []

def counting_rhyme(letter_list,phrase_list, result_array):
    i = 0
    count = 0
    while i < len(phrase_list):
        for j in range(len(letter_list)):
            if letter_list[j] in phrase_list[i]:
                count += phrase_list[i].count(letter_list[j])
        result_array.append(count)
        count = 0
        i += 1

    if len(set(result_array)) == 1:
        return 'Парам пам-пам'
    else:
        return 'Пам парам'

print(counting_rhyme(letters_list, new_string, result_array))
'''


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки 
# и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, 
# почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой 
# ровно два аргумента, как, например, у операции умножения.

# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**

# 1   2   3   4   5   6
# 2   4   6   8   10  12
# 3   6   9   12  15  18
# 4   8   12  16  20  24
# 5   10  15  20  25  30
# 6   12  18  24  30  36
'''
def print_operation_table(operation, num_rows=6, num_columns=9):
    for i in range(1, num_rows + 1):
        print(f"{i}\t", end='') # выводим номер строки
        for j in range(2, num_columns + 1):
            if i == 1:
                print(f"{j}\t", end='') # выводим номер столбца
            else:
                print(f"{operation(i, j)}\t", end='')
        print()


print("\n ТАБЛИЦА СЛОЖЕНИЯ: ")
print()
print_operation_table(lambda x, y: x + y)
print("\n ТАБЛИЦА УМНОЖЕНИЯ: ")
print()
print_operation_table(lambda x, y: x * y)
print("\n ТАБЛИЦА СТЕПЕНЕЙ: ")
print()
print_operation_table(lambda x, y: x ** y)
'''