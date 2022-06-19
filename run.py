import os
import sys


def run():
    if sys.platform.startswith('linux'):
        try:
            os.system("sudo apt install python3-tk -y")
            os.system("python3 -m pip install -r requirements.txt")
            os.system("python3 project/main.py")
        except OSError as error:
            print(error)

    elif sys.platform.startswith('win'):
        try:
            os.system("python -m pip install -r requirements.txt")
            os.system("python .\project\main.py")
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
    if sys.platform.startswith('win'):
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
