# 📍 Программа, которая находит произведение пар чисел списка. 
# (Парой считается первый и последний элемент, второй и предпоследний и т.д.)

my_list=[2, 3, 4, 5, 6]
import math 
size = math.ceil(len(my_list)/2)
my_list2 = []
for i in range(size):
    my_list2.append(my_list[i]*my_list[-i - 1])
print(f"{my_list} => {my_list2}")