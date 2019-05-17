import java.awt.*;
import java.awt.image.*;
import java.io.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;
import javax.swing.table.*;
import java.text.*;
import javax.imageio.ImageIO;
import java.util.Random;
import java.util.Date;
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
 * Construye un JFrame que simula el lanzamiento de dos dados, muestra la
 * hora, además de registrar los lanzamientos en una tabla y una gráfica.

 * @author: Jesús Ernesto Carro Martínez
 * @version: 17/05/2019
 */

public class Dice extends JApplet{
/** Para colocar los JPanel en Applet.*/
    public Dice() {
        this.setContentPane(new RollDicePanel());
    }//Fin del constructor

/** Crea JFrame para incluir los JPale de RollDicePanel. */
    public static void main(String[] args) {
    JFrame window = new JFrame();
    window.setTitle("Lanzamiento de dados");
    window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    window.setContentPane(new RollDicePanel());
    window.pack();
    window.show();
    }//fin main
}

class RollDicePanel extends JPanel implements ActionListener, Runnable {
    private Die _left; // Dados
    private Die _right;
    private JTable table; // Tabla
    private DefaultTableModel model; // Modelo de la tabla
    private JFreeChart chart; // Gráfica
    private ChartPanel chartPanel; // Panel de la gráfica
    
    JLabel timelabel; // JLabel para tiempo
    Timer timerHor; // Timer para timelabel
    JButton rollButton; // Botón
    JPanel firstPanel, dicePanel, tablePanel; // Los paneles a usar
    boolean stop=false;
    DefaultTableCellRenderer centerRenderer; // Para centar la tabla

    /** Construye los tres paneles para el JFrame */
    RollDicePanel() {
        // Se crean los dados
        _left = new Die();
        _right = new Die();
        // La tabla
        table = new JTable();
        model = new DefaultTableModel();
        Object[] columns = {"Tiro", "Dado 1", "Dado 2"};
        table.setModel(model);
        model.setColumnIdentifiers(columns);
        // Se arregla la tabla
        table.setBackground(Color.WHITE);
        table.setFont(new Font("Serif", Font.PLAIN, 20));
        table.setRowHeight(30);
        centerRenderer = new DefaultTableCellRenderer();
        centerRenderer.setHorizontalAlignment( JLabel.CENTER );
        table.setDefaultRenderer(String.class, centerRenderer);
        table.getTableHeader().setBackground(Color.WHITE);
        table.getTableHeader().setFont(new Font("Serif", Font.BOLD, 22));
        // Gráfica
        chart = createChart(new XYSeriesCollection());
        chartPanel = new ChartPanel(chart);
        // Estilo de gráfica
        chartPanel.setBackground(Color.WHITE);
        // Botón
        rollButton = new JButton("Lanzar");
        rollButton.setFont(new Font("Sansserif", Font.BOLD, 24));
        rollButton.addActionListener(this);
        // Jlabel para tiempo
        timelabel = new JLabel(String.format("%02d:%02d:%02d", 0, 0, 0));
        timelabel.setFont(new Font("Serif", Font.ITALIC, 18));
        timelabel.setHorizontalAlignment(JLabel.CENTER);
        timelabel.setOpaque(true);
        timelabel.setBackground(Color.WHITE);
        // timelabel.setBackground(Color.RED);
        DateFormat timeFormat = new SimpleDateFormat("HH:mm:ss");
        // Timer para el timelabel
        timerHor = new Timer(100, new ActionListener() {
            @Override
            /** ActionListener para cambiar el timelabel */
            public void actionPerformed(ActionEvent e) {
                Date date = new Date();
                String time = timeFormat.format(date);
                timelabel.setText(time);
            }
        });
        timerHor.setInitialDelay(0);
        timerHor.start();
        
        // Los JPanel de cada parte
        firstPanel = new JPanel();
        firstPanel.setLayout(new GridLayout(1, 2, 4, 0));
        firstPanel.add(timelabel);
        firstPanel.add(rollButton);

        dicePanel = new JPanel();
        dicePanel.setLayout(new GridLayout(1, 2, 4, 0));
        dicePanel.add(_left);
        dicePanel.add(_right);
        
        tablePanel = new JPanel();
        tablePanel.setLayout(new GridLayout(1, 2, 4, 0));
        tablePanel.add(new JScrollPane(table));
        tablePanel.add(chartPanel);

        // Se agrega al JFrame
        this.setLayout(new BorderLayout());
        this.add(firstPanel , BorderLayout.NORTH);
        this.add(dicePanel, BorderLayout.CENTER);
        this.add(tablePanel , BorderLayout.SOUTH);
    }//Fin del cosntructor

