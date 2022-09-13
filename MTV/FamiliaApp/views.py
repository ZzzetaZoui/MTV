from django.shortcuts import render
from FamiliaApp.models import DatosFamilia
from django.http import HttpResponse
from django.template import loader

def DatosDeFamilias(self):
    Datos1=DatosFamilia(nombre="Ana Paula", apellido="Onanty", dni=38456982, genero="Femenino", profesion="Doctora", correo="anapaula@gmail.com")
    Datos1.save()
    Datos2=DatosFamilia(nombre="Juan Marcos", apellido="Onanty", dni=45698754, genero="Masculino", profesion="Ingeniero Civil", correo="juanma10@gmail.com")
    Datos2.save()
    Datos3=DatosFamilia(nombre="Melissa", apellido="Alonso", dni=43561857, genero="Femenino", profesion="Astronauta", correo="alonsomeli1@gmail.com")
    Datos3.save()
    diccionario = {
        "nombre1":Datos1.nombre, "apellido1":Datos1.apellido, "dni1":Datos1.dni, "genero1":Datos1.genero, "profesion1":Datos1.profesion, "correo1":Datos1.correo,
        "nombre2":Datos2.nombre, "apellido2":Datos2.apellido, "dni2":Datos2.dni, "genero2":Datos2.genero, "profesion2":Datos2.profesion, "correo2":Datos2.correo,
        "nombre3":Datos3.nombre, "apellido3":Datos3.apellido, "dni3":Datos3.dni, "genero3":Datos3.genero, "profesion3":Datos3.profesion, "correo3":Datos3.correo   
    }

        
    plantilla=loader.get_template("plantilla.html")
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)