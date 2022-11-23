"""
imatlab_benchmark.py

Matemática Discreta - IMAT
ICAI, Universidad Pontificia Comillas

Descripción:
Script para la medición de tiempos de ejecución del programa IMAT-LAB.

Instrucciones de uso:
Modificar las listas de ficheros de entrada y de salida para utilizar distintos
benchmarks.

El bucle principal contiene código para ejecutar una medición de tiempos (benchmarking)
y/o hacer un perfilado (profiling) del código usando cada uno de los ficheros proporcionados.
Coméntese alguna de estas líneas si no se desea hacer el benchmarking o el profiling.
"""

import timeit
import cProfile
import imatlab

#Número de repeticiones de la toma de tiempos.
#Aumentarlo disminuye efectos aleatorios o casuales en el código, pero aumenta el coste de ejecución.
NITERS=1

def testRun(in_file:str, out_file:str):
    """ Wrapper para timeit y profile que abre los ficheros proporcionados
    y ejecuta sus comandos usando el módulo imatlab.
    
    Args:
        in_file: Nombre del fichero de entrada.
        out_file: Nombre del fichero de salida.
    
    Returns: Void
    Raises:
        IOError: Alguno de los ficheros no existe.
    """
    with open(in_file,"r") as fin:
        with open(out_file,"w",encoding="utf-8") as fout:
            imatlab.run_commands(fin,fout)

def measureTime(in_file:str,out_file:str)->float:
    """ Mide el tiempo medio de ejecución de  imatlab leyendo la entrada desde el fichero
    in_file y guardando la salida en el fichero out_file.

    Args:
        in_file: Nombre del fichero de entrada.
        out_file: Nombre del fichero de salida.
    
    Returns:
        float: Tiempo de ejecución medio medido
    Raises:
        IOError: Alguno de los ficheros no existe.
    """
    t=timeit.Timer("testRun('"+in_file+"','"+out_file+"')","from __main__ import testRun")
    return(t.timeit(number=NITERS)/NITERS)

def profile(in_file,out_file):
    """ Imprime en pantalla un profile de la ejecución de imatlab sobre la entrada leida
    desde el fichero in_file y guardando la salida en el fichero out_file.

    Args:
        in_file: Nombre del fichero de entrada.
        out_file: Nombre del fichero de salida.
    
    Returns: Void
    Raises:
        IOError: Alguno de los ficheros no existe.
    """
    cProfile.run("testRun('"+in_file+"','"+out_file+"')")



if __name__ == "__main__":
    #Inicar el listado de ficheros de entrada y de salida para procesar
    #Comentar, añadir o eliminar ficheros según sea necesario.
    #in_files=["primosTest.txt","factorTest.txt","mcdTest.txt","potenciaTest.txt",
    #            "invTest.txt","eulerTest.txt","sistemaTest.txt","cuadraticaTest.txt"]
    #out_files=["primosTest_out.txt","factorTest_out.txt","mcdTest_out.txt","potenciaTest_out.txt",
    #            "invTest_out.txt","eulerTest_out.txt","sistemaTest_out.txt","cuadraticaTest_out.txt"]
    #in_files=["eulerTest2.txt"]
    #out_files=["eulerSalida.txt"]
    in_files=["primosTest.txt","factorTest.txt","mcdTest.txt","potenciaTest.txt",
                "invTest.txt","sistemaTest.txt","cuadraticaTest.txt"]
    out_files=["primosTest_out.txt","factorTest_out.txt","mcdTest_out.txt","potenciaTest_out.txt",
                "invTest_out.txt","sistemaTest_out.txt","cuadraticaTest_out.txt"]

    runtime=[]
    for i in range(0,len(in_files)):
        #Comentar una línea o la otra para alternar benchmarking/profiling
        try:
            runtime.append(measureTime(in_files[i],out_files[i]))
            profile(in_files[i],out_files[i])
            print("Tiempo de ejecución de "+in_files[i]+": "+str(runtime[i]))
        except IOError:
            runtime.append(0)
            print("El fichero "+in_files[i]+" no existe.\n")

    print(runtime)