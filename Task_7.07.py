# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 7. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
counter = 0
counter_sum = 0
if a > b:
  a, b = b, a
for number in range (a, b + 1):
  if number % 3 == 0:
    counter += 1
    counter_sum += number
#    print(counter, counter_sum)
if counter >= 1:
  print('Ответ:', counter_sum / counter)
else:
  print('Указан слишком короткий диапазон')