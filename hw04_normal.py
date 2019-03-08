# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email.
# Теперь необходимо совершить проверки, имя и фамилия должны иметь
# заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате:
# текст в нижнем регистре, допускается нижнее подчеркивание и цифры,
# потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя,
# te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net),
# te_4_st@test.com - верно указан.

import re
name = input('Введите имя с большой буквы: ')
surname = input('Введите фамилию с большой буквы: ')
mail = input('Введите e-mail : ')

pattern_name = '^[А-Я]+[а-я]{2,20}'
check_name = (re.match(pattern_name, name))
check_surname = (re.match(pattern_name, surname))
print(check_name.group(0))
print(check_surname.group(0))

pattern_mail = '[a-z_0-9]+@[a-z0-9]+\.[com|org|ru]'
check_mail = (re.match(pattern_mail, mail))
print(check_mail.group())

re.match(pattern, string)

# Задача - 2:
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

dot_pat = '\.{2}'
a = (re.search(dot_pat, some_str))
# print (a.group())
if a:
    print ('Есть более одной точки')
else:
    print ('более одной точки нет')
#
#
#
# ljh