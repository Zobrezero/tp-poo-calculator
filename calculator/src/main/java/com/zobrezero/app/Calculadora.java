/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.zobrezero.app;

/**
 *
 * @author Carlos
 */
public class Calculadora
{
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)
    {
        // Declara dos números
        double numero1 = 10;
        double numero2 = 0;


        // Instancia la clase Suma y en el constructor pasa los números flotantes numero1 y numero2
        Suma sum = new Suma(numero1, numero2);

        // Instancia la clase Resta y en el constructor pasa los números flotantes numero1 y numero2
        Resta res = new Resta(numero1, numero2);

        // Instancia la clase Multiplicacion y en el constructor pasa los números flotantes numero1 y numero2
        Multiplicacion mul = new Multiplicacion(numero1, numero2);

        // Instancia la clase Division y en el constructor pasa los números flotantes numero1 y numero2
        Division div = new Division(numero1, numero2);


        // Accede al método que muestra el resultado de la suma
        sum.mostrarResultado();

        // Accede al método que muestra el resultado de la resta
        res.mostrarResultado();

        // Accede al método que muestra el resultado de la multiplicación
        mul.mostrarResultado();

        // Accede al método que muestra el resultado de la división
        div.mostrarResultado();
    }
}