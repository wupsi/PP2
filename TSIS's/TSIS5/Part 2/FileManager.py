import os
import os.path
from os.path import isfile


def Russian_menu():
    print(
        '''
-------------------------------------------------------------------------
        • Переместиться в предыдущую папку

        • Переместиться в другую папку
            
        • Показать список всех папок в текущей папке
            
        • Показать список всех файлов в текущей папке
            
        • Удалить файл
            
        • Изменить название файла
            
        • Запись в файл
            
        • Переписать файл
            
        • Изменить название текущей папки
            
        • Создать новый файл
            
        • Создать новую папку
            
        • Выход
-------------------------------------------------------------------------
    ''')


def English_menu():
    print(
        '''
-------------------------------------------------------------------------
        • Move to the previous folder

        • Move to another folder
            
        • Show all folders in the current folder
            
        • Show all files in the current folder
            
        • Delete a file
            
        • Change file name
            
        • Write to file
            
        • Overwrite file
            
        • Change the name of the current folder
            
        • Create new file
            
        • Create a new folder
            
        • Exit
-------------------------------------------------------------------------
    ''')


def Move_prev():
    os.chdir('..')

    if language:
        print('Ваше текущее расположение:', os.getcwd())
        return Russian_menu()

    else:
        print('Your current location:', os.getcwd())
        return English_menu()


def Move_another():

    if language:
        Enter = input(
            'Введите название папки, в которую хотите переместиться: ')
        if Enter:
            os.chdir(Enter)
            print('Ваше текущее расположение:', os.getcwd())
        else:
            print(f'Папки с названием {Enter} не существует!')
        return Russian_menu()

    else:
        Enter = input('Enter the name of the folder you want to move to: ')
        if Enter:
            os.chdir(Enter)
            print('Your current location:', os.getcwd())
        else:
            print(f"File with name {path} doesn't esixts!")
        return English_menu()


def All_folders():

    if language:
        for root, dirs, files in os.walk("."):
            print(root)
        return Russian_menu()

    else:
        for root, dirs, files in os.walk("."):
            print(root)
        return English_menu()


def All_files():
    all_files = []

    for root, dirs, files in os.walk("."):
        for filename in files:
            path = os.path.join(root, filename)
            all_files.append(path)

    if language:
        print('Все файлы в текущей папке и подпапках:')
        for path in all_files:
            print(path)
        return Russian_menu()

    else:
        print('All files in the current folder and subfolders:')
        for path in all_files:
            print(path)
        return English_menu()


def Delete_file():
    all_files = []

    for root, dirs, files in os.walk("."):
        for filename in files:
            path = os.path.join(root, filename)
            all_files.append(path)

    for i in all_files:
        print(i)

    if language:
        path = input(
            'Введите полное название файла вместе с директорией, которое хотите удалить: ')
        if path:
            os.remove(path)
            print(f'Файл с названием {path} удален.')
        else:
            print(f'Файла с названием {path} не существует!')
        return Russian_menu()

    else:
        path = input(
            'Enter the full name of the file along with the directory you want to delete: ')
        if path:
            os.remove(path)
            print(f'File with name {path} deleted.')
        else:
            print(f"File with name {path} doesn't esixts!")
        return English_menu()


def Rename_filename():
    all_files = []

    for root, dirs, files in os.walk("."):
        for filename in files:
            path = os.path.join(root, filename)
            all_files.append(path)

    for i in all_files:
        print(i)

    if language:
        path = input(
            'Введите полное название файла вместе с директорией, которое хотите переименовать: ')
        if path:
            renamed = input('Введите новое название для файла: ')
            os.rename(path, renamed)
            print(f'Файл с названием {path} переименован в {renamed}!')
        else:
            print(f'Файла с названием {path} не существует!')
        return Russian_menu()

    else:
        path = input(
            'Enter the full name of the file along with the directory you want to rename: ')
        if path:
            renamed = input('Enter a new name for the file: ')
            os.rename(path, renamed)
            print(f'File with name {path} renamed to {renamed}!')
        else:
            print(f"File with name {path} doesn't esixts!")
        return English_menu()


def Write_to_file():
    all_files = []

    for root, dirs, files in os.walk("."):
        for filename in files:
            path = os.path.join(root, filename)
            all_files.append(path)

    for i in all_files:
        print(i)

    if language:
        Enter = input('Выберите файл для записи: ')
        if Enter:
            file = open(Enter, 'a')
            file.write(input('Введите текст для записи в файл: '))
            file.close()
            print(open(Enter).read())
        else:
            print(f'Файла с названием {Enter} не существует!')
        return Russian_menu()

    else:
        Enter = input('Select the file to write: ')
        if Enter:
            file = open(Enter, 'a')
            file.write(input('Enter text to write to file: '))
            file.close()
            print(open(Enter).read())
        else:
            print(f"File with name {Enter} doesn't esixts!")
        return English_menu()


