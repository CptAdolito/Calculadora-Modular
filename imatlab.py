
import os
import modular
import re
from threading import Thread

def process_command(line):
    #Commands come in a string command(number(s))
    #We need to split the command and the number(s) to process them
    """line = line.split("(")
    command = line[0]
    numbers = line[1][:-1]
    numbers = numbers.split(",")
    numbers = [int(n) for n in numbers]"""
    search = re.search(r"(\w+)\((.*)\)", line)
    command = search.group(1)
    numbers = search.group(2)
    numbers = numbers.split(",")
    try:
        numbers = [int(n) for n in numbers]
    except:
        numbers = [n[1:-1].split(";") for n in numbers]
        numbers = [[int(n) for n in num] for num in numbers]
        numbers2 = []
        for i in range(len(numbers[0])):
            numbers2.append([numbers[j][i] for j in range(len(numbers))])
        numbers = numbers2
        
    if command == "primo":
        result = modular.es_primo(numbers[0])
    elif command == "primos":
        result = modular.lista_primos(numbers[0], numbers[1])
    elif command == "factorizar":
        result = modular.factorizar(numbers[0])
    elif command == "mcd":
        if len(numbers) == 2:
            result = modular.mcd(numbers[0], numbers[1])
        else:
            result = modular.mcd_n(numbers)
    elif command == "coprimos":
        result = modular.coprimos(numbers[0], numbers[1])
    elif command == "pow":
        result = modular.potencia_mod_p(numbers[0], numbers[1], numbers[2])
    elif command == "inv":
        result = modular.inversa_mod_p(numbers[0], numbers[1])
    elif command == "euler":
        result = modular.euler(numbers[0])
    elif command == "legendre":
        result = modular.legendre(numbers[0], numbers[1])
    elif command == "resolverSistema":
        result = modular.resolver_sistema_congruencias(numbers[0], numbers[1], numbers[2])
    elif command == "raiz":
        result = modular.raiz_mod_p(numbers[0], numbers[1])
    elif command == "ecCuadratica":
        result = modular.ecuacion_cuadratica(numbers[0], numbers[1], numbers[2], numbers[3])
    elif command == "cipolla":
        result = modular.cipolla(numbers[0], numbers[1])
    else:
        return "NOP"
    
    if type(result) == bool:
        if result == False:
            return "No"
        else:
            return "Sí"
    
    if command == "resolverSistema":
        return str(f"{result[0]} (mod {result[1]})")

    if type(result) == list or type(result) == tuple or type(result) == set or type(result) == dict:
        return str(result)[1:-1]
    
    return result

def run_commands(fin, fout):
    for line in fin:
        fout.write(str(process_command(line.strip())) + "\n")


    

def get_file_name():
    ok = False
    while not ok:
        filename = input("Ingrese el nombre del archivo: ").strip()
        if os.path.isfile(filename):
            ok = True
        else:
            print("Archivo no encontrado\n")
    return filename

if __name__ == "__main__":
    ok = False
    while not ok:
        entrada = input("Desea 1. Leer de un archivo o 2. Ingresar por consola? ")
        if entrada.strip() == "1":
            mode = "archivo"
            ok = True
        elif entrada.strip() == "2":
            mode = "consola"
            ok = True
        else:
            print("Opcion no valida")
    
    if mode == "archivo":
        in_file = get_file_name()
        out_file = get_file_name()
        with open(in_file,"r") as fin:
            with open(out_file,"w",encoding="utf-8") as fout:
                run_commands(fin,fout)

    elif mode == "consola":
        comando = input("Ingrese el comando (exit para salir):\n").strip()
        while comando != "exit":
            print(process_command(comando))
            comando = input("Ingrese el comando (exit para salir):\n").strip()
