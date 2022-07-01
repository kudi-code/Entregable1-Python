"""
Instrucciones NOTA: Pueden encontrar los archivos en este replit https://replit.com/team/gen-11-py/Final-OOP

Un grupo de estudiantes ha participado en un bootcamp de programacion, en el modulo de python han visto diferentes temas desde tipos de datos hasta objetos, en algunas clases estos estudiantes participan en un quiz con el fin de medir lo que han aprendido a lo largo del modulo, el profesor menciona que el primer lugare podra adquirir el libro de su eleccion, cada quiz genera un csv con informacion del puntaje obtenido por el estudiante.

Los campos de ese csv son los siguientes:

Rank: Posición del estudiante en el quiz First Name: Nombre Last Name: Apellido Attempt: Numero de respuestas Accuracy: Porcentaje de acierto Score: Cantidad total de puntos

Resaltar que los siguientes estudiantes han recibido puntos extra

    Kevin Salvador --> 8000
    Diego Angeles --> 2000

Tareas Aunque el instructor ha insistido a los estudiantes que al momento de realizar el quiz coloquen siempre el mismo nombre, algunos de ellos han hecho caso omiso a esa instrucción: Por lo cual deberas procesar los mismos para que en todos los quizes aparezcan los mismos usuarios. Deberas crear una clase para las siguientes funcionalidades: Abrir Archivos Procesar Archivos Encontrar Ganadores (Los dos primeros: Puntos extra si permiten que la cantidad de ganadores sea dinamica) ganador con su puntaje. ( SE CONSIDERA GANADORE A LAS PERSONA QUE TENGAN EL MAYOR PUNTAJE AL SUMAR EL PUNTAJE DE TODOS LOS QUIZES Y PUNTOS EXTRAS ) Encontrar Usuarios que tengan un porcentaje de acierto mayor a 70 % (Puntos extra si el porcentaje es dinamico) por cada quiz Cualquier clase extra que consideres necesaria para resolver el ejercicio. El objetivo final es encontrar las dos personas que hasta el día de hoy van a la delantera

Calificacion Programacion orientada a objetos: 60 % Funciones: 10 % Try Except: 5 % Documentacion (Ya sea docstring, tipado o incluso un readme explicando la funcionalidad del programa): 10 % Ciclos (for o while): 10% Imports / Modulos: 5 % Por cada item anterior se te asignara un puntaje, se considera que el ejercicio es aprobado cuando la suma de ese puntaje sea mayor a 60

Metodo de entrega Cuando consideren que el ejercicio esta completo marcar el boton submit. Enviar link al replit. (Cada persona del grupo debe hacer un envio)

Fecha limite de entrega viernes 6 de mayo 6pm

Si el ejercicio es enviado despues de la fecha limite sera calificado como No Aprobado
"""

import csv
from encodings import utf_8
from mimetypes import init

class ProcessData:
    def __init__(self, name) -> None:
        self.name = name
    #1. Open Files
    def open_file(self):
        self.data = []
        with open(self.name, encoding="UTF_8") as csv_file:    
            file_to_process = csv.DictReader(csv_file)
            for i in file_to_process:
                self.data.append({"rank" : i["Rank"], "Name" : i["First Name"] + " " + i["Last Name"],"Accuracy" : i["Accuracy"],"Score" : i["Score"]})
        return self.data
    #2. Process Data: Sort
    
    def process_data(self):
        def myFunc(e):
            return e['Name']
        self.data.sort(key=myFunc)
        return self.data

class ProcessAllData:
    def __init__(self, *args:list ) -> None:
        for data in args:
            print("---------------")
            for students in data: 
                print(students)
    def add_names(self ):
        pass

quiz_1 = ProcessData("quiz_1.csv")
data1 = quiz_1.open_file()
data1_sorted = quiz_1.process_data()
# print(data1_sorted)

quiz_2 = ProcessData("quiz_2.csv")
data2 = quiz_2.open_file()
data2_sorted = quiz_2.process_data()

all_data = ProcessAllData(data1_sorted, data1_sorted)


# print(data2)


quiz_3 = ProcessData("quiz_3.csv")
data3 = quiz_3.open_file()

quiz_4 = ProcessData("quiz_4.csv")
data4 = quiz_4.open_file()





