/** Librerias a usar */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;
using System.Data.SqlClient;

namespace ConsoleApplication1
 {
     class Program
     {
         /** Funcion principal */
         static void Main(string[] args)
         {
             int opcion;//opcion del menu 
            //  Create();
             do{
                 Console.Clear();//se limpia consola
                 opcion = menu();//muestra menu y espera opción
                 switch (opcion)
                 {
                     /** Opciones del menu */
                     case 1: 
                         int Id = Read_Console_Int("id");
                         String Nombre = Read_Console_Str("nombre");
                         String Direccion = Read_Console_Str("dirección");
                         String Curp = Read_Console_Str("curp");
                         int Edad = Read_Console_Int("edad");
                         int Habitacion = Read_Console_Int("Habitacion");
                         Insert(Id, Nombre, Curp, Direccion, Edad, Habitacion); 
                         break;
                     case 2: 
                         Nombre = Read_Console_Str("nombre");
                         Read(Nombre);
                         break;
                     case 3: 
                         Nombre = Read_Console_Str("nombre");
                         Delete(Nombre);
                         break;
                     case 4: break; //salir
                     default:                        
                         mensaje("ERROR: la opción no es valida. Intente de nuevo.");
                         break;
                 }
             }
             while(opcion!=4);
             mensaje("El programa ha finalizado.");            
         }

         static String Read_Console_Str(String label){
             Console.Write("\n> Ingrese " + label + " : ");
             try {
	             String x = System.Convert.ToString(Console.ReadLine());
                 return x;
                 } 
             catch (System.ArgumentNullException) {
	             mensaje("Error: Entradad incorrecta");
                 return " ";
                 }
             catch (System.FormatException) {
	             mensaje("Error: Entrada incorrecta");
                 return " ";
                 }
         }

         static int Read_Console_Int(String label){
             Console.Write("\n> Ingrese " + label + " : ");
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
         
         static void Read(String Nombre)
         {
             try
             {
                 SqlConnectionStringBuilder builder = new SqlConnectionStringBuilder();
                 builder.DataSource = "localhost";   // update me
                 builder.UserID = "SA";              // update me
                 builder.Password = "Mercenario93";      // update me
                 builder.InitialCatalog = "master";
                 using (SqlConnection conn = new SqlConnection(builder.ConnectionString))
                 {
                     conn.Open();
                     String sql = "USE HosJuarezDB; SELECT * FROM Pacientes";
                     using (SqlCommand cmd = new SqlCommand(sql, conn))
                     {
                         SqlDataReader reader = cmd.ExecuteReader();

                         if (reader.HasRows)
                         {
                             while (reader.Read())
                             {
                                 if (reader["Nombre"].ToString() == Nombre)
                                 {
                                     //  Console.WriteLine("Id = ", reader["Id"]);
                                     Console.WriteLine("Nombre = " + reader["Nombre"].ToString());
                                     Console.WriteLine("Curp = " + reader["Curp"].ToString());
                                     Console.WriteLine("Direccion = " + reader["Direccion"].ToString());
                                     Console.WriteLine("Edad = " + reader["Edad"].ToString());
                                     Console.WriteLine("Habitacion = " + reader["Habitacion"].ToString());
                                 }
                             }
                         }
                         mensaje("Paciente del hospital");
                         reader.Close();
                     }
                 }
             }
             catch (SqlException ex)
             {
                Console.WriteLine(ex.ToString());
                //Log exception
                //Display Error message
             }
         }

         static void Insert(int Id, String Nombre, String Curp, String Direccion, int Edad, int Habitacion)
         {
             try
             {
                 SqlConnectionStringBuilder builder = new SqlConnectionStringBuilder();
                 builder.DataSource = "localhost";   // update me
                 builder.UserID = "SA";              // update me
                 builder.Password = "Mercenario93";      // update me
                 builder.InitialCatalog = "master";
                 using (SqlConnection conn = new SqlConnection(builder.ConnectionString))
                 {
                     conn.Open();
                     String sql = "USE HosJuarezDB; INSERT INTO Pacientes VALUES(" +
                             "@Id, @Nombre, @Curp, @Direccion, @Edad, @Habitacion)";
                     using (SqlCommand cmd = new SqlCommand(sql, conn))
                     {
                         cmd.Parameters.AddWithValue("@Id", Id);
                         cmd.Parameters.AddWithValue("@Nombre", Nombre);
                         cmd.Parameters.AddWithValue("@Curp", Curp);
                         cmd.Parameters.AddWithValue("@Direccion", Direccion);
                         cmd.Parameters.AddWithValue("@Edad", Edad);
                         cmd.Parameters.AddWithValue("@Habitacion", Habitacion);

                         int rows = cmd.ExecuteNonQuery();

                         //rows number of record got inserted
                     }
                     mensaje("Se ingreso nuevo paciente");
                 }
             }
             catch (SqlException ex)
             {
                 Console.WriteLine(ex.ToString());
             }
         }

         static void Delete(String Nombre)
         {
             try
             {
                 SqlConnectionStringBuilder builder = new SqlConnectionStringBuilder();
                 builder.DataSource = "localhost";   // update me
                 builder.UserID = "SA";              // update me
                 builder.Password = "Mercenario93";      // update me
                 builder.InitialCatalog = "master";
                 using (SqlConnection conn = new SqlConnection(builder.ConnectionString))
                 {
                     conn.Open();
                     String sql = "USE HosJuarezDB; DELETE FROM Pacientes WHERE Nombre=@Nombre";
                     using (SqlCommand cmd = new SqlCommand(sql, conn))
                     {
                         cmd.Parameters.AddWithValue("@Nombre", Nombre);
                         
                         int rows = cmd.ExecuteNonQuery();

                         //rows number of record got deleted
                     }
                     mensaje("Se eliminó paciente");
                 }
             }
             catch (SqlException ex)
             {
                 Console.WriteLine(ex.ToString());
             }
         }

         /** muestra menu y retorna opción */
         static int menu()
         {
             //Console.Clear();
             Console.WriteLine("\n Hospital Juárez. \n");
             Console.WriteLine("\n Registro de pacientes. \n");
             Console.WriteLine(" 1.- Añadir paciente");
             Console.WriteLine(" 2.- Consultar paciente");
             Console.WriteLine(" 3.- Eliminar paciente");
             Console.WriteLine(" 4.- Salir del programa");
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
     }
 }