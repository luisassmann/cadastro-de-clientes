import os
import sys


def run():
    """Checa os requisitos e roda o programa."""
    try:
        os.system("python3 -m pip install -r requirements.txt")
        os.system("sudo apt install python3-tk")
        os.system("python3 project/main.py")
    except OSError as error:
        print(error)


if sys.platform.startswith('linux'):
    try:
        os.mkdir("./bin/")
        os.walk("..")
        open("./bin/cliente.pdf", "w+")
        open("./bin/clientes.db", "w+")
        run()
    except OSError as error:
        if type(error) == FileExistsError:
            run()
        else:
            print(error)
else:
    print("Sem suporte por enquanto.")
