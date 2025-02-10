def another_decorator(func):
    def wrapper():
        print("Executing function...")
        func()
        print("Function execution finished.")
    return wrapper

@another_decorator
def greet():
    print("Greetings from the second script!")

greet()
