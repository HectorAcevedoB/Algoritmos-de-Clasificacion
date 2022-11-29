import math
import random
from urllib import request
from django.shortcuts import render
from .models import Datos

# Create your views here.
def muestra_datos(request):
    consulta= Datos.objects.all()
    listaSuma=calculaSuma(consulta)
    contexto= zip(consulta,listaSuma)
    return render(request, 'daddy/web.html', {'contexto':contexto})
    


def calculaSuma(l):
        listaSuma=[]
        for i in l:
            r=i.x1 + i.x3 + i.x4
            listaSuma.append(r)
        return listaSuma

#DISTANCIAEUCLIDIANA

def algKNN(request): 
    x1 = random.randint(1,500)
    x2 = random.randint(1,500)
    x3 = random.randint(1,500)
    df = Datos.objects.all()
    ldis = distanciaEu(df,x1,x2,x3)
    ldis = sorted(ldis)
    contexto = zip(df,ldis)
    return render(request, 'daddy/algoritmo1.html', {'contexto':contexto})

def distanciaEu(df,x1,x2,x3):
    ldist = []
    for i in df:
        dis = (x1 - i.x1)**2+(x2 - i.x3)**2+(x3 - i.x4)**2
        raiz = round(math.sqrt(dis),4)
        ldist.append(raiz)
    return ldist


#BAYESIANO

def algBaye(request): 
    x1 = random.randint(1,500)
    x2 = random.randint(1,500)
    x3 = random.randint(1,500)
    df = Datos.objects.all()
    ldis = ABaye(df,x1,x2,x3)
    ldis = sorted(ldis)
    contexto = zip(df,ldis)
    return render(request, 'daddy/algoritmoBaye.html', {'contexto':contexto})

def ABaye(df,x1,x2,x3):
    ldist = []
    for i in df:
        dis = (x1 - i.x1)**2+(x2 - i.x3)**2+(x3 - i.x4)**2
        div = (dis / 27-1)
        ldist.append(div)
    return ldist

#RLineal
def RLineal(request):
    x1 = random.randint(1,500)
    x2 = random.randint(1,500)
    x3 = random.randint(1,500)
    df = Datos.objects.all()
    ldis = Alineal(df,x1,x2,x3)
    ldis = sorted(ldis)
    contexto = zip(df,ldis)
    return render(request, 'daddy/RALineal.html', {'contexto':contexto})

def Alineal(df,x1,x2,x3):
    ldist = []
    for i in df:
        sumx1 = i.x1 + i.x1
        sumx2 = i.x3 + i.x3
        Tsum= sumx1 + sumx2
        Dsum= Tsum / 200
        a=(Dsum)**2
        y = i.x4 + i.x4
        Divy = y / 100
        vi = 200 
        b=(Divy-a)*200
        ldist.append(a)
    return ldist


