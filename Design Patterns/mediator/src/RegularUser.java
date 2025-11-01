public class RegularUser extends User {
    public RegularUser(ChatMediator mediator, String username) {
        super(mediator, username);
    }

    @Override
    public void recieveMessage(String message) {
        System.out.println(username + " recieved message: " + message);
    }

    @Override
    public void sendMessage(String message) {
        System.out.println(username + " sent message: " + message);
        mediator.sendMessage(message, this);
    }
}
