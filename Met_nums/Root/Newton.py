import numpy as np
from tools.moduloFun import *

def newton(f, interv, error, n_iter=1000, tol=1e-6, h=1e-6):
    intervals = search(f, interv)
    soluciones = []
    for i in range(len(intervals)):
        aprox = [] # almacena aproximaciones que se comparan en el error.
        seed = (intervals[i,0]+intervals[i,1])/2 #elegimos como seed el punto medio de un intervalo con raíz.
        aprox.append(seed)
        cont = 0 # nos ayuda a llevar un control en las aproximaciones y la aprovechamos para hallar el error.
        sol = 0 # guarda las actualizaciones de las aproximaciones hechas en el loop
        for _ in range(n_iter):
            x_n = seed-f(seed)/df(f, seed, h) # se está usando la diferencia central para calcular la derivada.
            if(error(x_n-aprox(cont))<tol):
                break # break si se obtiene tiene un error aceptable
            seed = x_n # actualiza el x(i-1)
            aprox.append(x_n) # envía la aproximación a la lista de ellas.
            cont += 1 # nos permite llevar un control de los elementos de aprox.
            sol = x_n # envía a sol la última aproximación hecha en las iteraciones
        soluciones.append(sol)  # envía la solución a la lista de soluciones.
    return soluciones
      

