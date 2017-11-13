import java.awt.HeadlessException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;

import javax.swing.JOptionPane;


public class Server implements Runnable{
	static private ServerSocket server;
	static private Socket connection;
	static private ObjectOutputStream output;
	static private ObjectInputStream input;
	
	@Override
	public void run(){
	try {
		server = new ServerSocket(5678, 10);	
			while(true){
				connection = server.accept();
				output = new ObjectOutputStream(connection.getOutputStream());
				input = new ObjectInputStream(connection.getInputStream());
				output.writeObject("You have send: " + (String)input.readObject());
				
				}
	}catch (HeadlessException | ClassNotFoundException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
			

}catch (UnknownHostException e) {
		} catch (IOException e) {
			
		}
	}
	}


