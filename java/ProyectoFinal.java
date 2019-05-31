import java.awt.*;
import java.awt.image.*;
import java.io.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;
import javax.swing.table.*;
import java.text.*;
import javax.imageio.ImageIO;
import java.util.*;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.axis.NumberAxis;
import org.jfree.chart.block.BlockBorder;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.chart.title.TextTitle;
import org.jfree.data.xy.XYDataset;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

/**
 * Construye un JFrame que simula grafica la población total, PEA y PEI en
 * México desde 2005 hasta 2018 y hace un estimado lineal de los posibles 
 * resultados para 2019, 2020, 2021 y 2022.

 * @author: Monserrat
 * @version: 31/05/2019
 */

public class ProyectoFinal extends JApplet{
    /** Para colocar los JPanel en Applet.*/
        public ProyectoFinal() {
            this.setContentPane(new ProyectoFinalPanel());
        }//Fin del constructor
    
    /** Crea JFrame para incluir los JPanel de ProyectoFinalPanel. */
        public static void main(String[] args) {
        JFrame window = new JFrame();
        window.setTitle("Proyecto Final");
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setContentPane(new ProyectoFinalPanel());
        window.pack();
        window.show();
        }//fin main
}

class ProyectoFinalPanel extends JPanel implements ActionListener, Runnable {
    private DataFileTable panel; // Carga los archivos csv en un JPanle
    private JPanel bottonPanel, tablePanel; // Los paneles a usar
    private ConvertTableModel model1; // Para reducir los datos del csv.
    private JTable table1; // Aquí se presentarán los csv reducidos
    private JButton rollButton; // Botón para actualizar
    private JFreeChart chart; // Gráfica
    private ChartPanel chartPanel; // Panel de la gráfica

    // Ajuste lineal
    long b = 3239846000L;
    long m = 1667509L;
    long b2 = 1503224000L;
    long m2 = 772436L;
    boolean stop = false;
    int count = 2019;
    Object[] row1 = new Object[4];

    // Series para graficar
    XYSeries serie1 = new XYSeries("Población total"); // Serie para actualizar gráfica
    XYSeries serie2 = new XYSeries("PEA");
    XYSeries serie3 = new XYSeries("PEI");
    XYSeriesCollection datasetOut = new XYSeriesCollection();

    DefaultTableCellRenderer centerRenderer; // Para centrar la tabla

    /** Construye los tres paneles para el JFrame */
    ProyectoFinalPanel(){
    panel = new DataFileTable("PEA.csv", "Poblacion.csv"); // Se leen los archivos

    model1 = new ConvertTableModel("PEA.csv");
    table1 = new JTable();
    table1.setModel(model1);
    table1.createDefaultColumnsFromModel();
    table1.getTableHeader().setFont(new Font("Serif", Font.BOLD, 18));

    centerRenderer = new DefaultTableCellRenderer();
    centerRenderer.setHorizontalAlignment( JLabel.CENTER );
    table1.setDefaultRenderer(String.class, centerRenderer);

    tablePanel = new JPanel();
    tablePanel.setLayout(new GridLayout(1, 2, 4, 0));
    tablePanel.add(new JScrollPane(table1));

    // Gráfica
    chart = createChart(new XYSeriesCollection());
    chartPanel = new ChartPanel(chart);
    // Estilo de gráfica
    chartPanel.setBackground(Color.WHITE);
    tablePanel.add(chartPanel);

    for(int row = 0;row < table1.getRowCount();row++) {
        int fecha = Integer.valueOf(table1.getValueAt(row, 0).toString());
        serie1.add(fecha, Integer.valueOf(table1.getValueAt(row, 1).toString()));
        serie2.add(fecha, Integer.valueOf(table1.getValueAt(row, 2).toString()));
        serie3.add(fecha, Integer.valueOf(table1.getValueAt(row, 3).toString()));
    }

    datasetOut.addSeries(serie1);
    datasetOut.addSeries(serie2);
    datasetOut.addSeries(serie3);

    chart.getXYPlot().setDataset(datasetOut);

    rollButton = new JButton("Actualizar");
    rollButton.setFont(new Font("Sansserif", Font.BOLD, 24));
    rollButton.addActionListener(this);
    bottonPanel = new JPanel();
    bottonPanel.setLayout(new GridLayout(1, 2, 4, 0));
    bottonPanel.add(rollButton);
        
    this.setLayout(new BorderLayout());
    this.add(panel , BorderLayout.NORTH);
    this.add(tablePanel, BorderLayout.CENTER);
    this.add(bottonPanel , BorderLayout.SOUTH);
    }

