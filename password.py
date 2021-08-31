def f(x):
    return any(y.isdigit() for y in x)


def g(d):
    return any(i.isupper() for i in d)


while True:
    password = input('Enter your password: ')
    if len(password) >= 8 and f(password) and g(password):
        print('Secure password!')
        exit()
    else:
        retry = ''
        while len(retry) < 8 or not f(retry) or not g(retry):
            retry = input('\nTry Again! You need at least 8 characters, a capital letter and a number in your '
                          'password.\nEnter your Password: ')
        print('Secured password!')
        exit()