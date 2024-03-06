import numpy as np
from tools.moduloBisec import *

    
def bisec(f, interv, error, n_iter=1000, tol=1e-6):
    intervals = search(f, interv)
    sol=[] # Almacena las soluciones que va encontrando.
        for _ in range(n_iter): # se repetirá el ciclo tantas veces como número de iteraciones el usuario haya especificado.
            x_r=(a+b)/2 # esta variable representa el punto medio entre a y b.
            if(<0): 
                b=x_r
            elif(eval(a)*eval(x_r)>0):
                a=x_r
            else:
                return x_r
            sol=x_r
        return sol
    else:
        print(check)
    
print(bisec(0.5, 1))