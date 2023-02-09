import view
import csv
import os

student_id_counter = 0
students = {}
classes = {}

def Add_New_Student():
    new_student = dict()
    new_student['Id'] = Get_New_Id()
    new_student['First name'] = view.Get_New_Student_Info('student`s first name')
    new_student['Last name'] = view.Get_New_Student_Info('student`s last name')
    new_student['Birthday'] = view.Get_New_Student_Info('student`s birthday')
    Add_Students_In_Classes(new_student['Id'])
    return new_student

def Save_Students(student):
    with open ('Seminar_8_CW/students.csv', 'a') as file:
        file.write(f"{student['Id']};{student['First name']};{student['Last name']};{student['Birthday']}\n")

def Get_New_Id():
    global student_id_counter
    # pass # Заглушка. Ставится чтобы программа не ругалась на некоторый незаконченный объект
    student_id_counter += 1
    return student_id_counter

def Add_Students_In_Classes(student_id):
    global classes
    student_class = view.Get_New_Student_Info('students`s class')
    if student_class in classes:
        classes[student_class].append(student_id)
    else:
        classes[student_class] = [student_id]

def Get_Last_Student_Id():
    global student_id_counter
    with open('Seminar_8_CW/last_student_Id.txt', 'r', encoding='utf-8') as f: #  encoding='utf-8' - Чтобы в Винде руские буквы были видны в csv-файлах. Эксель не понимает эту кодировку.
        student_id_counter = int(f.read())
    return student_id_counter

def Save_Last_Student_Id():
    global student_id_counter
    with open('Seminar_8_CW/last_student_Id.txt', 'w', encoding='utf-8') as f:
        f.write(str(student_id_counter))

def Save_Classes():
    with open ('Seminar_8_CW/classes.txt', 'w') as file:
        for key, value in classes.items():
            file.write(key + ' - ' + str(value) + '\n')

def Get_Classes():
    global classes
    classes = {}
    with open ('Seminar_8_CW/classes.txt', 'r') as file:
        temp = file.readlines()
        for element in temp:
            l = list(element[element.index('[')+1:-2].split(', '))
            new_l = list()
            for i in l:
                i = int(i)
                new_l.append(i)
            classes[element[:element.index(' - ')]] = new_l

def Import_Data(path):
    global student_id_counter
    student_id_counter = Get_Last_Student_Id()
    exp_data = dict()
    with open(path, 'r', newline='') as file:
        title  = ['Id', 'First name', 'Last name', 'Birthday', '\n']
        for line in file:
            line = line.split(';')
            if line != title:
                student_id_counter += 1
                for i in range(len(line)):
                    if '\n' in line[i]:
                        line[i] = line[i].replace('\n', '')
                if line[0].isdigit():
                    exp_data[student_id_counter] = line[1::]
                else:
                    exp_data[student_id_counter] = line
    return exp_data
    
def Save_Import_Students(student):
    global classes
    with open ('Seminar_8_CW/students.csv', 'a') as file:
        for elem in student.items():
            file.write(f'{elem[0]};{elem[1][0]};{elem[1][1]};{elem[1][2]}\n')
            student_class = view.Get_New_Student_Info(f'В каком классе учился {elem[1][0]} \
{elem[1][1]} дата рождения {elem[1][2]}?')
            if student_class in classes:
                classes[student_class].append(elem[0])
            else:
                classes[student_class] = [elem[0]]

def Export_Data():
    exp_data = dict()
    with open('Seminar_8_CW/students.csv', 'r', newline='') as file:
        title  = ['Id', 'First name', 'Last name', 'Birthday', '\n']
        for line in file:
            line = line.split(';')
            if line != title:
                for i in range(len(line)):
                    if '\n' in line[i]:
                        line[i] = line[i].replace('\n', '')
                student_id_counter = line[0]
                exp_data[student_id_counter] = line[1::]
    return exp_data

def Save_Export_Students(student, path):
    with open (path, 'a') as file:
        for elem in student.items():
            file.write(f'{elem[0]};{elem[1][0]};{elem[1][1]};{elem[1][2]}\n')

