# decorator: functions that recieve function and return function

#Example 1:

def custom_decorator(function):
    def styling(*args):
        print('-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-')
        function(*args)
        print('-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-')
    return styling

@custom_decorator
def printing(name:str):
    print(name)

printing('Example 1, Testing ...')

#Example 2:

@custom_decorator
def printing():
    print('Example 2, Testing...')

printing()