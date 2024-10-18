numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
N=numbers.index(None)
lenN=len(numbers)
sumN=sum(numbers[:N])+sum(numbers[N+1:])
numbers[N]=sumN/lenN
print("Измененный список:", numbers)
