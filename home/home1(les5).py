def user(name, surname, birthe_year, city, email, phone_number):
    print(
        f'{name} {surname} {birthe_year} года Рождения, Проживающий в городе {city}\n'
        'Контактные данные:\n'
        f'- телефон:{phone_number}\n'
        f'- email: {email}'

    )

user('Ivan', 'Nikiporchik', '2001', 'DT', 'test@mail.ru', '454821454812812')