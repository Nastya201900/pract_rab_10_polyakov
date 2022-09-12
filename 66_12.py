def ff(file, rashirenie):
    if '.' not in file:
        return (file + '.' + rashirenie)
    else:
        i = -1
        while file[i] != '.':
            file = file[0:i]
        return (file + rashirenie)
f = input('Введите имя файла: ')
e = input('Введите новое расширение: ')
print('Результат:', ff(f, e))