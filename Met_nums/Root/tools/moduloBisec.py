import numpy as np

def check1(f, interv): # con esta función revisaremos si la función y el intervalo son argumentos aceptables.
    if(callable(f) and len(interv)==2):
        return True
    
def errors(err): # Diccionario que guarda los tipos de errores seleccionables como funciones.
    error = {'real': lambda f1, f0 : f1-f0 , 'abs': lambda f1, f0: abs(f1-f0), 'rel': lambda f1, f0: abs(f1-f0)/f1,
             'rel_max': lambda f1, f0: abs(f1-f0)/abs(max([f1, f0]))}  

def f_signo(f, interv): #esta función evaluará la función que se le dará de argumento y verá si se ha atravesado el
                      #eje x en ese intervalo al revisar los signos de la función evaluada en ambos puntos.
    a, b = min(interv), max(interv)
    if(f(a)*f(b)<0):
        return 1
    elif(f(a)*f(b)>0):
        return -1
    else:
        return 0      

def search(f, interv, n_intervs=100):#con esta función encontraré intervalos donde haya raíces. Créditos al profesor.

    a, b = min(interv), max(interv) # asigna a 'a' y 'b' el menor y mayor elemento del intervalo dado.

    if (a>0) and (b>0) and abs(b-a)<1: # Ajustamos la escala dependiendo de la distancia entre extremos.
        interDisc = np.linspace(a, b, 10)
    else:    
        interDisc = np.linspace(a, b, n_intervs) 

    intervals = [] # Almacena tods los intervalos donde halle cambios en el signo de la función evaluada.
    for i in range(n_intervs-1):
        inter_i = [interDisc[i], interDisc[i+1]] # Crea un arreglo con el elemento i-ésimo del intervalo y el siguiente.
        if (search(f, inter_i)): # busca si hay cambio de signo en la función evaluada en esos dos extremos (subintervalo)
            intervals.append(inter_i) # si hay cambio de signo, añade este subintervalo a intervals.     
    return intervals # al terminar el loop, regresa la lista de todos los subintervalos donde halló que habría raíces.   


    
    