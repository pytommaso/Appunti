# decorator:   (TOP)
# tack on extra functionality to a function


def new_decorator(func):

    def wrap_func():
        print('Code BEFORE')

        func()

        print('Code AFTER')

    return wrap_func


@new_decorator              # this is the switch
def func_1():
    print("This is the FUNC_1")


# @new_decorator
def func_2():
    print("This is the FUNC_2")


func_1()
func_2()
