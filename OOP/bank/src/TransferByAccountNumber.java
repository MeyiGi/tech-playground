

public class TransferByAccountNumber implements MoneyTransfer {
    private Bank bank;

    public TransferByAccountNumber(Bank bank) {
        this.bank = bank;
    }

    @Override
    public void pay(String sender, String recipient, int amount) {
        Client senderClient = bank.findClientByAccountNumber(sender);
        Client recipientClient = bank.findClientByAccountNumber(recipient);

        if (senderClient == null || recipientClient == null) {
            System.out.println("Ошибка: один из клиентов не найден.");
            return;
        }

        if (senderClient.getBalance() < amount) {
            System.out.println("Ошибка: недостаточно средств у отправителя.");
            return;
        }

        senderClient.setBalance(senderClient.getBalance() - amount);
        recipientClient.setBalance(recipientClient.getBalance() + amount);
        
        System.out.println("Перевод выполнен: " + amount + " от " + sender + " к " + recipient);
        bank.saveClientsInfo();
    }

}