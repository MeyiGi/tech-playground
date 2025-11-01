public interface ChatMediator {
    void sendMessage(String message, User user);
    ChatMediator addUser(User user);
}