def Overwrite_file():
    all_files = []

    for root, dirs, files in os.walk("."):
        for filename in files:
            path = os.path.join(root, filename)
            all_files.append(path)

    for i in all_files:
        print(i)

    if language:
        Enter = input('Выберите файл для записи: ')
        if Enter:
            file = open(Enter, 'w')
            file.write(input('Введите текст для записи в файл: '))
            file.close()
            print(open(Enter).read())
        else:
            print(f'Файла с названием {Enter} не существует!')
        return Russian_menu()

    else:
        Enter = input('Select the file to write: ')
        if Enter:
            file = open(Enter, 'w')
            file.write(input('Enter text to write to file: '))
            file.close()
            print(open(Enter).read())
        else:
            print(f"File with name {Enter} doesn't esixts!")
        return English_menu()


def Rename_foldername():

    if language:
        Enter = input('Введите новое название папки: ')
        os.chdir(Enter)
        print(f'Название папки изменилось на {Enter}:', os.getcwd())
        return Russian_menu()

    else:
        Enter = input('Enter the new folder name: ')
        os.chdir(Enter)
        print(f'The folder name has changed to {Enter}:', os.getcwd())
        return English_menu()


def Create_file():

    if language:
        Enter = input('Введите название нового файла: ')
        txt = open(Enter)
        print(f'Файл с названием {Enter} создана!')
        return Russian_menu()

    else:
        Enter = input('Enter a name for the new file: ')
        txt = open(Enter)
        print(f'File with name {Enter} created!')
        return English_menu()


def Create_folder():

    if language:
        Enter = input('Введите название новой папки: ')

        if not os.path.isdir(Enter):
            os.mkdir(Enter)
            print(f'Папка с названием {Enter} создана!')
            return Russian_menu()

        else:
            print(f'Папка с названием {Enter} уже существует!')
            return Russian_menu()

    else:
        Enter = input('Enter the name of the new folder: ')

        if not os.path.isdir(Enter):
            os.mkdir(Enter)
            print(f'Folder with name {Enter} is created!')
            return English_menu()
        else:
            print(f'Folder with name {Enter} already exists!')
            return English_menu()


while True:

    entered_language = input(
        '''
    Please select a language to continue working with File Manager.
    • English
    • Русский
    • exit

    ''')

    # Ввод языка
    if entered_language.lower() == 'русский':
        language = True
        print(
            '''--------------------------------------------------------------------------
    Вас приветствует Файловый Менеджер!

    Ваше текущее расположение:''', os.getcwd(),
            '\n\n    Список файлов и папок в текущей папке:\n\n   ', os.listdir(
                path='.'),
            '\n\n    Возможные запросы:')
        Russian_menu()
        break

    elif entered_language.lower() == 'english':
        language = False
        print(
            '''--------------------------------------------------------------------------
    File Manager welcomes you!

    Your current location:''', os.getcwd(),
            '\n\n    All files and folders in the current folder:\n\n   ', os.listdir(
                path='.'),
            '\n\n    Possible requests:')
        English_menu()
        break

    elif entered_language.lower() == 'exit':
        exit()
    else:
        print('''The language was entered incorrectly. Please, enter "English" or "Русский
--------------------------------------------------------------------------''')


while True:

    enter = input()

    # If language is "Русский"
    if language:

        if enter.lower() == 'выход':
            print('Досвидули!')
            exit()

        elif enter.lower() == 'переместиться в предыдущую папку':
            Move_prev()

        elif enter.lower() == 'переместиться в другую папку':
            Move_another()

        elif enter.lower() == 'показать список всех папок в текущей папке':
            All_folders()

        elif enter.lower() == 'показать список всех файлов в текущей папке':
            All_files()

        elif enter.lower() == 'удалить файл':
            Delete_file()

        elif enter.lower() == 'изменить название файла':
            Rename_filename()

        elif enter.lower() == 'запись в файл':
            Write_to_file()

        elif enter.lower() == 'переписать файл':
            Overwrite_file()

        elif enter.lower() == 'изменить название текущей папки':
            Rename_foldername()

        elif enter.lower() == 'создать новый файл':
            Create_file()

        elif enter.lower() == 'создать новую папку':
            Create_folder()

        else:
            print(
                'Введен некорректный запрос. Введите один из вышеперечисленных запросов.')

    # If language is "English"
    else:

        if enter.lower() == 'exit':
            exit()

        elif enter.lower() == 'move to the previous folder':
            Move_prev()

        elif enter.lower() == 'move to another folder':
            Move_another()

        elif enter.lower() == 'show all folders in the current folder':
            All_folders()

        elif enter.lower() == 'show all files in the current folder':
            All_files()

        elif enter.lower() == 'delete a file':
            Delete_file()

        elif enter.lower() == 'change file name':
            Rename_filename()

        elif enter.lower() == 'write to file':
            Write_to_file()

        elif enter.lower() == 'overwrite file':
            Overwrite_file()

        elif enter.lower() == 'change the name of the current folder':
            Rename_foldername()

        elif enter.lower() == 'create new file':
            Create_file()

        elif enter.lower() == 'create a new folder':
            Create_folder()

        else:
            print('Invalid request entered. Enter one of the above queries.')
