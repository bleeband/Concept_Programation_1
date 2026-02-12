name = "mon_module"

class MyCustomTypeError(Exception):
    def __init__(self, message):
        self.message = message

def my_split(string, char=" "):
    if not isinstance(string, str):
        raise MyCustomTypeError("Vous n'avez pas fourni une string")

    res = []
    current_string = []
    for c in string:
        if c != char:
            current_string.append(c)
        else:
            res.append("".join(current_string))
            current_string = []

    res.append("".join(current_string))
    return res

def presentation():
    print(f"Je suis {name} à votre service")
