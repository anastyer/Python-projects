import random

digit = '1234567890'
low_letters = 'qwertyuiopasdfghjklzxcvbnm'
up_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
signs = '#$%^&*_+=?-@!'

chars = ''

n = int(input('������� ������� ����� �������������? '))
length = int(input('������� ����� ������: '))
need_digit = input('����� �� �����? (�� ��� ���) ')
need_low = input('����� �� ��������� �����? (�� ��� ���) ')
need_up = input('����� �� �������� �����? (�� ��� ���) ')
need_sign = input('����� �� �����, ����� ��� #$%^&*_+=?-@!? (�� ��� ���) ')
delete_symbol = input('��������� ������� il1Lo0O? (�� ��� ���) ')

if need_digit.lower() == '��':
    chars += digit
if need_low.lower() == '��':
    chars += low_letters
if need_up.lower() == '��':
    chars += up_letters
if need_sign.lower() == '��':
    chars += signs
if delete_symbol.lower() == '��':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def password_generate(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    print(password)

for _ in range(n):
    password_generate(length, chars)