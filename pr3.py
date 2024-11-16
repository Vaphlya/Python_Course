password = input('Введіть пароль: ')

if password == 'password123' :
    print('Ви увійшли в систему!')
else :
    print('Неправильний пароль')
    exit()

day_of_week = {'Monday':'1', 'Tuesday':'2', 'Wednesday':'3', 'Thursday':'4', "Friday":'5', 'Saturday':'6', 'Sunday':'7'}

choose_week = input('Вкажіть день неділі: ')

if choose_week == '0' or '8' :
    print('Помилка')

a = 5
for i in range(1,11) :
    print(a * i)


    num = [2,3,4,5,3,7]
    print(sum(num))


def factorial(n) :
    return n * factorial(n-1)

number = 8
print(f'Факторіал: {factorial(number)}')


for i in range(1,51) :
    if i % 2 == 0 :
        print(i)

chisla = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def is_Prime(n) :
    if n < 2 :
        return False
    for i  in range(2, int(n**0.5) + 1) :
        if n % i == 0 :
            return False
    return True

prime_num = [num for num in chisla if is_Prime(num)]
print(prime_num)
