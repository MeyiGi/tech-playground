public class Logger {
    private static volatile Logger logger;
    private String username;
    private String password;

    private Logger(String username, String password) {
        this.username = username;
        this.password = password;
    }

    public static Logger getInstance() {
        if (logger == null) {
            synchronized (Logger.class) {
                if (logger == null) {
                    logger = new Logger("doni", "samat2004");
                }
            }
        }
        return logger;
    }
}
