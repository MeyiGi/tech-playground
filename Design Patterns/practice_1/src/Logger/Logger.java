package Logger;

public class Logger {
    private static volatile Logger logger;
    private String name;
    private String password;

    private Logger() {
        this.name = "Daniel";
        this.password = "12345";
    };

    public static Logger getLogger() {
        if (logger == null) {
            synchronized(Logger.class) {
                if (logger == null) {
                    logger = new Logger();
                }
            }
        }

        return logger;
    }
}

