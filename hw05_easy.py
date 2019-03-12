# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil
# # print(os.name)
def make_new_dir(comm_name):
    new_dir = (comm_name)
    path = os.path.join(os.getcwd(), new_dir)
    try:
        os.mkdir(path)
    except FileExistsError:
        print(new_dir, ': уже существует')
    return


def delete_dir(dir_name):
    del_dir = (dir_name)
    path = os.path.join(os.getcwd(), del_dir)
    try:
        os.rmdir(path)
    except FileExistsError:
        print(new_dir, ': не существует')
    return

def print_curr_dir():
    curr_dir = os.getcwd()
    print(os.listdir(curr_dir))
    return

# if __name__ == '__main__':
# number = input('Сколько директорий создать? (1-9): ')
# i=1
# while i <= int(number):
#     make_new_dir('dir_'+str(i))
#     i+=1
# input('type anykey')
# i=1
# while i <= int(number):
#     delete_dir('dir_'+str(i))
#     i+=1
# input('End od Task 1. type anykey')
#
# # Задача-2:
# # Напишите скрипт, отображающий папки текущей директории.
# # os.getcwd() - текущая рабочая директория.
# # os.listdir(path=".") - список файлов и директорий в папке.
#
# print_curr_dir()
# input('End od Task 2. type anykey')
#
# # Задача-3:
# # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
#
# work_file_name = os.path.basename(__file__)
# print(work_file_name)
# shutil.copy(work_file_name, 'copy_'+work_file_name)
# input('End od Task 3. type anykey')
#
