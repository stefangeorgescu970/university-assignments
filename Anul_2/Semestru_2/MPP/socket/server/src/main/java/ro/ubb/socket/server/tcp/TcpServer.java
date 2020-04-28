package ro.ubb.socket.server.tcp;

import ro.ubb.socket.common.HelloService;
import ro.ubb.socket.common.HelloServiceException;
import ro.ubb.socket.common.Message;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.function.UnaryOperator;

public class TcpServer {
    private ExecutorService executorService;
    private String serverHost;
    private int serverPort;

    private Map<String, UnaryOperator<Message>> methodHandlers;

    public TcpServer(ExecutorService executorService, String serverHost, int serverPort) {
        this.executorService = executorService;
        this.serverHost = serverHost;
        this.serverPort = serverPort;

        methodHandlers = new HashMap<>();
    }

    public void addHandler(String methodName, UnaryOperator<Message> handler) {
        methodHandlers.put(methodName, handler);
    }

    public void startServer() {
        try {
            ServerSocket serverSocket = new ServerSocket(serverPort);
            System.out.println("server started - waiting for clients");

            while (true) {
                Socket client = serverSocket.accept();
                System.out.println("client connected");

                executorService.submit(new ClientHandler(client));
            }

        } catch (IOException e) {
            e.printStackTrace();
            throw new HelloServiceException(e);
        }
    }

    private class ClientHandler implements Runnable {
        private Socket socket;

        ClientHandler(Socket socket) {
            this.socket = socket;
        }

        @Override
        public void run() {
            try (OutputStream os = socket.getOutputStream();
                 InputStream is = socket.getInputStream()) {

                Message request = Message.builder().build();
                request.readFrom(is);
                System.out.println("server - received request: " + request);

                Message response = methodHandlers.get(request.getHeader()).apply(request);
                System.out.println("server - computed response: " + response);

                response.writeTo(os);

            } catch (IOException e) {
                e.printStackTrace();
                throw new HelloServiceException(e);
            } finally {
                if (socket != null) {
                    try {
                        socket.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }

        }
    }
}
