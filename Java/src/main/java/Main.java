import java.io.*;
import java.net.*;

public class Main {

    static int port = 2018;

    public static void main(String[] args) throws IOException {
        ServerSocket server = new ServerSocket(port);
        System.out.println("Esperando cliente");
        Socket cli = server.accept();

        String recibido = "", enviado = "";

        OutputStreamWriter outw = new OutputStreamWriter(cli.getOutputStream(), "UTF8");
        InputStreamReader inw = new InputStreamReader(cli.getInputStream(), "UTF8");

        char[] cbuf = new char[512];

        while (true) {
            System.out.println("Esperando mensaje del cliente en python");
            inw.read(cbuf);
            for (char c : cbuf) {
                recibido += c;
                if (c == 00) {
                    break;
                }
            }

            System.out.println("Cliente dice: " + recibido);
            System.out.println("Enviar a cliente: >>>" + recibido);
            recibido = "S:" + recibido;


            outw.write(recibido.toCharArray());
            outw.flush();
            recibido = "";

            cbuf = new char[512];
        }
    }
}