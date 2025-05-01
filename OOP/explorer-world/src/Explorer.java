import java.util.ArrayList;

public class Explorer {
    private String name;
    private int energy;
    private int food;
    private ArrayList<String> items;  // Дополнительные вещи, которые может найти исследователь

    // Конструктор по умолчанию (без параметров)
    public Explorer() {
        this.name = "Unknown Explorer";
        this.energy = 100;
        this.food = 10;  // Начальное количество еды
        this.items = new ArrayList<>();
    }

    // Конструктор с параметрами
    public Explorer(String name, int initialEnergy, int initialFood) {
        this.name = name;
        this.energy = initialEnergy;
        this.food = initialFood;
        this.items = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public int getEnergy() {
        return energy;
    }

    public void addItem(String item) {
        items.add(item);
        System.out.println(name + " found " + item + "!");
    }

    public void eat(int amount) {
        if (amount <= food) {
            food -= amount;
            energy += amount;
            System.out.println(name + " ate " + amount + " units of food. Energy is now " + energy + ".");
        } else {
            System.out.println("Not enough food to eat.");
        }
    }

    public void explore() {
        if (energy > 0) {
            energy -= 10;  // Каждое исследование снижает энергию на 10
            System.out.println(name + " is exploring the world! Energy left: " + energy);
            addItem("Mystical Stone");  // Пример того, что можно найти в ходе исследования
        } else {
            System.out.println(name + " is too tired to explore. Need food to regain energy.");
        }
    }

    public void rest() {
        energy = 100;  // Восстанавливаем энергию
        System.out.println(name + " is resting and now has full energy.");
    }

    // Возвращает все найденные вещи
    public void showItems() {
        if (items.isEmpty()) {
            System.out.println(name + " hasn't found any items yet.");
        } else {
            System.out.println(name + " found the following items:");
            for (String item : items) {
                System.out.println(" - " + item);
            }
        }
    }
}
