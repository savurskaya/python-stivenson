#савурская полина, задача 34
a = int(input('введите количество вчерашнего хлеба:'))
s = 3.49 - 3.49*0.6
print('обычная цена буханки 3.49')
print('цена  вчерашней буханки', round(s, 2))
print('общая стоимость покупки', round(a*s, 2))