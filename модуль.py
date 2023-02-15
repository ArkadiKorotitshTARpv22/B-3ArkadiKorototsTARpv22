def get_population(city, cities):
    if city in cities.keys():
        return f'Популяция {city} равна {cities[city]}.'
    else:
        return 'Такого города нет в списке.' 

def get_city(population, cities, populations):
    if population in populations.keys():
        return f'Популяция {population} равна {cities[population]}.'
    else:
        return f'Популяция {population} равна {cities[population]}.'

def show_inf(cities):
    sorted_tuple = sorted(cities.items())
    return sorted_tuple 

def most_pop(cities):
    big = 0
    town = ''
    for city, pop in cities.items():
        if pop > big:
            big = pop
            town = city
    return f'{town} : {big}'

def less(cities, num):
    my_dic = {}
    for city, pop in cities.items():
        if pop < num:
            my_dic[city] = pop
    return my_dic