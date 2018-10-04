/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.zobrezero.app;

/**
 *
 * @author Carlos
 */
public class Resta extends Operacion{
    
    double resta;
       
    public Resta(double n1, double n2) {
        
        // llama al constructor de la Parent de la clase, en este caso llama al constructor de la clase Operacion
        super(n1, n2, '-');
        this.resta = n1 - n2;
        this.setRes(this.resta);
    }
}
