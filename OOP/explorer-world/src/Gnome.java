import java.util.ArrayList;

public class Gnome extends Explorer {
    private int miningSkill;
    private ArrayList<String> minedItems;

    // Конструктор с параметрами
    public Gnome(String name, int initialEnergy, int initialFood, int miningSkill) {
        super(name, initialEnergy, initialFood);  // Вызов конструктора родительского класса
        this.miningSkill = miningSkill;
        this.minedItems = new ArrayList<>();
    }

    // Переопределяем метод explore для улучшенной добычи ископаемых
    @Override
    public void explore() {
        if (getEnergy() > 0) {
            super.explore();  // Исследуем мир
            mine();  // После исследования добываем ископаемые
        } else {
            System.out.println(getName() + " is too tired to explore. Need food to regain energy.");
        }
    }

    // Метод для добычи ископаемых
    public void mine() {
        if (getEnergy() >= 15) {
            int minerals = miningSkill * 3;  // Чем выше мастерство, тем больше минералов
            String mineral = "Gemstone (" + minerals + " units)";
            minedItems.add(mineral);
            System.out.println(getName() + " mined a " + mineral + "!");
            rest();  // После добычи ископаемых гном отдыхает
        } else {
            System.out.println(getName() + " doesn't have enough energy to mine. Need rest.");
        }
    }

    // Показываем добытые ископаемые
    public void showMinedItems() {
        if (minedItems.isEmpty()) {
            System.out.println(getName() + " hasn't mined anything yet.");
        } else {
            System.out.println(getName() + " has mined the following items:");
            for (String item : minedItems) {
                System.out.println(" - " + item);
            }
        }
    }
}
