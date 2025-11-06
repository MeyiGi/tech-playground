public class Main {
    public static void clientCode(WizardAdapter adapter) {
        adapter.attack();
    }
    public static void main(String[] args) {
        Fighter fighterWithMagic = new Fighter();
        clientCode(fighterWithMagic);
    }
}