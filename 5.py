# 📍 Программа, которая составляет список чисел Фибоначчи, 
# в том числе для отрицательных индексов. 

def fibonacci(num):
    result = [-1, 1, 0, 1, 1]
    for i in range(len(result) + 1, num + 4):
        result.insert(-i, result[-i + 2] - result[-i + 1]) 
    for i in range (len(result), num + len(result) - 2):
        result.append (result[i - 1] + result[i - 2])
    return result
k = int(input("✏️  Введите 'k': "))
print(fibonacci(k))