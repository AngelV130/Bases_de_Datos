# set_pythonpath.py
import sys
import os
# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

# Ignorar advertencias
import warnings
warnings.filterwarnings('ignore')


import consultas.consulta_1.Ganancias_Autor as Ganancias_Autor


def main():
    Ganancias_Autor.main()
    return

if __name__ == "__main__":
    main()