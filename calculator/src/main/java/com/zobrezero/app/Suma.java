/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.zobrezero.app;

/**
 * La clase suma hereda la estructura de la clase Operacion,
 * también agrega el valor de la operación
 * s
 * @author Carlos
 */
public class Suma extends Operacion
{
    // Declara una variable para el resultado de la suma
    double suma;

    /**
     * Constructor de la clase, tiene dos argumentos que son los números a sumar
     *
     * @param      n1    Un número a sumar
     * @param      n2    Otro número a decir
     */
    public Suma(double n1, double n2)
    {
    	// Llama al constructor del parent Operacíon
        super(n1, n2, '+');
        // Calcula la suma de los ńúmeros
        this.suma = n1 + n2;
        // Setea el valor de la suma con un método heredado
        this.setRes(this.suma);
    }
}