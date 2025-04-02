public class App {
    public static void main(String[] args) throws Exception {
        View view = new View();
        Model model = new Model();
        new Controller(view, model);
    }
}
