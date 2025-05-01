public class App {
    public static void main(String[] args) {
        MoodDiary myDiary = new MoodDiary("Daniel", "Inspired 💡", "Started learning advanced Java!", "📘");

        myDiary.addTag("java");
        myDiary.addTag("study");
        myDiary.showEntry();

        myDiary.quickUpdate("Feeling happy and productive!");
        myDiary.setNote("Solved some tough problems and drank coffee ☕");
        myDiary.addTag("coffee");
        myDiary.showEntry();

        myDiary.getSummary();
        myDiary.motivateMe();
        myDiary.showAllHistory();
    }
}
