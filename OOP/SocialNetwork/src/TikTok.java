public class TikTok extends SocialNetwork {
    private int videoCount;  // Количество видео (private)

    // Конструктор с параметрами
    public TikTok(String name, int userCount, int maxPostLength, int videoCount) {
        super(name, userCount, maxPostLength);  // Вызов конструктора родительского класса
        this.videoCount = videoCount;
    }

    // Конструктор без параметров (по умолчанию)
    public TikTok() {
        super();
        this.videoCount = 0;
    }

    // Геттеры и сеттеры для videoCount
    public int getVideoCount() {
        return videoCount;
    }

    public void setVideoCount(int videoCount) {
        this.videoCount = videoCount;
    }

    // Метод для загрузки видео
    public void uploadVideo(String video) {
        videoCount++;
        System.out.println("Video uploaded: " + video + ". Total videos: " + videoCount);
    }

    // Метод для получения всех видео (расширяет функциональность)
    public void getAllVideos() {
        System.out.println("Total videos on TikTok: " + videoCount);
    }

    // Переопределяем метод добавления поста, учитывая видео
    @Override
    public void addPost(String post) {
        super.addPost(post);  // Используем метод родителя для добавления текста
        System.out.println("Post on TikTok added with multimedia content.");
    }
}
