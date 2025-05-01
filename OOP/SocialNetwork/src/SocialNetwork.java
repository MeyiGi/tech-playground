public class SocialNetwork {
    private String name;           // Название социальной сети (private)
    private int userCount;         // Количество пользователей (private)
    protected String[] posts;     // Список постов (protected)
    public int maxPostLength;     // Максимальная длина поста (public)

    // Конструктор по умолчанию (без значений)
    public SocialNetwork() {
        this.name = "Unknown Network";
        this.userCount = 0;
        this.posts = new String[10];
        this.maxPostLength = 280;  // Пример значения для максимальной длины поста
    }

    // Конструктор с параметрами
    public SocialNetwork(String name, int userCount, int maxPostLength) {
        this.name = name;
        this.userCount = userCount;
        this.posts = new String[10]; // Может быть изменено в будущем
        this.maxPostLength = maxPostLength;
    }

    // Геттеры и сеттеры для полей
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getUserCount() {
        return userCount;
    }

    public void setUserCount(int userCount) {
        this.userCount = userCount;
    }

    public String[] getPosts() {
        return posts;
    }

    public void setPosts(String[] posts) {
        this.posts = posts;
    }

    public void addPost(String post) {
        if (post.length() <= maxPostLength) {
            for (int i = 0; i < posts.length; i++) {
                if (posts[i] == null) {
                    posts[i] = post;
                    System.out.println("Post added: " + post);
                    return;
                }
            }
            System.out.println("No space left for new post.");
        } else {
            System.out.println("Post exceeds maximum length.");
        }
    }
}
