import collections
from ortools.linear_solver import pywraplp
from ortools.sat.python import cp_model
import numpy as np


def create_data_model ():
    data={}
    data['constraint_coeffs']=[[10,8],[6,2]]#Cant de MP usada para hacer el helado
    data['bounds']=[20000,10000]#MP disponible
    data['obj_coeffs']=[70,50]#Precio de helados
    data['num_vars']=2#N° helados
    data['precio_base']=[20,10] #Dinero que cuesta cada MP por unidad
    data['num_constraints']=2#N° de MP
    data['demanda']=[100,100]
    return data

def minimizacion_costos(data):
    #inciamos el modelo
    #data = create_data_model()
    solver = pywraplp.Solver('finalLogica', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    #cargamos las variables de decision
    x = {}
    for j in range(data['num_vars']):
        x[j] = solver.NumVar(0, solver.infinity(), 'x[%i]' %j) #Averiguar que es %j, probar eliminarlo

    print('Number of variables =', solver.NumVariables())
    # print(nombreMP)
    # print(cantMP)
    # print(porcPerdida)
    # print(SaboresH)
    # print(PrecioH)

    #cargamos restricciones
    for i in range(data['num_constraints']):
        constraint = solver.RowConstraint(0, data['bounds'][i], '') #Selecciona la cant disponible de mp
        for j in range(data['num_vars']):
            constraint.SetCoefficient(x[j], data['constraint_coeffs'][i][j])

  #Restriccion de que la produccion debe ser mayor o igual que la demanda
    for i in range(data['num_vars']):
        constraint = solver.RowConstraint(data['demanda'][i], float('inf') , '')
        for j in range(solver.NumVariables()):
            constraint.SetCoefficient(x[j],1) 
        


  #cargamos objetivo
    objective = solver.Objective()
    for j in range(data['num_vars']):
        objective.SetCoefficient(x[j], data['precio_base'][j])
    objective.SetMinimization()


  # MINIMIZACION DE COSTOS
    respuesta = {}
    respuesta["objetivo"] = "minimizacion_costos"
    respuesta["nombre_helados"] = data["nombre_helados"]
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        respuesta["resultado"] = "exito"
        respuesta["objective_value"] = str(round(solver.Objective().Value(),2))
        respuesta["soluciones"] = []
        print('Objective value =', solver.Objective().Value())
        for j in range(data['num_vars']):
            print(x[j].name(), ' = ', x[j].solution_value())
            respuesta["soluciones"].append({"nombre": data["nombre_helados"][j], "cantidad": str(round(x[j].solution_value(),2))})

            
    else:
        print('The problem does not have an optimal solution.')
        respuesta["resultado"] = "fracaso"
        respuesta["razon_fracaso"] = "no_solucion"
    return respuesta


def maximizacion_ganancias(data):
    solver = pywraplp.Solver('finalLogica', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    #cargamos las variables de decision
    x = {}
    for j in range(data['num_vars']):
        x[j] = solver.NumVar(0, solver.infinity(), 'x[%i]' %j) #Averiguar que es %j, probar eliminarlo

    print('Number of variables =', solver.NumVariables())
    #print(nombreMP)
    #print(cantMP)
    #print(porcPerdida)
    #print(SaboresH)
    #print(PrecioH)

    #cargamos restricciones
    for i in range(data['num_constraints']):
        constraint = solver.RowConstraint(0, data['bounds'][i], '') #Selecciona la cant disponible de mp
        for j in range(data['num_vars']):
            constraint.SetCoefficient(x[j], data['constraint_coeffs'][i][j])

    #Restriccion de que la produccion debe ser mayor o igual que la demanda
    for i in range(data['num_vars']):
        constraint = solver.RowConstraint(0, data['demanda'][i] , '')
        for j in range(solver.NumVariables()):
            constraint.SetCoefficient(x[j],1) 

    #cargamos objetivo
    objective = solver.Objective()
    for j in range(data['num_vars']):
        objective.SetCoefficient(x[j], data['obj_coeffs'][j])
    objective.SetMaximization()

    #Si se minimiza da 0, no minimizar 

    # MAXIMIZACION DE LAS GANANCIAS
    respuesta = {}
    respuesta["objetivo"] = "maximizacion_ganancias"
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        respuesta["resultado"] = "exito"
        respuesta["objective_value"] = str(round(solver.Objective().Value(),2))
        respuesta["soluciones"] = []
        print('Objective value =', solver.Objective().Value())
        for j in range(data['num_vars']):
            print(x[j].name(), ' = ', x[j].solution_value())
            respuesta["soluciones"].append({"nombre": data["nombre_helados"][j], "cantidad": str(round(x[j].solution_value(),2))})

            
    else:
        print('The problem does not have an optimal solution.')
        respuesta["resultado"] = "fracaso"
        respuesta["razon_fracaso"] = "no_solucion"
    return respuesta




def maximizacion_produccion(data):
    solver = pywraplp.Solver('finalLogica', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    #cargamos las variables de decision
    x = {}
    for j in range(data['num_vars']):
        x[j] = solver.NumVar(0, solver.infinity(), 'x[%i]' %j) #Averiguar que es %j, probar eliminarlo


    #cargamos restricciones
    for i in range(data['num_constraints']):
        constraint = solver.RowConstraint(0, data['bounds'][i], '') #Selecciona la cant disponible de mp
    for j in range(data['num_vars']):
        constraint.SetCoefficient(x[j], data['constraint_coeffs'][i][j])

    #Restriccion de que la produccion debe ser mayor o igual que la demanda
    for i in range(data['num_vars']):
        #constraint = solver.RowConstraint(data['demanda'][i], float('inf') , '') #para menor igual  de cero a demanda en vez de demanda a infinito
        constraint = solver.RowConstraint(0, data['demanda'][i] , '') #MENOR QUE LA DEMANDA
        for j in range(solver.NumVariables()):
            constraint.SetCoefficient(x[j],1) 

    #cargamos objetivo
    objective = solver.Objective()
    for j in range(data['num_vars']):
        objective.SetCoefficient(x[j], 1)
    objective.SetMaximization()

    respuesta = {}
    respuesta["objetivo"] = "maximizacion_produccion"
    respuesta["nombre_helados"] = data["nombre_helados"]
    
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        respuesta["resultado"] = "exito"
        respuesta["objective_value"] = str(round(solver.Objective().Value(),2))
        respuesta["soluciones"] = []
        print('Objective value =', solver.Objective().Value())
        for j in range(data['num_vars']):
            print(x[j].name(), ' = ', x[j].solution_value())
            respuesta["soluciones"].append(str(round(x[j].solution_value(),2)))

            
    else:
        print('The problem does not have an optimal solution.')
        respuesta["resultado"] = "fracaso"
        respuesta["razon_fracaso"] = "no_solucion"
    return respuesta

def Scheduling(jobs_data, nombre_maquinas, nombre_helados):
    print("SCHEDULIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIING")
    print("JOBS DATA ES %s" %jobs_data)
    # Create the model.
    model = cp_model.CpModel()

    #se fija en el primer componente de cada tupla, para asi encontrar la cantidad de maquinas
    machines_count = 1 + max(task[0] for job in jobs_data for task in job) # +1 eliminado
    print("MACHINE COUNT ES %s" %machines_count)
    all_machines = range(machines_count)
    #la duracion de las tareas(horizon) se calcula como la sumatoria de todas las duraciones
    # Computes horizon dynamically as the sum of all durations.
    horizon = sum(task[1] for job in jobs_data for task in job)

    # Named tuple to store information about created variables.
    task_type = collections.namedtuple('task_type', 'start end interval')
    # Named tuple to manipulate solution information.
    assigned_task_type = collections.namedtuple('assigned_task_type',
                                                'start job index duration')

    # Creates job intervals and add to the corresponding machine lists.
    all_tasks = {}
    machine_to_intervals = collections.defaultdict(list)

    for job_id, job in enumerate(jobs_data):
        for task_id, task in enumerate(job):
            machine = task[0]
            duration = task[1]
            suffix = '_%i_%i' % (job_id, task_id)
            start_var = model.NewIntVar(0, horizon, 'start' + suffix)
            end_var = model.NewIntVar(0, horizon, 'end' + suffix)
            interval_var = model.NewIntervalVar(start_var, duration, end_var,
                                                'interval' + suffix)
            all_tasks[job_id, task_id] = task_type(
                start=start_var, end=end_var, interval=interval_var)
            machine_to_intervals[machine].append(interval_var)

    #para evitar el solapamiento de tareas
    # Create and add disjunctive constraints.
    for machine in all_machines:
        model.AddNoOverlap(machine_to_intervals[machine])

    # Restriccion para definir el orden de ejecucion de las tareas.
    for job_id, job in enumerate(jobs_data):
        for task_id in range(len(job) - 1):
            model.Add(all_tasks[job_id, task_id +
                                1].start >= all_tasks[job_id, task_id].end)

    # Makespan objective.
    obj_var = model.NewIntVar(0, horizon, 'makespan')
    model.AddMaxEquality(obj_var, [
        all_tasks[job_id, len(job) - 1].end
        for job_id, job in enumerate(jobs_data)
    ])
    model.Minimize(obj_var)

    # Solve model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Create one list of assigned tasks per machine.
    assigned_jobs = collections.defaultdict(list)
    for job_id, job in enumerate(jobs_data):
        for task_id, task in enumerate(job):
            machine = task[0]
            assigned_jobs[machine].append(
                assigned_task_type(
                    start=solver.Value(all_tasks[job_id, task_id].start),
                    job=job_id,
                    index=task_id,
                    duration=task[1]))

    # Create per machine output lines.
    output = ''
    arr=np.array('')
    print("ALL MACHINES ES %s" %all_machines)

    rows = []
    for machine in all_machines:
        # Sort by starting time.
        assigned_jobs[machine].sort()
        sol_line_tasks =nombre_maquinas[machine] + ': '
        sol_line = '           '

        for assigned_task in assigned_jobs[machine]:
            # ['TrabajoMaquina', 'Trabajo en Maquina (no relev)', 'Maquina', null, null,  toMilliseconds(5), 100, null]
            #name = 'trabajo_%i_%i  ' % (assigned_task.job, assigned_task.index) #numero de helado, numero de esa maquina para ese helado
            name = ' %s en %s depende de %s' %(nombre_helados[assigned_task.job], nombre_maquinas[assigned_task.index],nombre_maquinas[assigned_task.index-1])

            rows.append([nombre_helados[assigned_task.job]+nombre_maquinas[assigned_task.index], 
                nombre_helados[assigned_task.job]+" en " +nombre_maquinas[assigned_task.index],
                nombre_maquinas[assigned_task.index],
                assigned_task.start,
                assigned_task.start + assigned_task.duration,
                None,
                100,
                nombre_helados[assigned_task.job]+nombre_maquinas[assigned_task.index-1] 
            ])
            if assigned_task.index == 0:
                rows[-1][-1] = None
            # Add spaces to output to align columns.
            sol_line_tasks += '%-10s' % name

            start = assigned_task.start
            duration = assigned_task.duration
            sol_tmp = '[%i,%i]' % (start, start + duration)

            # Add spaces to output to align columns.
            sol_line += '%-10s' % sol_tmp
        new_arr=np.delete(arr,0)
        sol_line += '\n'
        sol_line_tasks += '\n'
        output += sol_line_tasks
        output += sol_line

    # Finally print the solution found.
    print('Optimal Schedule Length: %i' % solver.ObjectiveValue())
    print(output)
    print(new_arr)
    print(rows)
    #return "Duracion optima es %i \n Output es %s y new_arr es %s" %(solver.ObjectiveValue(), output, new_arr)
    return {'duracion_optima': solver.ObjectiveValue(), 'rows': rows}


def Packing(data):

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Variables
    # x[i, j] = 1 if item i is packed in bin j.
    x = {}
    for i in data['items']:
        for j in data['bins']:
            x[(i, j)] = solver.IntVar(0, 1, 'x_%i_%i' % (i, j))

    # Restricciones
    # Cada item puede estar tan solo en un camion
    for i in data['items']:
        solver.Add(sum(x[i, j] for j in data['bins']) <= 1)
    # El total de cajas no puede superar el tamaño del camion.
    for j in data['bins']:
        solver.Add(
            sum(x[(i, j)] * data['weights'][i]
                for i in data['items']) <= data['bin_capacities'][j])

    # Objetivo
    objective = solver.Objective()

    for i in data['items']:
        for j in data['bins']:
            objective.SetCoefficient(x[(i, j)], data['values'][i])
    objective.SetMaximization()

    status = solver.Solve()
    respuesta = {}

    if status == pywraplp.Solver.OPTIMAL:
        print("objective value es ", type(objective.Value()))
        respuesta["resultado"] = "exito"
        print('Total packed value:', objective.Value())
        respuesta["valor_total"] = objective.Value()
        respuesta["camiones"] = []
        total_weight = 0
        for j in data['bins']:
            bin_weight = 0
            bin_value = 0
            respuesta["camiones"].append({"carga": [], "capacidad": data['bin_capacities'][j], })
            print('Bin ', j, '\n')
            for i in data['items']:
                if x[i, j].solution_value() > 0:
                    print('Item', i, '- weight:', data['weights'][i], ' value:',
                          data['values'][i])
                    bin_weight += data['weights'][i]
                    bin_value += data['values'][i]
                    respuesta["camiones"][j]["carga"].append({"item": data["nombre_items"][i], "peso":data['weights'][i], "valor":data['values'][i]})
            print('Packed bin weight:', bin_weight)
            respuesta["camiones"][j]["peso_camion"] = bin_weight
            print('Packed bin value:', bin_value)
            respuesta["camiones"][j]["valor_camion"] = bin_value
            print()
            total_weight += bin_weight
        print('Total packed weight:', total_weight)
        respuesta["peso_total"] = total_weight
    else:
        print('The problem does not have an optimal solution.')
        respuesta["resultado"] = "fracaso"
        respuesta["razon_fracaso"] = "no_solucion"
    return respuesta

