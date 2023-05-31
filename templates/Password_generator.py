import random
num = input('login ')
pas = ''
for x in range(8): #Количество символов (8)
    pas = pas + random.choice(list('12356789abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) #Символы, из которых будет составлен пароль
print('Hello, ', num, 'your password is: ', pas)