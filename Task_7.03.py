# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 3. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.
 
# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев 
# и выводит на экран среднюю зарплату за год.

income = 0
for mounth in range(1,13):
  salary = int(input(f'Введите зарплату за {mounth} месяц: '))
  income += salary
average_salary = income // 12 
print(f'Средняя зарплата за год составляет {average_salary}')
