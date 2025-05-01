import java.util.ArrayList;

public class MoodDiary {
    private String owner;
    private String mood;
    private String note;
    private String emoji;
    private ArrayList<String> tags;
    private ArrayList<String> history;

    public MoodDiary() {
        this.owner = "Unknown 🌚";
        this.mood = "Neutral 😐";
        this.note = "Nothing much today...";
        this.emoji = "📔";
        this.tags = new ArrayList<>();
        this.history = new ArrayList<>();
    }

    public MoodDiary(String owner, String mood, String note, String emoji) {
        this.owner = owner;
        this.mood = mood;
        this.note = note;
        this.emoji = emoji;
        this.tags = new ArrayList<>();
        this.history = new ArrayList<>();
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    public void setMood(String mood) {
        this.mood = mood;
    }

    public void setNote(String note) {
        this.note = note;
    }

    public void setEmoji(String emoji) {
        this.emoji = emoji;
    }

    public void showEntry() {
        System.out.println("📝 Entry for " + owner + " " + emoji);
        System.out.println("Mood: " + mood);
        System.out.println("Note: " + note);
        if (!tags.isEmpty()) {
            System.out.print("Tags: ");
            for (String tag : tags) {
                System.out.print("#" + tag + " ");
            }
            System.out.println();
        }
        System.out.println("──────────────────────────────");
        saveToHistory();  // Автоматически сохраняем запись
    }

    public void quickUpdate(String newMood) {
        this.mood = newMood;
        if (newMood.toLowerCase().contains("happy")) emoji = "😄";
        else if (newMood.toLowerCase().contains("sad")) emoji = "😢";
        else if (newMood.toLowerCase().contains("angry")) emoji = "😡";
        else if (newMood.toLowerCase().contains("love")) emoji = "😍";
        else emoji = "🤔";
    }

    public void motivateMe() {
        String[] messages = {
            "🌈 Every day is a fresh start!",
            "🔥 Believe in yourself!",
            "💪 You’ve got this!",
            "🚀 Keep pushing forward!",
            "🧘 Take a deep breath and smile."
        };
        int i = (int) (Math.random() * messages.length);
        System.out.println("💡 Motivation for " + owner + ": " + messages[i]);
    }

    public void addTag(String tag) {
        tags.add(tag.replace("#", "")); // избегаем двойных #
    }

    public void getSummary() {
        System.out.println("📊 Summary for " + owner + ":");
        System.out.println("Last Mood: " + mood + " " + emoji);
        System.out.println("Tags: " + (tags.isEmpty() ? "none" : tags));
        System.out.println("Notes saved: " + history.size());
        System.out.println("──────────────────────────────");
    }

    private void saveToHistory() {
        history.add("Mood: " + mood + ", Note: " + note + ", Emoji: " + emoji + ", Tags: " + tags.toString());
    }

    public void showAllHistory() {
        System.out.println("📚 History for " + owner + ":");
        for (String entry : history) {
            System.out.println("• " + entry);
        }
        System.out.println("──────────────────────────────");
    }
}
