#include <stdio.h>
#include <math.h>
double eval(double x) { // función que evalúa la función de grado 2 en un valor dado como argumento.
    return pow(x, 2) + 2 * x - 3;}

double bisect(double a, double b) { // la función que implementa el algoritmo lógico del método de bisección.
    double sol = 0; // esta variable almacenará el valor de x_r de cada iteración.
    for (int i = 0; i < 4000; ++i){ // pude usar un while, pero preferí no considerar errores y usar un for.
        double x_r = (a + b) / 2; // definición del punto medio.
        if ((eval(a) * eval(x_r)) < 0) // condición 1: si f(a) y f(x_r) son de distinto signo.
            b = x_r; // que el extremo derecho sea ahora x_r.
        else if ((eval(a) * eval(x_r)) > 0) // condición 2: si f(a) y f(x_r) son del mismo signo.
            a = x_r; // que el extremo izquierdo sea ahora x_r.
        sol = x_r;} //
    return sol;}

int main() {
    printf("%.12f\n", bisect(0, 2));
    return 0;}



