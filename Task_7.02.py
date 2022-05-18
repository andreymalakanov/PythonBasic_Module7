# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 2. Должники')

# Должники и законопослушные граждане хранятся в одной базе банка.
# Из этой базы нам выделяются по 10 человек, у каждого из которых есть свой номер.
# Правда, иногда база глючит и выдаёт нам отрицательный номер.
# А ещё по статистике, которую собрал наш МирПрогБанк, 
# каждый второй, кто в этом году брал кредит, не выплатил его вовремя.
# 
# Пользователь вводит 10 чисел.
# Напишите программу,
# которая определяет, сколько из них являются одновременно четными и положительными.

counter = 0
for number in range(1,11):
  i = int(input(f'Введите {number} число: '))
  if (i % 2 == 0) and (i > 0):
    counter += 1
if counter > 1:
  print(f'Чётными и положительными являются {counter} числа')
elif counter == 1:
  print('Чётным и положительным является 1 число')
else:
  print('Нет четных и положительных чисел')