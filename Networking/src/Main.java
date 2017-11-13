import java.awt.FlowLayout;
import java.awt.HeadlessException;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JTextField;

//Main class - socket, input, output
public class Main extends JFrame implements Runnable{
	static private Socket connection;
	static private ObjectOutputStream output;
	static private ObjectInputStream input;
	
	//Main method = initiates multithreading;
	
	public static void main(String[] args){
		new Thread(new Main("Test")).start();
		new Thread(new Server()).start();
						
	}
	//GUI
	public Main(String name){
		super(name);
		setLayout(new FlowLayout());
		setSize(300, 300);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setVisible(true);
		setLocationRelativeTo(null);
		
		final JTextField t1 = new JTextField(10);
		final JButton b1 = new JButton("Send");
		b1.addActionListener(new ActionListener(){

			@Override
			public void actionPerformed(ActionEvent arg0) {
				if(arg0.getSource()==b1){
					sendData(t1.getText());
					
				}
				
			}	
		});
		
		add(t1);
		add(b1);
		
		
		
	}
	@Override
	//Method that runs application
	public void run(){
		System.out.println("1");
		try {
			
			while(true){
				connection = new Socket(InetAddress.getByName("127.0.0.1"), 5678);
				output = new ObjectOutputStream(connection.getOutputStream());
				input = new ObjectInputStream(connection.getInputStream());
				try {
					JOptionPane.showMessageDialog(null, (String)input.readObject());
				} catch (HeadlessException | ClassNotFoundException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		} catch (UnknownHostException e) {
		} catch (IOException e) {}
	}	
		private static void sendData(Object obj){
			try {
				output.flush();
				output.writeObject(obj);
			} catch (IOException e) {
				
			}
		}
	}	

