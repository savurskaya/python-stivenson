#савурская полина, задача 52
a = input('введите буквенную оценку')
if a == 'A+':
    print('5.0')
elif a == 'A':
    print('4.0')
elif a == 'A-':
    print('3.7')
elif a == 'B+':
    print('3.3')
elif a == 'B':
    print('3.0')
elif a == 'B-':
    print('2.7')
elif a == 'C+':
    print('2.3')
elif a == 'C':
    print('2.0')
elif a == 'C-':
    print('1.7')
elif a == 'D+':
    print('1.3')
elif a == 'D':
    print('1.0')
elif a == 'F':
    print('0')
else:
    print('неправильный формат оценки')