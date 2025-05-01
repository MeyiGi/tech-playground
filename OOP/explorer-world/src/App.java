public class App {
    public static void main(String[] args) {
        // Создаем обычного исследователя с параметрами
        Explorer explorer = new Explorer("Explorer John", 80, 30);
        explorer.explore();  // Исследуем мир
        explorer.eat(15);    // Едим
        explorer.explore();  // Еще одно исследование
        explorer.showItems(); // Показываем найденные вещи

        // Создаем гнома с улучшенной добычей и другими параметрами
        Gnome gnome = new Gnome("Gnome Peter", 100, 50, 8);
        gnome.explore();     // Исследуем мир с добычей
        gnome.mine();        // Добываем ископаемые
        gnome.showMinedItems(); // Показываем добытые ископаемые
        gnome.rest();        // Гном отдыхает
        gnome.explore();     // Исследуем снова
    }
}
