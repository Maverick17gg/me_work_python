list1 = [2, 3, 3, 5, 6, 2, 1, 1, 7, 8]

list2 = []

def my_fun(a):
    for a in list1:
        if a not in list2:
            list2.append(a)
            yield a

for b in my_fun(list2):
    print(b)
