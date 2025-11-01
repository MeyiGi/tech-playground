public class Main {
    public static void main(String[] args) {
        ChatMediator simpleChat = new SimpleChat();
        User daniel = new RegularUser(simpleChat, "daniel");
        User kerem = new RegularUser(simpleChat, "kerem");
        User meyigi = new RegularUser(simpleChat, "meyigi");

        simpleChat
                .addUser(daniel)
                .addUser(kerem)
                .addUser(meyigi);

        daniel.sendMessage("hello motherfucker");
    }
}

// here I can add "factory method"
// here I can add "template method"
// here I can add "commands"
// here I can add "prototype"
// here I can add "builder"


