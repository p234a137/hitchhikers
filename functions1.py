
# https://realpython.com/blog/python/primer-on-python-decorators/
# functions


def foo(bar):
        return bar + 1


print (foo(2) == 3)


# first class objects
print(foo)
print(foo(2))
print(type(foo))


def call_foo_with_arg(foo, arg):
    return foo(arg)


print(call_foo_with_arg(foo, 3))


# Nested functions
def parent():
    print("Printing from parent() function.")

    def first_child():
        return "Printing from first_child() function."

    def second_child():
        return "Printing from second_child() function."

    print(first_child())
    print(second_child())


parent()
# cannot call first_child() directly because of the scope
# first_child()


# Returning functions
def parent2(num):

    def first_child():
        return "Printing from first_child() function."

    def second_child():
        return "Printing from second_child() function."

    try:
        assert num == 10
        return first_child
    except AssertionError:
        return second_child


foo = parent2(10)
bar = parent2(11)

print(foo)
print(bar)

print(foo())
print(bar())
