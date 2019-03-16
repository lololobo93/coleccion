/** Librerias a usar */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;

namespace ConsoleApplication1
 {
     class Program
     {
         /** Funcion principal */
         static void Main(string[] args)
         {
             int tam; // Tamano del arreglo
             Console.WriteLine("Capture el tamaño de la pila");
             tam = int.Parse(Console.ReadLine()); // Se pide tamano
             char[] miPila = new char[tam]; // De caracteres como se desea

             int opcion;//opcion del menu 
             do{
                 Console.Clear();//se limpia consola
                 opcion = menu();//muestra menu y espera opción
                 switch (opcion)
                 {
                     /** Opciones del menu */
                     case 1: 
                         anula(miPila); 
                         break;
                     case 2: 
                         saca(miPila);
                         imprimir(miPila); 
                         break;
                     case 3: 
                         agregar(miPila); 
                         imprimir(miPila);
                         break;
                     case 4: 
                         if (Vacia(miPila))
                         {
                             mensaje("La pila esta vacia");
                         } 
                         else
                         {
                             mensaje("La pila NO esta vacia");
                         }
                         break;
                     case 5: 
                         tope(miPila); 
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
         /** Anade un nuevo elemento a la pila, requiere de la funcion mete 
         donde agregrar solo verifica si el valor ingresado es un char*/
         static void agregar(char[] _pila )
         {
             Console.Write("\n> Ingrese caracter: ");
             try {
	             char Elemento = System.Convert.ToChar(Console.ReadLine());
                 if (estaLlena(_pila))
                 {
                     mensaje("La pila está llena, imposible agregar nuevo caracter \n");
                 }
                 else
                 {
                     mete(_pila, Elemento);
                 }
                 } 
             catch (System.ArgumentNullException) {
	             mensaje("Error: No existe caracter");
                 }
             catch (System.FormatException) {
	             mensaje("Error: Longitud de caracter mayor a 1");
                 }           
         } 
         /** Anade un nuevo elemento a _pila de tipo char  */
         static bool mete(char[] _pila, char _elemento)
         {
             bool fl = false;

             for (int i = _pila.Length - 1; i >= 0; i--)
             {
                 if (_pila[i] != (char)0)
                 {
                     _pila[i + 1] = _elemento;
                     fl = true;
                     break;
                 }
                 else if (_pila[i] == (char)0 && i == 0)
                 {
                     _pila[i] = _elemento;
                     fl = true;
                     break;
                 }
             }
             return fl;
         }
         /** Elimina todo los elementos de la pila */
         static bool anula(char[] _pila)
         {
             bool fl = false;

             for (int i = _pila.Length - 1; i >= 0; i--)
             {
                 if (_pila[i] != (char)0)
                 {
                     _pila[i] = (char)0;
                 }
             }
             fl = true;
             return fl;
         }
         /** Elimina ultimo elemento de la pila */
         static void saca(char[] _pila)
         {
             if (Vacia(_pila))
             {                
                 mensaje("La pila esta vacia");
             }
             else {
                 Suprime(_pila);
             }   
         }
         /* Imprime el tope de la pila o indica si esta vacia */
         static void tope(char[] _pila)
         {
             if (Vacia(_pila))
             {
                 mensaje("La pila esta vacia");
             }
             else
             {
                for (int i = _pila.Length - 1; i >= 0; i--)
                 {
                     if (_pila[i] != (char)0)
                     {
                         mensaje("tope: " + _pila[i]);
                         break;
                     }
                 }    
             }
         }
         /* Verifica si la pila esta vacia */
         static bool Vacia(char[] _pila)
         {
             bool fl = true;

             for (int i = _pila.Length - 1; i >= 0; i--)
             {
                 if (_pila[i] != (char)0)
                 {
                     fl = false;
                     break;
                 }
            }
             return fl;
         }
         /* Vacia la pila */
         static bool Suprime(char[] _pila)
         {
             bool fl = false;

             for (int i = _pila.Length - 1; i >= 0; i--)
             {
                 if (_pila[i] != (char)0)
                 {
                     _pila[i] = (char)0;
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
             Console.WriteLine(" 1.- Vaciar Pila");
             Console.WriteLine(" 2.- Sacar elemento");
             Console.WriteLine(" 3.- Agregar elemento");
             Console.WriteLine(" 4.- Esta vacia");
             Console.WriteLine(" 5.- Ver tope");
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
         /* Imprime la pila en consola de forma agradable */
         static void imprimir(char[] _pila)
         {
                 Console.WriteLine("\n > Formal Actual de la pila");
                 for (int i = _pila.Length - 1; i >= 0; i--)
                 {
                     if (_pila[i] != (char)0)
                     {
                         Console.WriteLine("-----");
                         Console.WriteLine("| {0} |", _pila[i]);
                     }
                 }
                 Console.WriteLine("-----");
                 Console.WriteLine("\n    > Presione cualquier tecla para continuar...");
                 Console.ReadKey();
         }
         /* Indica si la pila esta llena */
         static bool estaLlena(char[] _pila)
         {
             bool fl = false;
             int count = 0;

             for (int i = _pila.Length - 1; i >= 0; i--)
             {
                 if (_pila[i] != (char)0)
                 {
                     count += 1; ;
                 }
             }

             if (count == _pila.Length) { fl = true; }

             return fl;
        }
     }
 }