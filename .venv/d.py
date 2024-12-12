import os

def print_directory_tree(path, indent=0):
    try:
        # Получаем список файлов и папок в текущей директории
        items = os.listdir(path)
    except PermissionError:
        print("Нет доступа к папке:", path)
        return

    # Для каждого элемента в директории
    for item in items:
        # Полный путь к элементу
        full_path = os.path.join(path, item)

        # Выводим название элемента с отступом
        print(' ' * indent + item)

        # Если это директория, вызываем рекурсивно функцию для нее
        if os.path.isdir(full_path):
            print_directory_tree(full_path, indent + 4)

# Указываем путь к папке
folder_path = '/home/upsfffaaa/Загрузки/wpf-daily-planner-main'
print(folder_path)
print_directory_tree(folder_path)
