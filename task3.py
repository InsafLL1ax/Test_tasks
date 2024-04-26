def build_directory_structure(n):
    directories = {}

    for _ in range(n):
        path = input()
        parts = path.split('/')  # Разделяем путь на части
        current_level = directories  # Начинаем с корневого уровня директорий

        for part in parts:
            if part != '':  # Игнорируем пустые части пути
                if part not in current_level:
                    current_level[part] = {}  # Добавляем вложенную директорию, если её ещё нет
                current_level = current_level[part]  # Перемещаемся во вложенную директорию

    return directories

def print_directory_structure(directory, indent=0):
    for key, value in directory.items():
        print('  ' * indent + key)  # Печатаем имя директории с отступом
        print_directory_structure(value, indent + 1)  # Рекурсивно печатаем вложенные директории

# Получаем количество директорий
n = int(input())

# Строим структуру директорий
directory_structure = build_directory_structure(n)

# Выводим структуру директорий
print_directory_structure(directory_structure)