# 📍 Программа, которая находит сумму элементов списка из нескольких чисел, 
# стоящих на нечётной позиции.

my_list = [2, 3, 5, 9, 3]
sum_of_list = 0
for i in range(1, len(my_list), 2):
        sum_of_list += my_list[i]
print(my_list)
print(f"Сумма элементов на нечётных позициях: {sum_of_list}")