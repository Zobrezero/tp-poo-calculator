/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.zobrezero.app;;

/**
 *  Clase que calcula la multiplicación de dos números
 *  hereda de la clase Operacion
 *
 * @author Carlos
 */
public class Multiplicacion extends Operacion
{
	// crea una variable para guardar el resultado de la operación
    double multi;

    /**
     * Constructor de la clase
     *
     * @param      n1    Primer número a multiplicar
     * @param      n2    Segundo número a multiplicar
     */
    public Multiplicacion(double n1, double n2)
    {
    	// llama al constructor de la clase Operacion
        super(n1, n2, '*');
        // hace el cálculo de la multiplicación
        this.multi = n1 * n2;
        // setea el valor obtenido
        this.setRes(this.multi);
    }
}