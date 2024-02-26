#include <stdio.h>
#include <math.h>

double f(double x){ // esta función evalúa en algún punto la función dada.
    return 3*pow(x, 2) + 2*x -3;
}

double df(double x){ // esta función evalúa en algún punto la derivada de la función dada.
    return 4*x + 2;
}

double newton(double x){ // esta función implementa el algoritmo del método de Newton-Raphson.
    double x_0 = x; // alamcenamos los nuevos valores de x obtenidos en cada iteración al usar el método.
    for (int i = 0; i < 25; ++i) {
        double x_n = x_0 - f(x_0)/df(x_0); // ecuación del método de Newton.
        x_0 = x_n; // actualizamos el valor de x_0, que es el valor obtenido al usar la ecuación.
    }
    return x_0; // devolvemos el valor final de x_0.
}

int main() {
    printf("%.18f", newton(3)); // Usamos la función de método con x incial igual a 3.
    return 0;
}
