from typing import Any, Callable
from functools import wraps

def log(filename:Any):
    """ Логирует вызов функции и ее результат в файл или в консоль"""
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(result)
            if result == sum(args):
                # filename.write("my_function ok")
                print("my_function ok")
            else:
                raise ValueError
                error = "ValueError"
                print(f"my_function error: {error}. Inputs:{args}, {kwargs}")
                #filename.write(f"my_function error: {error}. Inputs:{args}, {kwargs}")
            return result

        return wrapper
    return decorator

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(2, 8)
