#Практикум 12.7.3

#Напишите программу, в результате которой будет сформирован список deposit значений — накопленные средства за год вклада в каждом из банков. На вход программы с клавиатуры вводится сумма money, которую человек планирует положить под проценты.
#Объявляем переменную в тип int #Сумму вводим с клавиатуры

money = int(input("Enter sum: ")) 

#Имеем словарь со значениями процентных ставок в банках
# Объявляем депозиты в список

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [] 
#Составляем программу с помощью цикла для вычисления процентов
#Оборачиваем результат в целочисленные числа
#Добавляем полученный результат в список deposit

for value in per_cent.values():
   result = int(money / 100 * value)  
   deposit.append(result)
print(deposit)

#Выявляем максимальную сумму которую можно вынести

print(max(deposit))
