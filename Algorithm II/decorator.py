def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
        func()
    return wrapper

@my_decorator
def say_hello():
    print("hello!")

say_hello()