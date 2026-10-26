def program(func):
    def function():
        print("start the progran")
        func()
        print("end the session")
    return function
@program
def greet():
    print("hello boss")
greet()