def Save_Exp_Classes(path):
    with open (path + '/classes_export.txt', 'w') as file:
        for key, value in classes.items():
            file.write(key + ' - ' + str(value) + '\n')

def Save_Exp_in_Data_Classes(path, clas):
    with open (path, 'w') as file:
        for key, value in clas.items():
            file.write(key + ' - ' + str(value) + '\n')

def Get_Classes_on_Export(path):
    global classes_EXP
    classes_EXP = {}
    with open (path, 'r') as file:
        temp = file.readlines()
        for element in temp:
            l = list(element[element.index('[')+1:-2].split(', '))
            new_l = list()
            for i in l:
                i = int(i)
                new_l.append(i)
            classes_EXP[element[:element.index(' - ')]] = new_l

def Update_Two_Dict():
    global classes
    global classes_EXP
    temp = dict()
    for i in classes.items():
        for j in classes_EXP.items():
            if i[0] == j[0]:
                temp[i[0]] = i[1] + j[1]
    upd_data = {**classes, **classes_EXP, **temp}
    return upd_data

def All_Students_Sorted(find_atribut):
    global key_atribut
    data = dict()
    temp_list = list()
    with open('Seminar_8_CW/students.csv', 'r', newline='') as file:
        for line in file:
            line = line.split(';')
            for i in range(len(line)):
                if '\n' in line[i]:
                    line[i] = line[i].replace('\n', '')
            temp_list = line.copy()
            match find_atribut:
                case 'По Имени и Фамилии':
                    name = temp_list.pop(1)
                    surname = temp_list.pop(1)
                    data[f'{name} {surname}'] = temp_list
                case 'По уникальному Ключу':
                    data[line[0]] = line[1::]
                case 'По Дате рождения':
                    data[line[3]] = line[:3:]
            key_atribut = find_atribut
    os.system('clear')
    print('Вот все данные отсортированные по выбранному параметру')
    for i in data.items():
        print(i)
    return data

def Delete_Student(data):
    global pop_student
    for i in data.items():
        print(i)
    key_delete = view.Enter_Key_Student()
    if key_delete in data:
        pop_student = data.pop(key_delete)
    print(f'Ученик {pop_student} - удален\n\
Остались:')
    for i in data.items():
        i
    return data

def Edit_Student_v2(data):
    pop_student = dict()
    for i in data.items():
        print(i)
    key_edit_student = view.Enter_Key_Student() # Ключ изменяемого студента
    pop_student[key_edit_student] = data[key_edit_student]
    data.pop(key_edit_student)
    key = view.Find_Edit_Atribut()
    match key:
        case 'уникальный ключ':
            new_atribut = view.New_Atribut(key, pop_student)
            pop_student[new_atribut] = pop_student[key_edit_student]
            data[new_atribut] = pop_student[key_edit_student]
        case 'имя':
            new_atribut = view.New_Atribut(key, pop_student)
            for value in pop_student.values():
                value[0] = new_atribut
            data[key_edit_student] = pop_student[key_edit_student]
        case 'фамилию':
            new_atribut = view.New_Atribut(key, pop_student)
            for value in pop_student.values():
                value[1] = new_atribut
            data[key_edit_student] = pop_student[key_edit_student]
        case 'дату рождения':
            new_atribut = view.New_Atribut(key, pop_student)
            for value in pop_student.values():
                value[2] = new_atribut
            data[key_edit_student] = pop_student[key_edit_student]            
    return(data)

def Save_Edit_Students(student, path):
    with open (path, 'w') as file:
        for elem in student.items():
            file.write(f'{elem[0]};{elem[1][0]};{elem[1][1]};{elem[1][2]}\n')

def Return_Started_Sort_Data(data):
    new_data = dict()
    global key_atribut
    match key_atribut:
        case 'По Имени и Фамилии':
            for i in data.items():
                new_data[i[1][0]] = [i[0].split(' ')[0], i[0].split(' ')[1], i[1][1]]
        case 'По уникальному Ключу':
            new_data = data.copy()
        case 'По Дате рождения':
            for i in data.items():
                new_data[i[1][0]] = [i[1][1], i[1][2], i[0]]
    return new_data
