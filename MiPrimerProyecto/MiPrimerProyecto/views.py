from aifc import open
from email import contentmanager
from os import name

from django.http import HttpResponse

from django.template import Context, Template 

import datetime

def mi_primera_vista(request):
    
    pass

    return HttpResponse("Saludos desde django")


def segunda_vista(request):
    
    with open(r"C:\Users\Ignacio\OneDrive\Documentos\Curso Pyhton\Proyecto Django\MiPrimerProyecto\index.html") as f:
       plantilla = Template(f.read())
        
    contexto = Context()    
    
    documento = plantilla.render(contexto) 
    
    return HttpResponse(documento)


def tiempo(request):
    
    nombre = "Juan Carlo"
    hoy = datetime.datetime.now()
    
    html=f"""
    <html>
        <head></head>
            <body>
                <h1>El tiempo es: <h2>{hoy}</h2></h1>
                Saludos desde django en <b>coder</b> soy {nombre}
            </body> 
            
    </html>
    """
    return HttpResponse(html)

def nombre(requestname):
    nombre = name
    
    hoy = datetime.datetime.now()
    
    html=f"""
    <html>
        <head></head>
            <body>
                <h1>El tiempo es: <h2>{hoy}</h2></h1>
                Saludos desde django en <b>coder</b> soy {nombre}
            </body> 
            
    </html>
    """
    
    return HttpResponse(html)