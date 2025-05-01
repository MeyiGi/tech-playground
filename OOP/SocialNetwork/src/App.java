public class App {
    public static void main(String[] args) {
        // Создаем объект SocialNetwork с параметрами
        SocialNetwork facebook = new SocialNetwork("Facebook", 1000000000, 280);
        facebook.addPost("Hello, world!");  // Добавляем пост
        System.out.println(facebook.getName() + " has " + facebook.getUserCount() + " users.");
        
        // Создаем объект TikTok с параметрами
        TikTok tiktok = new TikTok("TikTok", 1200000000, 500, 5000);
        tiktok.addPost("Check out my new dance!");  // Добавляем пост с видео
        tiktok.uploadVideo("Dance Video 1");        // Загружаем видео
        tiktok.getAllVideos();                      // Показываем количество видео
        System.out.println(tiktok.getName() + " has " + tiktok.getUserCount() + " users.");
    }
}
