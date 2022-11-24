#Solicitar al usuario que ingrese una direccion  de email. imprimir un mensaje diciendo
#si la direccion es valida o no, valiendose de una funcion para decidirlo.
#una direccion se considera valida si tiene @
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def verificacion(email):  #funcion para verificar email
  if (re.fullmatch(regex, email)):
    print("El email es valido3")

  else:
    print("l email es valido")


def validacion(correo):
  if "@" in correo:
    print("El email es valido1.")


def valido(correo):
  for i in correo:
    if i == "@":
      print("El email es valido2.")


em = input("Ingrese Email: ")

validacion(em)
valido(em)
verificacion(em)
