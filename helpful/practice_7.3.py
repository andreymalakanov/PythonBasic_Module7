# Andrey Malakanov
# Skillbox PythonBasic

# Practice 7.3 - 1

print('Задача 1. Квадраты чисел')
print()
# Напишите программу, которая выводит квадраты чисел от 0 до 10. Для этого используйте цикл for и функцию range.
for number in range(11):
  print(number ** 2)
print()
print('========================================')
print()


# Practice 7.3 - 2
print('Задача 2. Кукушка')
print()
# Напишите программу, которая имитировала бы часы с кукушкой. В начале работы она спрашивает, который час, а затем нужное количество раз пишет “Ку-ку!”. 
hour = int(input('Который час? '))
for number in range(hour):
  print('Ку-ку!')
print()
print('========================================')
print()


# Practice 7.3 - 3
print('Задача 3. Любовь с первой цифры (цикл for)')
print()
# Перепишите программу из прошлого модуля, используя цикл for.
# Паша очень любит математику. Настолько сильно, что у него по всей комнате висят всякие таблицы умножения, сложения, какие-то графики, формулы. И теперь он захотел распечатать таблицу степеней двойки, у них как раз началась новая тема по информатике.
# Используя цикл for, выведите на экран для числа 2 его степени от 0 до 20.
for exp in range(21):
  print(f'2^{exp} =', 2 ** exp)