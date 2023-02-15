#Arkadi Korotitsh TARpv22

from модуль import *

cities = []
populations = []
print("сделано Arkadi Korotitsh TARpv22")
while True:
    city = input('Введите название города. ')
    population = int(input('Введите население этого города. '))
    cities.append(city)
    populations.append(population)
    escape = input('Введите "e" для завершения ввода данных о городах \
или Enter для продолжения. ')
    if escape.lower() == 'e':
        break

city_dict = dict(zip(cities, populations))


while True:
    command = input('Команды: \n1-Узнать, вводя название города,  сколько в нем жителей\n2-Отобразить в алфавитном порядке список городов и количество жителей\n3-Найти населенность города, введя его название\n4-Найти города в которых живет меньше, чем n жителей\n5-найти город с самым высоким населением\n6-выйти\n')
    if command == '1':
        city = input('Введите название города. ')
        print(get_population(city, city_dict))
    if command == '3':
        city = int(input('Введите количество населения. '))
        print(get_city(city,populations, city_dict))
    if command == '2':
        print(show_inf(city_dict))
    if command == '5':
        print(most_pop(city_dict))
    if command == '4':
        num = int(input('Введите количество населения. '))
        print(less(city_dict, num))
    if command == '6':
        break
        