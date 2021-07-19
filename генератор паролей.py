import random

digit = '1234567890'
low_letters = 'qwertyuiopasdfghjklzxcvbnm'
up_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
signs = '#$%^&*_+=?-@!'

chars = ''

n = int(input('Сколько паролей нужно сгенерировать? '))
length = int(input('Введите длину пароля: '))
need_digit = input('Нужны ли цифры? (да или нет) ')
need_low = input('Нужны ли прописные буквы? (да или нет) ')
need_up = input('Нужны ли строчные буквы? (да или нет) ')
need_sign = input('Нужны ли знаки, такие как #$%^&*_+=?-@!? (да или нет) ')
delete_symbol = input('Исключить символы il1Lo0O? (да или нет) ')

if need_digit.lower() == 'да':
    chars += digit
if need_low.lower() == 'да':
    chars += low_letters
if need_up.lower() == 'да':
    chars += up_letters
if need_sign.lower() == 'да':
    chars += signs
if delete_symbol.lower() == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def password_generate(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    print(password)

for _ in range(n):
    password_generate(length, chars)