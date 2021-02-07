from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets          
from .serializers import HeladoSerializer, MateriaPrima_HeladoSerializer, MateriaPrimaSerializer     
from .models import Helado, MateriaPrima, MateriaPrima_Helado
import json
from .calculos import calcular_precios_helado, calcular_precios_materia,datos_helados,datos_materiaprima_helado,datos_materias, mapaea_materias, crear_modelo, encuentra_no_validos, datos_heladomaquina, nombre_maquinas, datos_packing, crear_modelo_packing, resumir_packing, nombre_helados_id
from .calculos_or import minimizacion_costos, maximizacion_ganancias, maximizacion_produccion, Scheduling, Packing


def index(request):
    return render(request, 'optimizacion/index.html')

def optimizacion(request):
    return render(request, 'optimizacion/optimizacion.html')

def calculos_helado(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        #print(body)
        resultado = calcular_precios_helado(body)
        #print(resultado)
        #id_helados,cantidades, precios, demandas = datos_helados(body)
        #cant_mph = datos_materiaprima_helado(id_helados)
        #print("id helados son: %s \n cantidades son %s \n precios son %s \n demandas son %s \n cant materia prima por helado es %s"  %(str(id_helados),str(cantidades), str(precios), str(demandas), str(cant_mph)))
        return JsonResponse(resultado)

def calculos_materia(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        #print(body)
        resultado = calcular_precios_materia(body)
        #print(resultado)
        #id_materias, disponibilidad, costos = datos_materias(body)
        #print("id materias son: %s \n disponibilidades son %s \n costos son %s "  %(str(id_materias),str(disponibilidad), str(costos)))

        return JsonResponse(resultado)

def calculos(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        helados = body["helados"]
        id_helados,cantidades, precios, demandas, nombres_helados = datos_helados(helados)
        cant_helados = len(id_helados)
        cant_mph = datos_materiaprima_helado(id_helados)
        print("ACA id helados son: %s \n cantidades son %s \n precios son %s \n demandas son %s \n cant materia prima por helado es %s"  %(str(id_helados),str(cantidades), str(precios), str(demandas), str(cant_mph)))

        materias = body["materias"]
        id_materias, disponibilidad, costos = datos_materias(materias)
        print(" ACA id materias son: %s \n disponibilidades son %s \n costos son %s "  %(str(id_materias),str(disponibilidad), str(costos)))

        arreglo_mat_helado = mapaea_materias(id_materias,cant_helados,cant_mph)
        print("arreglo es %s" %arreglo_mat_helado)

        #Elimino los que no son posibles crear ya que no se seleccionaron todas sus materias primas como disponibles.
        no_validos, id_no_validos = encuentra_no_validos(id_materias,cant_mph, id_helados)
        print(" no validos es %s" %no_validos)
        #Elimino los indices
        for i in range(0,len(no_validos)):
            print(" i es %s" %i)
            print("no_validos[%s] es %s" %(i,no_validos[i]))
            print("precios son %s demandas son %s y arreglo mat helado son %s" %(precios,demandas,arreglo_mat_helado))
            del precios[no_validos[i]]
            del nombres_helados[no_validos[i]]
            del demandas[no_validos[i]]
            for j in range(0, len(id_materias)):
                del arreglo_mat_helado[j][no_validos[i]]
            for j in range(i+1, len(no_validos)):
                no_validos[j]=no_validos[j] -1
            print("precios son %s demandas son %s y arreglo mat helado son %s" %(precios,demandas,arreglo_mat_helado))
            print(" no validos es %s" %no_validos)
            print("no_validos[%s] es %s" %(i,no_validos[i]))

        respuesta = {}
        if(len(demandas) == 0):
            respuesta["resultado"] = "fracaso"
            respuesta["razon_fracaso"] = "materia_insuficiente"
        else:
            respuesta["resultado"] = "exito"
            respuesta["no producidos"] = []
            for idh in id_no_validos:
                print("No es posible producir %s " %Helado.objects.get(pk=idh).nombre)
                respuesta["no_producidos"].append(Helado.objects.get(pk=idh).nombre)

            data = crear_modelo(precios,demandas, arreglo_mat_helado, disponibilidad,costos, nombres_helados)

            if body["objetivo"] == "maximizarganancias":
                print("maximizacion ganancias")
                respuesta["optimizacion"] = maximizacion_ganancias(data)
            elif body["objetivo"] == "maximizarproduccion":
                print("maximizacion produccion")
                respuesta["optimizacion"] =maximizacion_produccion(data)
            elif body["objetivo"] == "minimizarcostos":
                print("minimizacion costos")
                respuesta["optimizacion"] =minimizacion_costos(data)
            else:
                respuesta["resultado"] = "fracaso"
                respuesta["razon_fracaso"] = "opcion_no_disponible"
            
        print("\n\n\n RESPUESTA \n", respuesta)
        return JsonResponse(respuesta)

def scheduling(request):
    if request.method == 'POST':
        print("HOLAAAAAAAAAAAAA")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print("BODY ES", body)
        helados_id = list(map(int, body['helados'])) 
        print("HELADOS ID ES %s" %helados_id)
        nombres_helado = nombre_helados_id(helados_id)
        nombre_maq = nombre_maquinas()
        jobs = datos_heladomaquina(helados_id)
        print("nombre maquina %s" %nombre_maq)
        respuesta = Scheduling(jobs,nombre_maq, nombres_helado)
        return JsonResponse(respuesta)

def packing(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        #Convertimos de lista de strings a lista de enteros
        cantidades = list(map(int, body["cantidades"]))
        capacidades = list(map(int, body["capacidades"]))
        helados = list(map(int, body["helados"]))
        tamanos = list(map(int, body["tamanos"]))
        values, weights, nombres_helados = datos_packing(helados,tamanos,cantidades)
        print(body)
        data = crear_modelo_packing(weights, values, capacidades, nombres_helados)
        respuesta = Packing(data)
        print(resumir_packing(respuesta))
        resumido = resumir_packing(respuesta)
        return JsonResponse(resumido)




class HeladoView(viewsets.ModelViewSet):
    serializer_class = HeladoSerializer
    queryset = Helado.objects.all()

class MateriaPrimaView(viewsets.ModelViewSet):
    serializer_class = MateriaPrimaSerializer
    queryset = MateriaPrima.objects.all()

class MateriaPrima_HeladoView(viewsets.ModelViewSet):
    serializer_class = MateriaPrima_HeladoSerializer
    queryset = MateriaPrima_Helado.objects.all()