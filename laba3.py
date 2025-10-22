# Пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Что делаем:
# 1. Сравниваем соседние элементы.
# 2. Меняем их местами, если порядок неправильный.
# 3. Самое большое число постепенно "всплывает" к концу списка.


# Сортировка выбором
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Что делаем:
# 1. Ищем минимальный элемент в неотсортированной части.
# 2. Меняем его с первым элементом этой части.
# 3. Повторяем для всей длины списка.


# Сортировка вставками
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Что делаем:
# 1. Берём элемент и ищем место в уже отсортированной части слева.
# 2. Сдвигаем элементы вправо, чтобы освободить место.
# 3. Вставляем текущий элемент на правильное место.


# Тестируем и выводим результат
d = list(int(input()))
print("Пузырьковая сортировка:", bubble_sort(d.copy()))
print("Сортировка выбором:", selection_sort(d.copy()))
print("Сортировка вставками:", insertion_sort(d.copy()))













