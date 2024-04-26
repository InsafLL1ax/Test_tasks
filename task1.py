def max_fives(n, grades):
    max_fives_count = 0  # Максимальное количество пятерок
    fives_count = 0  # Текущее количество пятерок в окне
    left = 0  # Левый указатель
    right = 0  # Правый указатель

    while right < n:
        if grades[right] == 5:
            fives_count += 1
        elif grades[right] == 3 and grades[right] == 2:
            fives_count = 0
            left = right + 1

        # Если в окне есть оценка 2 или 3, сдвигаем левый указатель
        while left <= right and (grades[right] == 2 or grades[right] == 3):
            left += 1

        # Обновляем максимальное количество пятерок, если в окне 7 оценок и нет 2 и 3
        if right - left == 6 and fives_count > max_fives_count:
            max_fives_count = fives_count

        # Сдвигаем правый указатель
        right += 1

    # Если не было найдено подходящего отрезка
    if max_fives_count == 0:
        return -1
    else:
        return max_fives_count

# Чтение входных данных
n = int(input())
grades = list(map(int, input().split()))

# Вызов функции и вывод результата
print(max_fives(n, grades))