    /** Listener para el botón. */
    public void run() {
        while (count < 2023) {
            XYSeriesCollection datasetIn = new XYSeriesCollection(); //Dataset de la gráfica
            if (stop) {
                break;
            }
            row1[0] = count; 
            row1[1] = m*count - b;
            row1[2] = m2*count - b2;
            row1[3] = m*count - b - (m2*count - b2);
            model1.addRow(row1); // Actualiza tabla
            table1.setModel(model1);
            table1.createDefaultColumnsFromModel();
            table1.getTableHeader().setFont(new Font("Serif", Font.BOLD, 18));

            centerRenderer = new DefaultTableCellRenderer();
            centerRenderer.setHorizontalAlignment( JLabel.CENTER );
            table1.setDefaultRenderer(String.class, centerRenderer);
            
            serie1.add(count, m*count - b);
            serie2.add(count, m2*count - b2);
            serie3.add(count, m*count - b - (m2*count - b2));
            datasetIn.addSeries(serie1);
            datasetIn.addSeries(serie2);
            datasetIn.addSeries(serie3);
            chart.getXYPlot().setDataset(datasetIn); // Actualiza gráfica
            try {
                Thread.sleep(2000); // Espera 30 segundos
            } catch(Exception e) {}
            count += 1;
        }
        rollButton.setText("Actualizar"); // Cambia botón
    }
    /** Acción si se acticva el botón. */
    public void actionPerformed(ActionEvent e) {
        Thread t=new Thread(this);
        if(e.getActionCommand().equals("Actualizar")) {
            rollButton.setText("Detener");
            stop = false;
            t.start();
        }
        else if(e.getActionCommand().equals("Detener")) {
            rollButton.setText("Actualizar");
            stop = true;
        }
    }

    /** 
     * Contruye la gráfica para el dataset proporcionado.
     @param dataset Dataset para contruir gráfica
     @return Gráfica con el formato deseado
     */
    private JFreeChart createChart(XYDataset dataset) {

        JFreeChart chart = ChartFactory.createXYLineChart(
                "Población en México", 
                "Año", 
                "Número de personas", 
                dataset, 
                PlotOrientation.VERTICAL,
                true, 
                true, 
                false 
        );

        XYPlot plot = chart.getXYPlot();

        XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer();

        // Modficaciones de estilo
        plot.setRenderer(renderer);
        plot.setBackgroundPaint(Color.white);

        plot.setRangeGridlinesVisible(true);
        plot.setRangeGridlinePaint(Color.BLACK);

        plot.setDomainGridlinesVisible(true);
        plot.setDomainGridlinePaint(Color.BLACK);

        chart.getLegend().setFrame(BlockBorder.NONE);

        chart.setTitle(new TextTitle("Población en México (Total, PEA y PEI)",
                        new Font("Serif", java.awt.Font.BOLD, 18)
                )
        );

        return chart;

    }
}

/**
 * Crea el JPanel para presentar los datos del csv.
 */
class DataFileTable extends JPanel {
  public DataFileTable(String dataFilePathPEA, String dataFilePathPob) {
    JTable table3, table2;
    DataFileTableModel model3, model2;
    DefaultTableCellRenderer centerRenderer; // Para centar la tabla
   //  ConvertTableModel model1;
    Font f;

    f = new Font("SanSerif",Font.PLAIN,24);
    setFont(f);
    setLayout(new GridLayout(1, 2, 4, 0));

    model3 = new DataFileTableModel(dataFilePathPEA);
   //  model1 = new ConvertTableModel(dataFilePathPEA);

    table3 = new JTable();
    table3.setModel(model3);
    table3.createDefaultColumnsFromModel();
    table3.getTableHeader().setFont(new Font("Serif", Font.BOLD, 18));
    centerRenderer = new DefaultTableCellRenderer();
    centerRenderer.setHorizontalAlignment( JLabel.CENTER );
    table3.setDefaultRenderer(String.class, centerRenderer);

    model2 = new DataFileTableModel(dataFilePathPob);

    table2 = new JTable();
    table2.setModel(model2);
    table2.createDefaultColumnsFromModel();
    table2.getTableHeader().setFont(new Font("Serif", Font.BOLD, 18));
    centerRenderer = new DefaultTableCellRenderer();
    centerRenderer.setHorizontalAlignment( JLabel.CENTER );
    table2.setDefaultRenderer(String.class, centerRenderer);

    JScrollPane scrollpane1 = new JScrollPane(table3);
    JScrollPane scrollpane2 = new JScrollPane(table2);
    
    add(scrollpane1);
    add(scrollpane2);
    }
}
