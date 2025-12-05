a = 1
b = 2

def foo():
    print(f"je suis le a de foo {a}")
    print(f"je suis le b de foo {b}")

def fun():
    b = 4
    print(f"je suis le b de fun {b}")
    foo()

fun()
