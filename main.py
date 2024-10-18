task1=input("Введите дату:  ")
task2=input("Введите задачу:  ")
task3=input("Введите дату:  ")
task4=input("Введите задачу:  ")
task5=input("Введите дату:  ")
task6=input("Введите задачу:  ")


print(task1, task2, task3, task4, task5, task6)

countries = {
  'Введите дату':'Сегодня', 
  'Введите задачу':'Выучить Pythton'
}
countries1 = {
    'Введите дату':'Завтра',
  'Введите задачу':'Разработать TODO-приложение'
  }

countries2 = {
    'Введите дату':'Послезавтра',
  'Введите задачу':'Разработать Telegram-бота'
}

print("Введите дату: %s" %countries["Введите дату"])
print("Введите задачу: %s" %countries["Введите задачу"])
print("Введите дату: %s" %countries1["Введите дату"])
print("Введите задачу: %s" %countries1["Введите задачу"])
print("Введите дату: %s" %countries2["Введите дату"])
print("Введите задачу: %s" %countries2["Введите задачу"])



#Решение эталонное
date = input('Введите дату: ')
task = input('Введите задачу: ')
​
s = date + ' ' + task
print(s)
​
# Альтернативное решение
print(date, task)
# print может выводить на экран сразу несколько строк через пробел

#Задача №2
date_1 = input('Введите дату: ')
task_1 = input('Введите задачу: ')
date_2 = input('Введите дату: ')
task_2 = input('Введите задачу: ')
date_3 = input('Введите дату: ')
task_3 = input('Введите задачу: ')

print(date_1, task_1)
print(date_2, task_2)
print(date_3, task_3)

#Задача №3
task_dict = {}

date = input('Введите дату: ')
task = input('Введите задачу: ')
task_dict[date] = task

date = input('Введите дату: ')
task = input('Введите задачу: ')
task_dict[date] = task


date = input('Введите дату: ')
task = input('Введите задачу: ')
task_dict[date] = task

# Если хотите лучше понять это решение - добавьте вывод на экран после каждого пользовательского ввода
# print(date, task)
# print(task_dict)
# Вы увидите, что переменные date и task изменяются, но данные в словаре task_
