# Moving in directories/ Work with files

# Location
# 1. rename directory
# 2. print number of files
# 3. print number of directories
# 4. list content of the directory
# 5. add file to this directory
# 6. add new directory to this directory

import os
import os.path

print('Текущая директория:', os.getcwd())

if not os.path.isdir('Folder'): 
    os.mkdir('Folder')
    print('Новая папка создана!')

if os.path.isdir('Folder'):
    os.chdir('NameChange')
    print('Название папки изменено!')

