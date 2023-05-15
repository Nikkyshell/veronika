def calculator(type_operation):
    def sum():
        c = a + b
        print(c)
    def subtract():
        c = a - b
        print(c)
    def mult():
        c = a * b
        print(c)
    def divide():
        c = a/b
        print(c)
    if type_operation == "+":
        sum()
    elif type_operation == "-":
        subtract()
    elif type_operation == "*":
        mult()
    elif type_operation == '/':
        divide()
    else:
        print('ошибка, вы ввели не тот знак')
a = float(input("введите первое число: "))
b = float(input("введите второе число: "))
type_operation = input("введите знак: ")
calculator(type_operation)
