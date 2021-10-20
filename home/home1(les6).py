import random
list1 = random.sample(range(1, 100), 10) #генерирует числа от 1 до 100, всего этих чисел 20
print(list1)
list2 = []
for el in range(len(list1) - 1):
    if list1[el] < list1[el+1]:
        list2.append(list1[el+1])
print(list2)

