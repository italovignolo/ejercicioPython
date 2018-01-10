#coding=utf-8
class Persona:
    #Ejecutar archivo python =execfile("nombre.py")
    nombre = "Karl"
    #def __init__(self):
        #print "Hola Mundo POO Python "+self.nombre

    def __init__(self):
        print "hola beibi"

    def suma_de_dos_numeros(self, numero1, numero2):
        return numero1 + numero2

    def mostrar_diez_numeros(self):
        i = 1 #declaro variable
        while i<=10: #Ciclo While
            print i
            i += 1

    def mi_primer_arreglo(self):
        lista = [] #Declaración de un arreglo
        lista.append(123) #add
        lista.append("hola a todos")
        return lista

    def mostrar_lista(self, lista_input):
        #foreach
        for elemento in lista_input:
            print elemento

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False


#class Profesor(Persona): #Clase Profesor hereda de Persona

    #def saludo_profe(self):
        #print "Hola soy el profe "+self.nombre

objeto = Persona()
#print objeto.suma_de_dos_numeros(3,5)
#objeto.mostrar_diez_numeros()
#print objeto.mi_primer_arreglo()
#lista = [154, "Nuevo texto", "+56998766332", 0.34, True, False]
#objeto.mostrar_lista(lista)
#numero = 18

#if objeto.es_par(numero):
    #print "Es par"
#else:
    #print "No es par"

#objeto_profesor = Profesor()
#objeto_profesor.saludo_profe()

#Trabajo: Investigar como instalar librería MySQL en Python
