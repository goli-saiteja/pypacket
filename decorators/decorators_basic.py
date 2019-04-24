# Decorators are used when we want our function to perform some special operations before and after
# A Decorator must always return a function


def null_decorator(fun):
    print('Before function called')
    return fun


def greet(msg):
    print(msg)


greet = null_decorator(greet)

greet('hello')

# The above functionality can be overcome by small syntactic sugar called as decorators


def null_decorator(fun):
    print('Before function called')
    return fun


@null_decorator
def greet(msg):
    print(msg)


greet('hello')
