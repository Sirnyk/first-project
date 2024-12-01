
def ask_password(correct_password):
    tr = 3
    password = ''
    while tr > 0:
        password = input()
        if password == correct_password:
            print('Пароль принят')
            tr -= 3
        else:
            print('попробуйте еще раз')
            tr -= 1
    if password != correct_password:
        print('В доступе отказано')

ask_password('password123')