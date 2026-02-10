""" __name__  est une variable spéciale en Python qui contient le nom du module actuel.
Lorsque vous exécutez un script Python, le nom du module est défini sur "__main__". 
Cela signifie que si vous exécutez un script directement, le code à l'intérieur de la condition `if __name__ == "__main__":` 
sera exécuté. Cependant, si vous importez ce script en tant que module dans un autre script, le code à l'intérieur 
de cette condition ne sera pas exécuté. """

# import tools.calc
import tools

# print("index est exécuté.")
# print(__name__)

# tools.calc.add(2, 3)
tools.add(2, 3)
tools.calc.multiply(4, 5)