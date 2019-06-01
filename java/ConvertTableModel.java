import javax.swing.*;
import javax.swing.table.*;
import javax.swing.event.*;
import java.io.*;
import java.util.*;

/**
 * Clase de apoyo para el archivo principal ProyectoFinal.
 */
public class ConvertTableModel extends AbstractTableModel {
  protected Vector data;
  protected Vector columnNames ;  
  protected String datafile;
  
  public ConvertTableModel(String f){
    datafile = f;
    initVectors();  
    }

  public void initVectors() {
    String aLine ;
    data = new Vector();
    columnNames = new Vector();
    try {
      FileInputStream fin =  new FileInputStream(datafile);
      BufferedReader br = new BufferedReader(new InputStreamReader(fin));
      // extract column names
      StringTokenizer st1 = 
         new StringTokenizer(br.readLine(), ",");
         columnNames.addElement("Periodo"); 
         columnNames.addElement("Población");
         columnNames.addElement("PEA");
          columnNames.addElement("PEI");
      // extract data
      int basis = 2005;
      int memory = 0;
      int actual;
      String fecha;
      boolean isFound;
      long b = 3239846000L;
      long m = 1667509L;
      while ((aLine = br.readLine()) != null) {  
        StringTokenizer st2 = new StringTokenizer(aLine, ",");
        while(st2.hasMoreTokens()) {
          fecha = st2.nextToken();
          actual = Integer.valueOf(st2.nextToken());
          isFound = fecha.indexOf(String.valueOf(basis)) !=-1? true: false;
          if (isFound) {
            memory += actual;
          }
          else {
            data.addElement(String.valueOf(basis));
            if (basis==2005){
              memory /= 4;
            }
            else {
              memory /= 3;
            }
            data.addElement(String.valueOf(m*basis - b));
            data.addElement(String.valueOf(memory));
            data.addElement(String.valueOf(m*basis - b - memory));
            basis += 1;
            memory = 0;
          }
        }
      }
      br.close();  
    }
    catch (Exception e) {
      e.printStackTrace();
      }
  }

  public int getRowCount() {
    return data.size() / getColumnCount();
    }

  public int getColumnCount(){
    return columnNames.size();
    }

  public String getColumnName(int columnIndex) {
    String colName = "";

    if (columnIndex <= getColumnCount())
       colName = (String)columnNames.elementAt(columnIndex);

    return colName;
    }
    
  public Class getColumnClass(int columnIndex){
    return String.class;
    }
    
  public boolean isCellEditable(int rowIndex, int columnIndex) {
    return false;
    }
    
  public Object getValueAt(int rowIndex, int columnIndex) {
    return (String)data.elementAt
        ( (rowIndex * getColumnCount()) + columnIndex);
    }
    
  public void setValueAt(Object aValue, int rowIndex, int columnIndex) {
    return;
    }

  public void addRow(Object[] row) {
    data.addElement(String.valueOf(row[0]));
    data.addElement(String.valueOf(row[1]));
    data.addElement(String.valueOf(row[2]));
    data.addElement(String.valueOf(row[3]));
    }
}