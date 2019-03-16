/* Librerias usadas */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;
 
namespace ConsoleApplication1
 {
     class Program
     {
         /* Funcion principal */
         static void Main(string[] args)
         {
             int tam;// Tamano de la cola
             Console.WriteLine("Capture el tamaño de la cola");
             tam = int.Parse(Console.ReadLine()); // Pide el tamano
             char[] micola = new char[tam];// Arreglo de caracteress

             int opcion;//opcion del menu 
             do{
                 Console.Clear();//se limpia consola
                 opcion = menu();//muestra menu y espera opción
                 switch (opcion)
                 {
                     /* Se realizada cada accion sobre la cola */
                     case 1: 
                         anula(micola); 
                         break;
                     case 2: 
                         frente(micola);
                         break;
                     case 3: 
                         Pone_en_cola(micola); 
                         imprimir(micola);
                         break;
                     case 4: 
                         quita_de_cola(micola);
                         imprimir(micola); 
                         break;
                     case 5: 
                         if (Vacia(micola))
                         {
                             mensaje("La cola esta vacia");
                         } 
                         else
                         {
                             mensaje("La cola NO esta vacia");
                         }
                         break;
                     case 6: break; //salir
                     default:                        
                         mensaje("ERROR: la opción no es valida. Intente de nuevo.");
                         break;
                 }
             }
             while(opcion!=6);
             mensaje("El programa ha finalizado.");            
         }
         /** añade un nuevo elemento a la cola, requiere de mete donde Pone_en_cola
         verifica si el valor introducido es de tipo char */
         static void Pone_en_cola(char[] _cola )
         {
             Console.Write("\n> Ingrese caracter: ");
             try {
	             char Elemento = System.Convert.ToChar(Console.ReadLine());
                 if (estaLlena(_cola))
                 {
                     mensaje("La cola está llena, imposible agregar nuevo caracter \n");
                 }
                 else
                 {
                     mete(_cola, Elemento);
                 }
                 } 
             catch (System.ArgumentNullException) {
	             mensaje("Error: No existe caracter");
                 }
             catch (System.FormatException) {
	             mensaje("Error: Longitud de caracter mayor a 1");
                 }           
         } 
         /* Introduce _elemento en _cola */
         static bool mete(char[] _cola, char _elemento)
         {
             bool fl = false;

             for (int i = _cola.Length - 1; i >= 0; i--)
             {
                 if (_cola[i] != (char)0)
                 {
                     _cola[i + 1] = _elemento;
                     fl = true;
                     break;
                 }
                 else if (_cola[i] == (char)0 && i == 0)
                 {
                     _cola[i] = _elemento;
                     fl = true;
                     break;
                 }
             }
             return fl;
         }
         /** Elimina todo los elementos de la cola */
         static bool anula(char[] _cola)
         {
             bool fl = false;

             for (int i = _cola.Length - 1; i >= 0; i--)
             {
                 if (_cola[i] != (char)0)
                 {
                     _cola[i] = (char)0;
                 }
             }
             fl = true;
             return fl;
         }
         /** Elimina primer elemento de la cola, requiere de Suprime */
         static void quita_de_cola(char[] _cola)
         {
             if (Vacia(_cola))
             {                
                 mensaje("La cola esta vacia");
             }
             else {
                 Suprime(_cola);
             }   
         }
         /* Imprime en consola el primer elemento de la cola (frente) */
         static void frente(char[] _cola)
         {
             if (Vacia(_cola))
             {
                 mensaje("La cola esta vacia");
             }
             else
             {
                for (int i = 0; i <= _cola.Length - 1; i++)
                 {
                     if (_cola[i] != (char)0)
                     {
                         mensaje("frente: " + _cola[i]);
                         break;
                     }
                 }    
             }
         }
         /* Indica si la pila esta vacia */
         static bool Vacia(char[] _cola)
         {
             bool fl = true;

             for (int i = _cola.Length - 1; i >= 0; i--)
             {
                 if (_cola[i] != (char)0)
                 {
                     fl = false;
                     break;
                 }
            }
             return fl;
         }
         /* Se elimina elemento del frente de la cola */
         static bool Suprime(char[] _cola)
         {
             bool fl = false;

             for (int i = 0; i <= _cola.Length - 1; i++)
             {
                 if (_cola[i] != (char)0)
                 {
                     _cola[i] = (char)0;
                     fl = true;
                     break;
                 }
             }

             return fl;
         }

         /** muestra menu y retorna opción */
         static int menu()
         {
             //Console.Clear();
             Console.WriteLine("\n            Menu\n");
             Console.WriteLine(" 1.- Vaciar cola");
             Console.WriteLine(" 2.- Ver frente");
             Console.WriteLine(" 3.- Agregar elemento");
             Console.WriteLine(" 4.- Sacar elemento");
             Console.WriteLine(" 5.- Esta vacia");
             Console.WriteLine(" 6.- Termina programa");
             Console.Write(" > Ingresa tu opción: ");            
             try
             {
                 int valor = Convert.ToInt32( Console.ReadLine() );                
                 return valor;
             }
             catch {
                 return 0;
             }            
         }
 
         /** Muestra mensaje del programa al usuario */
         static void mensaje( String texto )
         {
             if (texto.Length > 0)
             {
                 Console.WriteLine("\n =======================================================");
                 Console.WriteLine(" > {0}", texto);
                 Console.WriteLine(" =======================================================");
                 Console.WriteLine("\n    > Presione cualquier tecla para continuar...");
                 Console.ReadKey();
             }            
         }
         /* Imprime cola de forma agradable en la consola */
         static void imprimir(char[] _cola)
         {
                 Console.WriteLine("\n > Formal Actual de la cola \n");
                 for (int i = 0; i <= _cola.Length - 1; i++)
                 {
                     if (_cola[i] != (char)0)
                     {
                         Console.Write("| {0} ", _cola[i]);
                     }
                 }
                 Console.Write("|\n");
                 Console.WriteLine("\n    > Presione cualquier tecla para continuar...");
                 Console.ReadKey();
         }
         /* Verifica si la cola esta llena */
         static bool estaLlena(char[] _cola)
         {
             bool fl = false;
             int count = 0;

             for (int i = _cola.Length - 1; i >= 0; i--)
             {
                 if (_cola[i] != (char)0)
                 {
                     count += 1; ;
                 }
             }

             if (count == _cola.Length) { fl = true; }

             return fl;
        }
     }
 }