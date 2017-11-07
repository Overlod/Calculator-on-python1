def echo_1(*numbers):
    '''
    Used to run add function
    You can enter a large number of numbers
    '''
    return add(*numbers)

def echo_2(numbers):
    '''
    Used to run multiply function
    You can enter a large number of numbers
    '''
    return multiply(numbers)

def add(*numbers):
    '''
    Used to add the numbers
    Can add a large number of numbers
    '''
    return sum(numbers)

def multiply(numbers):
    '''
    Used to multiply the numbers
    Can multiply a large number of numbers
    '''
    mul = 1
    for i in numbers:
        mul = mul * i
    return mul

def subtract(x, y):
    '''
    Used to subtract one from the other
    Can subtract one number from the other (2 numbers)
    '''
    return x - y

def divide(x, y):
    '''
    Used to divide one from the other
    Can divide one number from the other (2 numbers)
    '''
    return x / y

def breaker(a):
    '''
    Used to stop program cycle
    '''
    p = 0
    while True:
        if a == 'Y':
            p += 1
            break
        elif a == 'N':
            p -= 1
            break
        else:
            print("Некорректный ввод, попробуйте снова!")
            continue
    return p

def print_answer(results):
    '''
    Used to print answer
    '''
    print("Ответ: " + results)


while True:
    print("Настройки:")
    print("Введите '+', чтобы прибавить два числа")
    print("Введите '-', чтобы вычесть из одного числа другое")
    print("Введите '*', чтобы умножить два числа")
    print("Введите '/', чтобы разделить одно число на другое")
    print("Введите '?', чтобы узнать дополнительную информацию")
    print("Введите 'quit', чтобы выйти из программы")
    user_input = input(': ')

    if user_input == 'quit':
        break
    elif user_input == '+':
        try:
            input_ = map(int, input("Введите числа, которые хотите сложить:").split())
            listok = list(input_)
            res = str(echo_1(*listok))
        except ValueError:
            print("Unknown input")
            continue
        print_answer(res)
        x = input("Хотите продолжить? Y/N: ")
        if breaker(x) > 0:
            continue
        elif breaker(x) < 0:
            break
    elif user_input == '-':
        try:
            num1_subtract = float(input("Введите первое число: "))
            num2_subtract = float(input("Введите второе число: "))
        except ValueError:
            print("Unknown input")
            continue
        result_subtract = str(subtract(num1_subtract, num2_subtract))
        print_answer(result_subtract)
        x = input("Хотите продолжить? Y/N: ")
        if breaker(x) > 0:
            continue
        elif breaker(x) < 0:
            break
    elif user_input == '*':
        try:
            input_2 = map(int, input("Введите числа для выполнения операции:").split())
            listok1 = list(input_2)
            res1 = str(echo_2(listok1))
        except ValueError:
            print("Unknown input")
            continue
        print_answer(res1)
        x = input("Хотите продолжить? Y/N: ")
        if breaker(x) > 0:
            continue
        elif breaker(x) < 0:
            break
    elif user_input == '/':
        try:
            num1_division = float(input("Введите первое число: "))
            num2_division = float(input("Введите второе число: "))
        except ValueError:
            print("Unknown input")
            continue
        try:
            result_divide = str(divide(num1_division, num2_division))
        except ZeroDivisionError:
            print("ZeroDivisionError")
            continue
        print_answer(result_divide)
        x = input("Хотите продолжить? Y/N: ")
        if breaker(x) > 0:
            continue
        elif breaker(x) < 0:
            break
    elif user_input == '?':
        try:
            question = input('''Введите название функции, описание которой хотите получить:
            \nПеречень функций:
            \n1) echo_1
            \n2) echo_2
            \n3) add
            \n4) multiply
            \n5) divide_
            \n6) subtract_
            \n7) breaker
            \n:''')
            if question == "echo_1":
                print(echo_1.__doc__)
            elif question == "echo_2":
                print(echo_2.__doc__)
            elif question == "add":
                print(add.__doc__)
            elif question == "multiply":
                print(multiply.__doc__)
            elif question == "divide":
                print(divide.__doc__)
            elif question == "subtract":
                print(subtract.__doc__)
            elif question == "breaker":
                print(breaker.__doc__)
            else:
                print("Unknown input")
                continue
            x = input("Хотите продолжить? Y/N: ")
            if breaker(x) > 0:
                continue
            elif breaker(x) < 0:
                break
        except ValueError:
            print("ValueError")
            continue
    else:
        print("Unknown input")
        continue
