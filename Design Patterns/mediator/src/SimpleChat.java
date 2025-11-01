import java.util.ArrayList;
import java.util.List;

public class SimpleChat implements ChatMediator {
    List<User> users = new ArrayList<>();

    @Override
    public void sendMessage(String message, User user) {
        for (User u : users) {
            if (u != user) {
                u.recieveMessage(message);
            }
        }
    }

    @Override
    public ChatMediator addUser(User user) {
        users.add(user);
        return this;
    }
}
