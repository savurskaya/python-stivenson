#савурская полина, задача 38
a = int(input('введите количество сторон:'))
if a == 3: 
    print('треугольник')
elif a == 4:
    print('четырехугольник')
elif a == 5:
    print('пятиугольник')
elif a == 6:
    print('шестиугольник')
elif a == 7:
    print('семиугольник')
elif a == 8:
    print('восьмиугольник')
elif a == 9:
    print('девятиугольник')
elif a == 10:
    print('десятиугольник')
elif 3 > a or a > 10:
    print('неверно введено число сторон')