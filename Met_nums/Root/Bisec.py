import numpy as np
from tools.moduloFun import * # importamos nuestros módulos

def bisec(f, interv, error, n_iter=1000, tol=1e-6):
    intervals = search(f, interv)
    soluciones=[] # Almacena las soluciones que va encontrando.
    for i in range(len(interv)): # con esto aseguro que hará la bisección para cada intervalo.
        a, b = intervals[i, 0], intervals[i,1] # nos da los extremos de cada subintervalo
        aprox=[] # vamos almacenando las aproximaciones para poder hacer un break al llegar al error deseado.
        x_r = (a+b)/2 # hacemos bisección una vez para obtener la primera aproximación de la lista.
        if(f(a)*f(x_r)<0):
            b=x_r
        elif(f(a)*f(x_r)>0):
            a=x_r
        aprox.append(x_r) #se añade a la lista la primera aproximación    
        cont = 0   
        sol=0
        for _ in range(n_iter): # se repetirá el ciclo tantas veces como número de iteraciones el usuario haya especificado.
            x_r=(a+b)/2 # esta variable representa el punto medio entre a y b.
            if(f(a)*f(x_r)<0): 
                b=x_r
            elif(f(a)*f(x_r)>0):
                a=x_r   
            else:
                return x_r
            aprox.append(x_r) # se añade a la lista nuestra aproximación obtenida
            if(error(x_r, aprox[cont])<=tol): # se calcula el error entre aprox_i y aprox_(i+1)
                break #se genera un break si se ha llegado al error deseado.
            cont += 1
            sol = x_r # Actualiza el valor de la aproximación.
        soluciones.append(sol) # Una vez "hallada" la solución, la almancenamos en lista de soluciones.
    return soluciones # retorna la lista de soluciones halladas.