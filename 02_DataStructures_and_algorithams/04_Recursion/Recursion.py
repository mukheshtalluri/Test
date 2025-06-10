# Recursion : Recursion is the process calling function itself with small modification in the input until base condition is satisfied.

def first_method():
    second_method()
    print('This is the first method')


def second_method():
    third_method()
    print('This is the second method')


def third_method():
    forth_method()
    print('This is the third method')


def forth_method():
    print('This is the forth method')

first_method()

# Recursion with real world use problems
def fibonacci_sequence(num):
    if num in [0, 1]:
        return num
    return fibonacci_sequence(num - 2) + fibonacci_sequence(num - 1)

print(fibonacci_sequence(6))