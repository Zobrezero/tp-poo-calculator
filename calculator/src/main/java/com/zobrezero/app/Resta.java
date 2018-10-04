/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.zobrezero.app;

/**
 * La clase hereda de la clase Operacion
 *  y agrega el valor del resultado de a operacion
 *
 * @author Carlos
 */
public class Resta extends Operacion
{
	// declara una variable para guardar el resultado de la operación
	double resta;
       
    /**
     * Constructor de la clase
     *
     * @param      n1    Primer número a restar
     * @param      n2    Segundo número a restar
     */
    public Resta(double n1, double n2)
    {
        // llama al constructor de la Parent de la clase, en este caso llama al constructor de la clase Operacion
        super(n1, n2, '-');
        // hace el calculo de la resta
        this.resta = n1 - n2;
        // setea el valor obtenido
        this.setRes(this.resta);
    }
}