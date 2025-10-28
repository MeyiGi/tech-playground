public class Database {
    private static volatile Database obj;
    private String username;
    private String password;

    private Database(String username, String password) {
        this.username = username;
        this.password = password;
    }

    public static Database getInstance() {
        if (obj == null) {
            synchronized (Database.class) {
                if (obj == null) {
                    return new Database("Meyigi", "sAmat.2004h");
                }
            }
        }
        return obj;
    }

    @Override
    public String toString() {
        return "Database{" +
                "username='" + username + '\'' +
                ", password='" + password + '\'' +
                '}';
    }
}
