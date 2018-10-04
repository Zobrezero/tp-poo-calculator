/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.zobrezero.app;

/**
 *  La clase Operacion define la estructura de las operaciones que se van a ejecutar posteriormente,
 *  pero sin definir en ningún momento como y en dónde se ejecutan.
 *  Permite el acceso a todas las propiedades y métodos, no se reserva nada.
 *  
 * @author Carlos
 */
public class Operacion
{
    // Declara las propiedades de la clase, son los parámetros de la operación
    // Por lo que veo, las propiedades de la clase no se les aclara si son públicas o no
    double n1;
    double n2;
    double res;
    char operacion;

    /**
     * Constructor de la clase, al crearse pide tres argumentos
     *
     * @param      n1         Número 1
     * @param      n2         Número 2
     * @param      operacion  Caracter que define la operación
     */
    public Operacion(double n1, double n2, char operacion)
    {
        this.n1 = n1;
        this.n2 = n2;
        this.operacion = operacion;
    }

    /**
     * Método que se encarga de mostrar el resultado de la operación de manera legible por humanos
     */
    public void mostrarResultado()
    {
        System.out.println(this.n1 + " " + this.operacion + " " + this.n2 + " = " + this.res);   
    }

    /**
     * Retorna el valor del número uno
     *
     * @return     El número uno.
     */
    public double getN1()
    {
        return n1;
    }

    /**
     * Le otorga un valor al número uno
     *
     * @param      n1    El valor para el número uno
     */
    public void setN1(double n1)
    {
        this.n1 = n1;
    }

    /**
     * Retorna el valor del número dos
     *
     * @return     El número dos.
     */
    public double getN2() 
    {
        return n2;
    }

    /**
     * Le otorga un valor al número dos
     *
     * @param      n2    El valor para el número dos
     */
    public void setN2(double n2)
    {
        this.n2 = n2;
    }

    /**
     * Retorna el tipo de operación definido actualmente
     *
     * @return     La operación.
     */
    public char getOperacion()
    {
        return operacion;
    }

    /**
     * Le otorga un valor a la operación
     *
     * @param      operacion  El tipo de operación a asignar
     */
    public void setOperacion(char operacion)
    {
        this.operacion = operacion;
    }

    /**
     * Retorna el resultado de la operación
     *
     * @return     EL resultado.
     */
    public double getRes()
    {
        return res;
    }

    /**
     * Le otorga un valor al resultado de la operación
     *
     * @param      res   El valor a otorgar.
     */
    public void setRes(double res)
    {
        this.res = res;
    }   
}