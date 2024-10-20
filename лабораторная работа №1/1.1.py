1
nomer = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
missing_index = nomer.index(None)  #решили что пропущенный элемент обозначен как None
#считаем сумму и количество элементов без пропущенного
total_sum = sum(num for num in nomer if num is not None)
count = len(nomer)  #количество элементов включая пропуск
#среднее арифметическое
average = total_sum / count  #убираем пропуск из суммы
#замена пропущенного элемента средним арифметическим
nomer[missing_index] = average
print("Измененный список:", nomer)