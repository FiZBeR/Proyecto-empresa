from django.shortcuts import render
from email import message
from re import template
from wsgiref.util import request_uri
from xml.dom.expatbuilder import DOCUMENT_NODE
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from ast import Delete
import json
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View

from .models import Administrador, Login, Operario, Perfil_Empresa, Transacciones

class EmpresasViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, User=0):
        if User > 0:
            pem = list(Perfil_Empresa.objects.filter(UserID=User).values())
            if len(pem) > 0:
                respuesta = pem[0]
                datos = {"Empresa": respuesta}
            else:
                datos = {"Respuesta": "No se encontrarton datos"}
        else:
            template_name = ".html"
            pem = Perfil_Empresa.objects.all()
            datos = {'listadoAdmon': pem}
        return render(request, template_name, datos)

    def post(self, request):

        Perfil_Empresa.objects.create(ID_Empresa=request.POST["ID_Empresa"], Nombre_Empresa=request.POST["Nombre_Empresa"], Email_Coorporativo=request.POST["Email_Coorporativo"],
                                     Telefono_Coorporativo=request.POST["Telefono_Coorporativo"])
        return redirect('//')

    def put(self, request, User):
        datos = json.loads(request.body)
        pem = list(Perfil_Empresa.objects.filter(UserID=User).values())
        if len(pem) > 0:
            NewEmpresa = Perfil_Empresa.objects.get(UserID=User)
            NewEmpresa.UseID_EmpresarID = datos['ID_Empresa']
            NewEmpresa.Nombre_Empresae = datos['Nombre_Empresa']
            NewEmpresa.Email_Coorporativo = datos['Email_Coorporativo']
            NewEmpresa.Telefono_Coorporativo = datos['Telefono_Coorporativo']
            NewEmpresa.save()
            mensaje = {"Respuesta": "Se actualizaron los datos correctamente"}
        else:
            mensaje = {"Respuesta": "No se encontraron datos"}
        return JsonResponse(mensaje)

    def delete(self, request, User):
        pem = list(Perfil_Empresa.objects.filter(UserID=User).values())
        if len(pem) > 0:
            Perfil_Empresa.objects.filter(UserID=User).delete
            mensaje = {"Respuesta": "El registro se elimino correctamente"}
        else:
            mensaje = {"Respuesta": "No se encontraron datos"}
        return JsonResponse(mensaje)
        