    /** Listener para el botón. */
    public void run() {
        int dado1, dado2;
        Object[] row = new Object[3];
        XYSeries serie1 = new XYSeries("Dado 1"); // Serie para actualizar gráfica
        XYSeries serie2 = new XYSeries("Dado 2");
        for (int i=0; ;i++) {
            XYSeriesCollection dataset = new XYSeriesCollection(); //Dataset de la gráfica
            if (stop) {
                break;
            }
            dado1 = _left.roll(); // Se lanza dado
            dado2 = _right.roll(); // y el otro dado también.
            
            row[0] = i+1;
            row[1] = dado1;
            row[2] = dado2;
            model.addRow(row); // Actualiza tabla
            table.getColumnModel().getColumn(0).setCellRenderer(centerRenderer); 
            table.getColumnModel().getColumn(1).setCellRenderer(centerRenderer); 
            table.getColumnModel().getColumn(2).setCellRenderer(centerRenderer); 
            
            serie1.add(i+1, dado1);
            serie2.add(i+1, dado2);
            dataset.addSeries(serie1);
            dataset.addSeries(serie2);
            chart.getXYPlot().setDataset(dataset); // Actualiza gráfica
            if (i==4) { // para correr solo 5 veces
                break;
            }
            try {
                Thread.sleep(30000); // Espera 30 segundos
            } catch(Exception e) {}
        }
        rollButton.setText("Lanzar"); // Cambia botón
    }
    /** Acción si se acticva el botón. */
    public void actionPerformed(ActionEvent e) {
        Thread t=new Thread(this);
        if(e.getActionCommand().equals("Lanzar")) {
            rollButton.setText("Detener");
            stop = false;
            model.setRowCount(0);
            t.start();
        }
        else if(e.getActionCommand().equals("Detener")) {
            rollButton.setText("Lanzar");
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
                "Dados", 
                "Tiro", 
                "Resultado", 
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

        chart.setTitle(new TextTitle("Lanzamiento de dados",
                        new Font("Serif", java.awt.Font.BOLD, 18)
                )
        );

        return chart;

    }
}

class Die extends JPanel {
    private int _value; // Valor obtenido
    private BufferedImage image; // Aquí se guardará la imagen
    private static Random random = new Random(); // Generador aleatorio

    /** Construye la base para el dado*/
    public Die() {
        setBackground(Color.RED);
        setPreferredSize(new Dimension(515,515));
        roll();
    }//Fin de constructor
    
    /** 
     * Genera número aleatorio de 1 a 6..
    @return Número entre 1 y 6.
    */
    public int roll() {
        int val = random.nextInt(6) + 1; // Range 1-6
        setValue(val);
        return val;
    }//Fin de roll

    /** 
     * Modifica el valor del dado y ejecuta repaint().
     @param spots Número entre 1 y 6.
    */
    public void setValue(int spots) {
        _value = spots;
        repaint(); // Redibujamos el dado.
    }//end setValue
    
    /** Usada por paintComponent(). Carga la imagen a usar. */
    public void ImagePanel() {
        try {
            image = ImageIO.read(new File("./dados/"+String.valueOf(_value)+".png"));
        } catch (IOException ex) {}
    }// Fin ImagePanel

    /** Dibuja el dado. */
    public void paintComponent(Graphics g) {
        super.paintComponent(g); // Necesario
        ImagePanel();
        int x = (this.getWidth() - image.getWidth(null)) / 2;
        int y = (this.getHeight() - image.getHeight(null)) / 2;
        g.drawImage(image, x, y, null);
    }//Fin paintComponent
}// Fin Dice