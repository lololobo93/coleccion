import java.awt.*;
import java.awt.event.*;
import java.text.*;
import java.util.Date;
import java.time.Duration;
import java.time.LocalDateTime;
import javax.swing.*;

/**
 * Construye un frame que contiene la hora actual, un cronómetro start-stop y una cuenta 
 * regresiva introducida por el usuario en minutos.

 * @author: Montserrat González García
 * @version: 13/05/2019
 */

public class TareaHilos {

    // Contenido de la clase

    public static void main(String[] args) {
        new TareaHilos();
    }

    /**
     * Constructor del JFrame.
     */
    public TareaHilos() {
        EventQueue.invokeLater(new Runnable() {
            @Override
            public void run() {
                try {
                    UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
                } catch (ClassNotFoundException | InstantiationException | IllegalAccessException | UnsupportedLookAndFeelException ex) {
                    ex.printStackTrace();
                }

                JFrame frame = new JFrame("Hora actual, cronómetro y contador descendente");
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                frame.setMinimumSize(new Dimension(300,300));
                frame.add(new TareaPane());
                frame.pack();
                frame.setLocationRelativeTo(null);
                frame.setVisible(true);
            }
        });
    }//Cierre del constructor.

    /**
     * Constructor del JPanel con los diferentes objetos, es decir, reloj, cronómetro
     * y cuenta regresiva.
     */
    public class TareaPane extends JPanel {

        private JLabel label, timelabel, labelCD;
        private JLabel label1, label2, label3, labelSpace1, labelSpace2, labelSpace3;
        private long lastTickTime;
        private Timer timer, timerHor, timerCD;
        private LocalDateTime startTime;
        private JTextField minSet;

        private Duration duration;

        public TareaPane() {
            setLayout(new GridBagLayout());
            label2 = new JLabel("Cronómetro");
            label2.setFont(new Font("Serif",Font.BOLD, 25));
            label = new JLabel(String.format("%02d:%02d:%02d.%03d", 0, 0, 0, 0));
            label.setFont(new Font("Serif",Font.ITALIC, 20));
            label.setForeground(Color.blue);

            labelSpace1 = new JLabel("          ");
            labelSpace2 = new JLabel("          ");
            labelSpace3 = new JLabel("          ");
            
            label1 = new JLabel("Hora actual");
            label1.setFont(new Font("Serif",Font.BOLD, 25));
            timelabel = new JLabel(String.format("%02d:%02d:%02d", 0, 0, 0));
            timelabel.setFont(new Font("Serif",Font.ITALIC, 20));
            timelabel.setForeground(Color.green);
            DateFormat timeFormat = new SimpleDateFormat("HH:mm:ss");
            
            timer = new Timer(100, new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    long runningTime = System.currentTimeMillis() - lastTickTime;
                    Duration duration = Duration.ofMillis(runningTime);
                    
                    label.setText(format(duration));
                }
            });

            timerHor = new Timer(100, new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    Date date = new Date();
                    String time = timeFormat.format(date);
                    timelabel.setText(time);
                }
            });
            timerHor.setInitialDelay(0);
            timerHor.start();

            GridBagConstraints gbc = new GridBagConstraints();
            gbc.gridx = 0;
            gbc.gridy = 0;
            gbc.gridwidth = 4;
            gbc.gridheight = 1;
            gbc.gridy++;
            add(labelSpace1, gbc);
            gbc.gridy++;
            add(label1, gbc);
            gbc.gridy++;
            add(timelabel, gbc);

            gbc.gridy++;
            add(labelSpace2, gbc);
            gbc.gridy++;
            add(label2, gbc);
            gbc.gridy++;
            add(label, gbc);

            JButton start = new JButton("Start");
            start.setPreferredSize(new Dimension(100, 30));
            start.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    if (!timer.isRunning()) {
                        lastTickTime = System.currentTimeMillis();
                        timer.start();
                    }
                }
            });
            JButton stop = new JButton("Stop");
            stop.setPreferredSize(new Dimension(100, 30));
            stop.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    timer.stop();
                }
            });

            gbc.gridy++;
            gbc.gridwidth = 2;
            add(start, gbc);
            gbc.gridx = 2;
            add(stop, gbc);

            label3 = new JLabel("Cuenta regresiva");
            label3.setFont(new Font("Serif",Font.BOLD, 25));
            gbc.gridx = 0;
            gbc.gridy++;
            gbc.gridwidth = 4;
            add(labelSpace3, gbc);
            gbc.gridy++;
            add(label3, gbc);
            minSet = new JTextField(6);
            gbc.gridy++;
            gbc.gridwidth = 2;
            add(minSet, gbc);
            labelCD = new JLabel("...");
            labelCD.setFont(new Font("Serif",Font.ITALIC, 20));
            labelCD.setForeground(Color.red);

            JButton btnCD = new JButton("Start");
            btnCD.setPreferredSize(new Dimension(100, 30));
            
            btnCD.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    minSet.getText().trim();
                    if(minSet.getText().isEmpty()) {
                        duration = Duration.ofMinutes(0);
                    }
                    else {
                        duration = Duration.ofMinutes(Integer.parseInt(minSet.getText()));
                    }
                    if (timerCD.isRunning()) {
                        timerCD.stop();
                        startTime = null;
                        btnCD.setText("Start");
                    } else {
                        startTime = LocalDateTime.now();
                        timerCD.start();
                        btnCD.setText("Stop");
                    }
                }
            });
            gbc.gridx = 2;
            add(btnCD, gbc);
            gbc.gridx = 0;
            gbc.gridy++;
            gbc.gridwidth = 4;
            add(labelCD, gbc);

            timerCD = new Timer(100, new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    LocalDateTime now = LocalDateTime.now();
                    Duration runningTime = Duration.between(startTime, now);
                    Duration timeLeft = duration.minus(runningTime);
                    if (timeLeft.isZero() || timeLeft.isNegative()) {
                        timeLeft = Duration.ZERO;
                        System.exit(0);
                        // btn.doClick(); // Cheat
                    }

                    labelCD.setText(format(timeLeft));
                }
            });
        }// Cierre del constructor.

        /**
         * Método que convierte una entrada de tiempo a una String con formato 
         * HH:mm:ss.mss.
         * @param duration Duracion en formato temporal a convertir a String HH:mm:ss.mss.
         * @return Tiempo en formato HH:mm:ss.mss
         */
        protected String format(Duration duration) {
            long hours = duration.toHours();
            long minutes = duration.minusHours(hours).toMinutes();
            long millis = duration.minusMinutes(minutes).toMillis();
            long seconds = millis / 1000;
            millis -= (seconds * 1000);
            return String.format("%02d:%02d:%02d.%03d", hours, minutes, seconds, millis);
        }

    }

} // Cierre de la clase.