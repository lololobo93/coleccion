import java.io.FileReader;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.Statement;
 
/**
 * Clase de apoyo para el archivo principal ProyectoFinal.
 * En esta se crea la base de datos donde se guardan los
 * datos de los archivos CSV.
 */
public class ImportCsv
{
    private static void readCsv(String filename)
    {
 
        try (CSVReader reader = new CSVReader(new FileReader(filename), ','); 
                     Connection connection = DBConnection.getConnection();)
        {
                String insertQuery = "Insert into txn_tbl (txn_id, año, poblacion) values (null,?,?)";
                PreparedStatement pstmt = connection.prepareStatement(insertQuery);
                String[] rowData = null;
                int i = 0;
                while((rowData = reader.readNext()) != null)
                {
                    for (String data : rowData)
                    {
                            pstmt.setString((i % 3) + 1, data);
 
                            if (++i % 3 == 0)
                                    pstmt.addBatch();// add batch
 
                            if (i % 30 == 0)// insert when the batch size is 10
                                    pstmt.executeBatch();
                    }
                }
            }
            catch (Exception e)
            {
                    e.printStackTrace();
            }
     
        }
     
        private static void readCsvUsingLoad(String filename)
        {
            try (Connection connection = DBConnection.getConnection())
            {
     
                    String loadQuery = "LOAD DATA LOCAL INFILE '" + filename + "' INTO TABLE txn_tbl FIELDS TERMINATED BY ','" + " LINES TERMINATED BY '\n' (txn_amount, card_number, terminal_id) ";
                    System.out.println(loadQuery);
                    Statement stmt = connection.createStatement();
                    stmt.execute(loadQuery);
            }
            catch (Exception e)
            {
                    e.printStackTrace();
            }
        }
     
}