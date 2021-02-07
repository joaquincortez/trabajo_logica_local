from .models import Helado, MateriaPrima, MateriaPrima_Helado, MaquinaHelado, Maquina
import numpy as np


def producto(a,b):
    return a * b

def calcular_precios_helado(datos):
    lista = datos.items()
    resultado = {}
    total = 0
    print(lista)
    print(type(lista))
    for key, value in lista:
        helado = Helado.objects.get(id=key)
        precio = helado.precio * int(value)
        resultado[helado.nombre] = str(precio) #precio * cant
        total+= precio
    resultado["total"] = str(total)
    return resultado

def calcular_precios_materia(datos):
    lista = datos.items()
    resultado = {}
    total = 0
    print(lista)
    print(type(lista))
    for key, value in lista:
        materia_prima = MateriaPrima.objects.get(id=key)
        precio = materia_prima.costo * int(value)
        resultado[materia_prima.nombre] = str(precio) #precio * cant
        total+= precio
    resultado["total"] = str(total)
    return resultado

def datos_helados(datos):
    lista = list(datos.items())
    cantidades = list(datos.values())
    precios = []
    demandas = []
    nombres = []
    
    for key, value in lista:
        helado = Helado.objects.get(id=key)
        precios.append(float(helado.precio))
        demandas.append(value)
        nombres.append(helado.nombre)
    
    return list(datos.keys()),cantidades, precios, list(map(int, demandas)) , nombres


def datos_materias(datos):
    id_materias = list(datos.keys())
    costos = []
    for idm in id_materias:
        costos.append(float(MateriaPrima.objects.get(pk=idm).costo))
    return list(map(int, id_materias)), list(map(int, list(datos.values()))), costos

def datos_materiaprima_helado(helados_id):
    cantidades_mph = [] #mph: materia prima por helado
    
    for helado in helados_id:
        materias_helado = {}
        mphs = MateriaPrima_Helado.objects.all().filter(helado = helado)
        for m in mphs:
            materias_helado[m.materia_prima.id] = m.cantidad / 10 #Divimos cantiad en diez
        cantidades_mph.append(materias_helado)
    
    return cantidades_mph


def mapaea_materias(id_materias,cant_helados, reg_mat_hel):
    cant_materias = len(id_materias)
    arr_cant_mathelado = np.zeros((cant_materias, cant_helados), dtype=int)
    for i in range(0,cant_materias):
        print("\n\n\n MATERIA %s" %i)
        for j in range(0,cant_helados):
            print("\n HELADO %s" %j)
            mat_helados = list(reg_mat_hel[j].keys())
            cant_mat_helado = list(reg_mat_hel[j].values())
            print("ID MATERIAS ES %s" %id_materias)
            print("ID MATERIAS DEL HELADO ES ES %s" %mat_helados)
            print("CANT MATERIAS DEL HELADO ES ES %s" %cant_mat_helado)
            l=0
            while(l < len(mat_helados) and id_materias[i] != mat_helados[l]):
                l+=1
            if l != len(mat_helados):
                print("ARREGLO ANTES ESCRIBIR ES %s" %arr_cant_mathelado.tolist())
                print("SE ESCRIBIO ARREGLO[%s][%s] = %s" %(i,j,cant_mat_helado[l]))
                arr_cant_mathelado[i][j]= cant_mat_helado[l]
    
    return arr_cant_mathelado.tolist()

def crear_modelo(precio_helados, demanda_helados, mat_helado, disponibilidad_materias, costo_materias, nombre_helados):
    data={}
    data['constraint_coeffs']=mat_helado #Cant de MP usada para hacer el helado
    data['bounds']=disponibilidad_materias #MP disponible
    data['obj_coeffs']=precio_helados #Precio de helados
    data['num_vars']= len(precio_helados)#N° helados
    data['precio_base']=costo_materias #Dinero que cuesta cada MP por unidad
    data['num_constraints']=len(costo_materias) #N° de MP
    data['demanda']=demanda_helados
    data['nombre_helados'] = nombre_helados
    print("DATA ES %s" %data)
    return data

