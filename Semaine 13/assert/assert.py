# assert expression, message

def add(a, b):
    assert isinstance(a, int) and isinstance(b, int), "A et/ou B doit etre un nombre entier"
    return a + b

print(add(2, "3"))  # Cela va lever une AssertionError

