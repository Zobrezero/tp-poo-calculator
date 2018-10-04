/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.zobrezero.app;

/**
 *
 * @author Carlos
 */
public class Division extends Operacion
{
    // crea una variable para guardar el resultado de la división
    double div = 0;

    /**
     * Constuctor de la clase
     *
     * @param      n1    Numerador de la división
     * @param      n2    Denominador de la división
     */
    public Division(double n1, double n2)
    {
        // llama al constructor de la clase Operacion
        super(n1, n2, '/');
        // revisa el valor del denominador sea distinto de cero así poder calcular la división
        // de lo contrario muestra un error legible al usuario
        if(n2 == 0)
        	System.out.println("no se puede division entre cero");
        else
        	this.div = n1 / n2;
        // guarda el valor de la divisón
        this.setRes(this.div);
    }
}