def encuentra_no_validos(id_materias, reg_mat_hel, id_helados):
    lista = list(reg_mat_hel)
    helados_no_validos = []
    id_no_validos = []
    for i in range(0,len(lista)):
        if not set(list(lista[i].keys())) <= set(id_materias):
            print("lista es %s y materias es %s" %(list(lista[i].keys()), id_materias))
            helados_no_validos.append(i)
            id_no_validos.append(id_helados[i])
    return helados_no_validos, id_no_validos
    

def datos_heladomaquina(helados):
    jobs = []
    print("helados son %s" %helados)
    for h in helados:
        ####TENGO LISTA DE ID DE HELADOS Y POR CADA ID OBTENGO LAS MAQUINAS Y LA GUARDO EN ORDEN EN ARREGLO JOBS
        maquinahelado = MaquinaHelado.objects.all().filter(helado = h).order_by('orden')
        job = []
        for m in maquinahelado:
            print("anadido helado %s" %h)
            job.append((m.maquina.id-1,m.tiempo))
        if job != []:
            jobs.append(job)
    return jobs

def nombre_maquinas():
    maquinas = Maquina.objects.all()
    nombres = []
    for m in maquinas:
        nombres.append(m.nombre)
    return nombres

def nombre_helados_id(id_helados):
    nombres = []
    for idh in id_helados:
        nombres.append(Helado.objects.get(id=idh).nombre)
    return nombres

def datos_packing(id_helados, tamanos, cantidades):
    nombre_helados = []
    values = []
    weights = []
    for i in range(0,len(id_helados)):
        helado = Helado.objects.get(id=id_helados[i])
        nombre_helados += [helado.nombre]* cantidades[i]
        values += [float(helado.precio) * tamanos[i]] * cantidades[i]
        weights += [tamanos[i]]*cantidades[i]
    print("Values son %s weights son %s y nombre_helados son %s" %(values,weights,nombre_helados))
    return values, weights, nombre_helados

def crear_modelo_packing(weights, values, capacidades, nombre_helados):
    data = {}
    data['weights'] = weights
    data['values'] = values
    data['items'] = list(range(len(nombre_helados)))
    data['nombre_items'] = nombre_helados
    data['num_items'] = len(weights)
    num_bins = len(capacidades) #numero de camiones en nuestro caso
    data['bins'] = list(range(num_bins))
    data['bin_capacities'] = capacidades #capacidad de cada camion
    return data

def resumir_packing(datos):
    resumido = {
        'resultado':datos['resultado'],
        'valor_total': datos['valor_total'],
        'camiones': [],
        'peso_total': datos['peso_total']
    }
    for camion in datos['camiones']:
        cargas = []
        item_anterior = camion['carga'][0]['item']
        peso_anterior = camion['carga'][0]['peso']
        contador_total = 0
        peso_total = 0
        valor_total = 0
        contador = 0
        suma_valor = 0
        for carga in camion['carga']:
            contador_total += 1
            peso_total += carga['peso']
            valor_total += carga['valor']
            if carga['item'] == item_anterior and carga['peso'] == peso_anterior:
                contador+=1
                suma_valor+=carga['valor']
            else:
                cargas.append({
                    'item': item_anterior,
                    'peso': peso_anterior,
                    'valor': suma_valor,
                    'cantidad': contador
                })
                contador = 1
                suma_valor = carga['valor']
                item_anterior = carga['item']
                peso_anterior = carga['peso']
            #Inserto la ultima:
        cargas.append({
                'item': item_anterior,
                'peso': peso_anterior,
                'valor': suma_valor,
                'cantidad': contador
        })
        resumido['camiones'].append({
            'carga':cargas,
            'cantidad_cajas': contador_total,
            'peso_camion': peso_total,
            'valor_camion': valor_total,
            'capacidad': camion['capacidad']
        })
    return resumido
        

            









