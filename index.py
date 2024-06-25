# set_pythonpath.py
import sys
import os
# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

# Ignorar advertencias
import warnings
warnings.filterwarnings('ignore')


import consultas.consulta_1.Ganancias_Autor as Ganancias_Autor
import consultas.consulta_2.Ganasias_Author_Region as Ganasias_Author_Region


def main():
    # Ganancias_Autor.main()
    Ganasias_Author_Region.main()
    return

if __name__ == "__main__":
    main()