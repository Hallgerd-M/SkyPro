from typing import Any, Callable
from functools import wraps

def log(filename):
    """ Логирует вызов функции и ее результат в файл или в консоль"""
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == sum(args):
                # filename.write("my_function ok")
                print("my_function ok")
            else:
                raise ValueError('Сообщение об ошибке')
                # filename.write(f"my_function error: {error}. Inputs:{args}, {kwargs}")
                print (f"my_function error: {error}. Inputs:{args}, {kwargs}")
            return result
        return wrapper
    return decorator

def predicates_are_int(x, y):
    return type(x, y) == int

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

#@log(predicates_are_int, error_message="Error")
#def my_function(x, y):
#    return x + y

#if __name__ == "___main__":
#    print(my_function(2, "6"))

