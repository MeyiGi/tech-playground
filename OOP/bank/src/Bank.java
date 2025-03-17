import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.List;
import java.util.ArrayList;

public class Bank {
    private List<Client> clients = new ArrayList<>();

    public void print_clients()  {
        for (Client client : clients) {
            System.out.println(client);
        }
    }

    public void readClients() {
        readClients("input.txt");
    }

    public void readClients(String fileName) {
        clients.clear();
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] data = line.split(" ");
                if (data.length == 4) {
                    clients.add(new Client(data[0], data[1], data[2], Integer.parseInt(data[3])));
                }
            }
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }

    public void saveClientsInfo() {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"))) {
            for (Client client : clients) {
                bw.write(client.toString());
                bw.newLine();
            }
        } catch (IOException e) {
            System.out.println("Error writing file: " + e.getMessage());
        }
    }
    
    public void executeTransfer(MoneyTransfer transfer, String sender, String recipient, int amount) {
        transfer.pay(sender, recipient, amount);
    }

    public Client findClientByPhoneNumber(String id) {
        for (Client client : clients) {
            if (client.getPhoneNumber().strip().equals(id)) {
                return client;
            }
        }
        return null;
    }

    public Client findClientByAccountNumber(String id) {
        for (Client client : clients) {
            if (client.getAccountNumber().strip().equals(id)) {
                return client;
            }
        }
        return null;
    }
}

/* 
Overriding:
--- TransferByAccountNumber.java -> pay method
--- TransferByPhoneNumber.java -> pay method

Overloading:
--- Bank.java -> readClients() and readClients(String fileName)
 */