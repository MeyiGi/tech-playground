public class Client {
    private String name;
    private String accountNumber;
    private String phoneNumber;
    private int balance;

    Client() {
        super();
    }

    Client(String name, String accountNumber, String phoneNumber, int balance) {
        this.name = name;
        this.accountNumber = accountNumber;
        this.phoneNumber = phoneNumber;
        this.balance = balance;
    }

    public String getName() {
        return name;
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public int getBalance() {
        return balance;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAccountNumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }

    public void setBalance(int balance) {
        this.balance = balance;
    }
    
    @Override
    public String toString() {
        return this.name + " " + this.accountNumber + " " + this.phoneNumber + " " + this.balance;
    }
}
