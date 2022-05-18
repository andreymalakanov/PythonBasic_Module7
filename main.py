students_num = int(input('Введите число: '))
A = 0
B = 0
C = 0
for number in range(1, students_num + 1):
  mark = int(input(f'Введите оценку {number} ученика: '))
  if mark == 5:
    A += 1
  elif mark == 4:
    B += 1
  elif mark == 3:
    C += 1
  else:
    print('Оценка задана неверно')
if (A > B) and (A > C):
  print('Отличников больше!')
elif B > C:
  print('Хорошистов больше!')
else:
  print('Троечников больше!')