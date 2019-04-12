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
             int tam = 10; // Tamano del arreglo
            //  Console.WriteLine("Capture el tamaño de la lista");
            //  tam = int.Parse(Console.ReadLine()); // Se pide tamano
             int[] miLista = new int[tam]; // De enteros como se desea

             int opcion;//opcion del menu 
             do{
                 Console.Clear();//se limpia consola
                 opcion = menu();//muestra menu y espera opción
                 switch (opcion)
                 {
                     /** Opciones del menu */
                     case 1: 
                         inserta_prin(miLista); 
                         imprime_lista(miLista);
                         break;
                     case 2: 
                         localiza_prin(miLista);
                         break;
                     case 3: 
                         recupera_prin(miLista);
                         break;
                     case 4: 
                         suprime_prin(miLista);
                         imprime_lista(miLista);
                         break;
                     case 5: 
                         anula(miLista); 
                         break;
                     case 6: 
                         imprime_lista(miLista); 
                         break;
                     case 7: break; //salir
                     default:                        
                         mensaje("ERROR: la opción no es valida. Intente de nuevo.");
                         break;
                 }
             }
             while(opcion!=7);
             mensaje("El programa ha finalizado.");            
         }
         /** Anade un nuevo elemento a la lista, requiere de la funcion mete 
         donde agregrar solo verifica si el valor ingresado es un int*/
         static void inserta_prin(int[] _lista )
         {  
             if (estaLlena(_lista))
             {
                 mensaje("La lista está llena, imposible insertar nuevo entero \n");
             }
             else
             {
                 int p = pos_ing();
                 if (p != (int)0)
                 {
                     int x = int_ing();
                     inserta(_lista, x, p-1);
                 }
             }
         }
         /** Anade un nuevo elemento a _lista de tipo int  */
         static void inserta(int[] _lista, int _elemento, int _pos)
         {
             if (_lista[_pos] == (int)0)
             {
                 _lista[_pos] = _elemento;
             }
             else if (izq_der(_lista, _pos))
             {
                 int elemA = _lista[_pos]; 
                 int posA = (_pos-1);
                 inserta(_lista, elemA, posA);
                 _lista[_pos] = _elemento;
             }
             else
             {
                 int elemA = _lista[_pos]; 
                 int posA = (_pos+1);
                 inserta(_lista, elemA, posA);
                 _lista[_pos] = _elemento;
             }
         }
         /** Verifica donde se tiene espacio para insertar nuevo elemento  */
         static bool izq_der(int[] _lista, int _pos)
         {
             bool fl = true;
             for (int i = _pos; i >= 0; i--)
             {
                 if (_lista[i] == (int)0)
                 {
                     fl = true;
                     return fl;
                 }
             }
             for (int i = _pos; i <= _lista.Length - 1; i++)
             {
                 if (_lista[i] == (int)0)
                 {
                     fl = false;
                     return fl;
                 }
             }
             return fl;
         }
         /** Elimina todo los elementos de la lista */
         static void anula(int[] _lista)
         {
             for (int i = _lista.Length - 1; i >= 0; i--)
             {
                 if (_lista[i] != (int)0)
                 {
                     _lista[i] = (int)0;
                 }
             }
         }
         /** Elimina un elemento de la lista */
         static void suprime_prin(int[] _lista)
         {
             if (Vacia(_lista))
             {                
                 mensaje("La lista esta vacia");
             }
             else
             {
                 int p = pos_ing();
                 if (p != (int)0) {suprime(_lista, p-1);}
             }   
         }
         /* Verifica si la lista esta vacia */
         static bool Vacia(int[] _lista)
         {
             bool fl = true;

             for (int i = _lista.Length - 1; i >= 0; i--)
             {
                 if (_lista[i] != (int)0)
                 {
                     fl = false;
                     break;
                 }
            }
             return fl;
         }
         /* Elimina el elemento en _pos de _lista */
         static void suprime(int[] _lista, int _pos)
         {
             if (_lista[_pos] == (int)0) { }
             else if (check_sup(_lista, _pos))
             {
                 _lista[_pos] = (int)0;
                 for (int i = _pos; i <= _lista.Length - 2; i++)
                 {
                     _lista[i] = _lista[i+1];
                     _lista[i+1] = (int)0;
                 }
             }
         }
         /* Revisa donde recolocar alos elmentos despues de suprimir
         algun elemento */
         static bool check_sup(int[] _lista, int _pos)
         {
             if (_pos == 0)
             {
                 return true;
             }
             else if (_lista[_pos-1] != (int)0) 
             {
                 return true;
             }
             return false;
         }
         /* Verifica si la lista esta vacia. En caso contrario pasa a la funcion
         localiza */
         static void localiza_prin(int[] _lista)
         {

             if (Vacia(_lista))
             {                
                 mensaje("La lista esta vacia");
             }
             else 
             {
                 int x = int_ing();
                 localiza(_lista, x);
             }   
         }
         /* Busca el elemento _x en _lista */
         static int localiza(int[] _lista, int _x)
         {
             for (int i = 0; i <= _lista.Length - 1; i++)
             {
                 if (_lista[i] == _x)
                 {
                     mensaje("Se encontro " + System.Convert.ToString(_x) + " en posicion " +  System.Convert.ToString(i));
                     return i;
                 }   
             }
             mensaje("NO se encontro " + System.Convert.ToString(_x) + " en lista");
             return (int)0;     
         }
         /* Verifica si la lista esta vacia. En caso contario pasa a recupera */
         static void recupera_prin(int[] _lista)
         {

             if (Vacia(_lista))
             {                
                 mensaje("La lista esta vacia");
             }
             else 
             {
                 int p = pos_ing();
                 if (p != (int)0) {recupera(_lista, p-1);}
             }   
         }
         /* Imprime el elemento en la posicion _x de _lista */
         static int recupera(int[] _lista, int _x)
         {
             if (_lista[_x] != (int)0)
             {
                 mensaje("En la posicion " + System.Convert.ToString(_x+1) + " se encontro " + System.Convert.ToString(_lista[_x]));
                 return _lista[_x];
             }
             else
             {
                 mensaje("La posicion " + System.Convert.ToString(_x) + " esta vacia");
                 return (int)0;
             }
         }
         /* Verifica si la entrada de posicion es valida */
         static int pos_ing()
         {
             Console.Write("\n> Ingrese posicion: ");
             try {
	             int p = System.Convert.ToInt32(Console.ReadLine());
                 if ((p > 10) | (p<1))
                 {
                     mensaje("Posicion fuera de rango (1-10) \n");
                     return (int)0;
                 }
                 else
                 {
                     return p;
                 }
                 } 
             catch (System.ArgumentNullException) {
	             mensaje("Error: Introduce un entero");
                 return (int)0;
                 }
             catch (System.FormatException) {
	             mensaje("Error: Introduce un entero");
                 return (int)0;
                 }
         }
         /* Verifica si la entrada de elemento es valida */
         static int int_ing()
         {
             Console.Write("\n> Ingrese entero: ");
             try {
	             int x = System.Convert.ToInt32(Console.ReadLine());
                 return x;
                 } 
             catch (System.ArgumentNullException) {
	             mensaje("Error: Introduce entero");
                 return (int)0;
                 }
             catch (System.FormatException) {
	             mensaje("Error: Introduce entero");
                 return (int)0;
                 }
         }
         /** muestra menu y retorna opción */
         static int menu()
         {
             //Console.Clear();
             Console.WriteLine("\n Hola. Bienvenido al programa que simula una lista de tamano 10. \n");
             Console.WriteLine("\n Opciones: \n");
             Console.WriteLine(" 1.- Inserta");
             Console.WriteLine(" 2.- Localiza");
             Console.WriteLine(" 3.- Recupera");
             Console.WriteLine(" 4.- Suprime");
             Console.WriteLine(" 5.- Anula");
             Console.WriteLine(" 6.- Imprimir lista");
             Console.WriteLine(" 7.- Salir del programa");
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
         /* Imprime la lista en consola de forma agradable */
         static void imprime_lista(int[] _lista)
         {
             Console.WriteLine("\n > Formal Actual de la lista");
             for (int i = 0; i <= _lista.Length - 1; i++)
             {
                 if (_lista[i] == (int)0)
                 {
                     Console.Write("  ");    
                 }
                 else
                 {
                     Console.Write(" {0} ", _lista[i]);
                 }

                 if (i < _lista.Length - 1)
                 {
                     Console.Write(",");
                 }
             }
             Console.Write("\n");
             Console.WriteLine("\n    > Presione cualquier tecla para continuar...");
             Console.ReadKey();
         }
         /* Indica si la lista esta llena */
         static bool estaLlena(int[] _lista)
         {
             bool fl = false;
             int count = 0;

             for (int i = _lista.Length - 1; i >= 0; i--)
             {
                 if (_lista[i] != (int)0)
                 {
                     count += 1; ;
                 }
             }

             if (count == _lista.Length) { fl = true; }

             return fl;
        }
     }
 }