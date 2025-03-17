public class App {
    public static void main(String[] args) {
        Bank demirbank = new Bank();
        MoneyTransfer transactorByAccountNumber = new TransferByAccountNumber(demirbank);
        MoneyTransfer transactorByPhoneNumber = new TransferByPhoneNumber(demirbank);
        demirbank.readClients("something.txt");
        demirbank.print_clients();
        demirbank.executeTransfer(transactorByAccountNumber, "1234567890", "0987654321",1000);
        demirbank.print_clients();
        demirbank.executeTransfer(transactorByPhoneNumber, "89001234567", "89005554433", 2000);
        demirbank.print_clients();
    }
}