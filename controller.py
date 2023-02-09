import view
import model

def Buttom():
    model.Get_Last_Student_Id()
    model.Get_Classes()
    stop = False
    while not stop:
        match view.Choice_Start_Menu():
            case 'Работа с учениками':
                match view.New_Student_or_Not():
                    case 'Добавить нового ученика':
                        model.Save_Students(model.Add_New_Student())
                        if view.Get_New_Student_Info('"q" - нажмите чтобы выйти или "Enter" чтобы продолжить\n-> ').lower() == 'q':
                            stop  = True
                        model.Save_Classes()
                        model.Save_Last_Student_Id()
                    case 'Работать с базой данных по ученикам':
                        stop_edit_data = False
                        while not stop_edit_data:
                            match view.Choice_DEL_or_EDIT_or_Sort():
                                case 'Сортировать учеников по какому то параметру':
                                    data = model.All_Students_Sorted(view.Find_Atribut())
                                    data = model.Return_Started_Sort_Data(data)
                                case 'Редактировать ученика':
                                    model.Save_Edit_Students(model.Edit_Student_v2(model.Export_Data()))
                                case 'Удалить ученика':
                                    data = model.Delete_Student(model.Export_Data())
                                    path = 'Seminar_8_CW/students.csv'
                                    model.Save_Edit_Students(data, path)
                                    stop_edit_data = True
                                case 'Выйти из этого меню':
                                    stop_edit_data = False


            case 'Перенесем нашу базу в другую (экспорт)':
                match view.Choice_Export_Method():
                    case 'Создать новый файл для экспорта':
                        name = view.Name_New_Data()
                        path = view.Path_to_Export_Data()
                        data = model.Export_Data()
                        model.Save_Export_Students(data, path + '/' + name)
                        model.Save_Exp_Classes(path)
                        if view.Get_New_Student_Info('"q" - нажмите чтобы выйти или "Enter" чтобы продолжить\n-> ').lower() == 'q':
                            stop  = True
                    case 'Экспорт базы в другую базу':
                        path = view.Path_to_Export_Data_in_Data()
                        model.Save_Export_Students(model.Export_Data(), path)
                        path_classes = view.Path_to_Exported_Classes()
                        model.Get_Classes_on_Export(path_classes)
                        model.Get_Classes()
                        model.Save_Exp_in_Data_Classes(path_classes, model.Update_Two_Dict())
                        if view.Get_New_Student_Info('"q" - нажмите чтобы выйти или "Enter" чтобы продолжить\n-> ').lower() == 'q':
                            stop  = True

            case 'Перенесем данные из другой базы в нашу (импорт)':
                model.Get_Last_Student_Id()
                model.Get_Classes()
                path = view.Path_to_Data()
                import_students_data = model.Import_Data(path)
                model.Save_Import_Students(import_students_data)
                model.Save_Last_Student_Id()
                model.Save_Classes()
                if view.Get_New_Student_Info('"q" - нажмите чтобы выйти или "Enter" чтобы продолжить\n-> ').lower() == 'q':
                    stop = True
            
            case 'q':
                stop = True
