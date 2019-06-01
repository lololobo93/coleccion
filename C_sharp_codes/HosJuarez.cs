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
                         int Id = ReadId() + 1;
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
         
         /* Lee la consola para obtener lo solicitado en label,
         un String en este caso. */
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

         /* Lee la consola para obtener lo solicitado en label, un entero 
         en este caso. */
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
         
         /* Lee la base de datos para imprimir los datos del paciente con
         nombre Nombre */
         static void Read(String Nombre)
         {
             try
             {
                 SqlConnectionStringBuilder builder = new SqlConnectionStringBuilder();
                 builder.DataSource = "localhost";   
                 builder.UserID = "SA";              
                 builder.Password = "TuPassword";      
                 builder.InitialCatalog = "master";
                 using (SqlConnection conn = new SqlConnection(builder.ConnectionString))
                 {
                     conn.Open();
                     String sql = "USE HosJuarezDB; SELECT * FROM Pacientes";
                     Boolean isNoFound = true;
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
                                     Console.WriteLine("\nNombre: " + reader["Nombre"].ToString());
                                     Console.WriteLine("Curp: " + reader["Curp"].ToString());
                                     Console.WriteLine("Dirección: " + reader["Direccion"].ToString());
                                     Console.WriteLine("Edad: " + reader["Edad"].ToString());
                                     Console.WriteLine("Habitacio: " + reader["Habitacion"].ToString());
                                     isNoFound = false;
                                     mensaje("Datos del paciente solicitado");
                                 }
                             }
                         }
                         if (isNoFound)
                         {
                             mensaje("No se encontró paciente con nombre " + Nombre);
                         }
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

         /* Busca el último Id de la base de datos para ingresar las siguientes
         entradas después de esta. */
         static int ReadId()
         {
             try
             {
                 SqlConnectionStringBuilder builder = new SqlConnectionStringBuilder();
                 builder.DataSource = "localhost";   
                 builder.UserID = "SA";              
                 builder.Password = "TuPassword";      
                 builder.InitialCatalog = "master";
                 using (SqlConnection conn = new SqlConnection(builder.ConnectionString))
                 {
                     conn.Open();
                     String sql = "USE HosJuarezDB; SELECT * FROM Pacientes";
                     using (SqlCommand cmd = new SqlCommand(sql, conn))
                     {
                         SqlDataReader reader = cmd.ExecuteReader();
                         int id_count = 0;
                         if (reader.HasRows)
                         {
                             while (reader.Read())
                             {
                                 if (Convert.ToInt32(reader["Id"]) > id_count)
                                 {
                                     id_count = Convert.ToInt32(reader["Id"]);
                                 }
                             }
                         }
                         reader.Close();
                         return id_count;
                     }
                 }
             }
             catch (SqlException ex)
             {
                 Console.WriteLine(ex.ToString());
                 return 0;
                //Log exception
                //Display Error message
             }
         }

         /* Determina si existe paciente con nombre Nombre. */
         static bool FindPaciente(String Nombre)
         {
             try
             {
                 SqlConnectionStringBuilder builder = new SqlConnectionStringBuilder();
                 builder.DataSource = "localhost";   
                 builder.UserID = "SA";              
                 builder.Password = "TuPassword";      
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
                                     return true;
                                 }
                             }
                         }
                         reader.Close();
                         return false;
                     }
                 }
             }
             catch (SqlException ex)
             {
                Console.WriteLine(ex.ToString());
                return false;
                //Log exception
                //Display Error message
             }
         }

         /* Ingresa un nuevo paciente a la base de datos. */
         static void Insert(int Id, String Nombre, String Curp, String Direccion, int Edad, int Habitacion)
         {
             if (FindPaciente(Nombre))
             {
                 mensaje("Ya existe registro de paciente con nombre " + Nombre);
             }
             else {
                 try
                 {
                     SqlConnectionStringBuilder builder = new SqlConnectionStringBuilder();
                     builder.DataSource = "localhost";   
                     builder.UserID = "SA";              
                     builder.Password = "TuPassword";      
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
         }

         /* Elimina paciente Nombre de la base de datos. */
         static void Delete(String Nombre)
         {
             try
             {
                 SqlConnectionStringBuilder builder = new SqlConnectionStringBuilder();
                 builder.DataSource = "localhost";   
                 builder.UserID = "SA";              
                 builder.Password = "TuPassword";      
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
             Console.WriteLine("\n Hospital Juárez.");
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