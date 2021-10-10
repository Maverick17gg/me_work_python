user_input = str(input("Введите строку:"))
user_input = user_input.split(" ")
for i in user_input:
    print(f'{user_input.index(i) + 1}: {i[:10].center(10)}')