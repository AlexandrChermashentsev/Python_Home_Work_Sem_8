def Get_New_Student_Info(message):
    return input(f'{message}: ')

def Choice_Start_Menu():
    choice = input('Что будем делать?\n\
"1" - Работа с учениками\n\
"2" - Перенесем нашу базу в другую (экспорт)\n\
"3" - Перенесем данные из другой базы в нашу (импорт)\n\
"q" - Выход\n\
-> ')
    match choice:
        case '1':
            choice = 'Работа с учениками'
        case '2':
            choice = 'Перенесем нашу базу в другую (экспорт)'
        case '3':
            choice = 'Перенесем данные из другой базы в нашу (импорт)'
        case 'q':
            choice = 'q'
    return choice

def Path_to_Data():
    return input('Введите полный путь к файлу (csv) -> ') + '.csv'

def Path_to_Export_Data():
    return input('Введите путь в который вы хотите экспортировать базу данных\n\
Студенты будут выгружены в формате: Уникальный ключь;Имя;Фамилия;Дата рождения(день-месяц-год)\n\
Введите путь -> ')

def Name_New_Data():
    return input('Как назовем ваш новый файл? ') + '.csv'

def Path_to_New_Classes():
    return input

def Path_to_Export_Data_in_Data():
    return input('Введите полный путь (Путь + имя файла) в который вы хотите экспортировать базу данных\n\
Студенты будут выгружены в формате ".csv": Уникальный ключь;Имя;Фамилия;Дата рождения(день-месяц-год)\n\
Введите путь -> ') + '.csv'

def Path_to_Exported_Classes():
    return input('Введите полный путь до файла с данными о классах\n\
-> ') + '.txt'

def Choice_Export_Method():
    choice = input('Сохраним в существующий файл или создадим новый?\n\
"1" - Создать новый файл для экспорта\n\
"2" - Экспорт базы в другую базу\n\
-> ')
    match choice:
        case '1':
            choice = 'Создать новый файл для экспорта'
        case '2':
            choice = 'Экспорт базы в другую базу'
    return choice

def Find_Atribut():
    atribut = input('По каким параметрам будем искать ученика?\n\
"1" - по уникальному Ключу\n\
"2" - по Имени и Фамилии\n\
"3" - по Дате рождения\n\
-> ')
    match atribut:
        case '1':
            atribut = 'По уникальному Ключу'
        case '2':
            atribut = 'По Имени и Фамилии'
        case '3':
            atribut = 'По Дате рождения'
    return atribut

def New_Student_or_Not():
    choice = input('Добавим нового ученика или будем работать с базой учеников?\n\
"1" - Добавить нового ученика\n\
"2" - Работать с базой данных по ученикам\n\
-> ')
    match choice:
        case '1':
            choice = 'Добавить нового ученика'
        case '2':
            choice = 'Работать с базой данных по ученикам'
    return choice

def Enter_Key_Student():
    return input('Введите ключ ученика\n-> ')

def Find_Edit_Atribut():
    choice = input('Введите какой параметр хотите изменить в данных ученика\n\
"1" - Уникальный ключ\n\
"2" - Имя\n\
"3" - Фамилия\n\
"4" - Дата рождения\n-> ')
    match choice:
        case '1':
            choice = 'уникальный ключ'
        case '2':
            choice = 'имя'
        case '4':
            choice = 'дату рождения'
        case '3':
            choice = 'фамилию'
    return choice

def Choice_DEL_or_EDIT_or_Sort():
    choice = input('Что будем делать с учеником?\n\
"1" - Редкатировать данные ученика\n\
"2" - Удалить ученика из базы данных\n\
"3" - Сортировать учеников\n\
"q" - Выйти из этого меню\n\
-> ')
    match choice:
        case '1':
            choice = 'Редактировать ученика'
        case '2':
            choice = 'Удалить ученика'
        case 'q':
            choice = 'Выйти из этого меню'
        case '3':
            choice = 'Сортировать учеников по какому то параметру'
    return choice

def New_Atribut(key, student):
    return input(f'Вы выбрали поменять {key} у ученика {list(student.items())}. Введите новое значение -> ')

