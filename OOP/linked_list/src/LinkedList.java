public class LinkedList {
    // Узел списка
    private static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
        }
    }

    private Node head;

    // Добавить в конец
    public void append(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }

        Node curr = head;
        while (curr.next != null) {
            curr = curr.next;
        }
        curr.next = newNode;
    }

    // Получить длину списка
    public int getLength() {
        int count = 0;
        Node curr = head;
        while (curr != null) {
            count++;
            curr = curr.next;
        }
        return count;
    }

    // Вставка по индексу
    public void insertAtIndex(int index, int data) {
        if (index < 0 || index > getLength()) {
            throw new IndexOutOfBoundsException("Invalid index");
        }

        Node newNode = new Node(data);
        if (index == 0) {
            newNode.next = head;
            head = newNode;
            return;
        }

        Node curr = head;
        for (int i = 0; i < index - 1; i++) {
            curr = curr.next;
        }
        newNode.next = curr.next;
        curr.next = newNode;
    }

    // Удалить по индексу
    public void deleteAtIndex(int index) {
        if (index < 0 || index >= getLength()) {
            throw new IndexOutOfBoundsException("Invalid index");
        }

        if (index == 0) {
            head = head.next;
            return;
        }

        Node curr = head;
        for (int i = 0; i < index - 1; i++) {
            curr = curr.next;
        }
        curr.next = curr.next.next;
    }

    // Проверка существования значения
    public boolean isExists(int data) {
        Node curr = head;
        while (curr != null) {
            if (curr.data == data) {
                return true;
            }
            curr = curr.next;
        }
        return false;
    }

    // Получить по индексу
    public int getByIndex(int index) {
        if (index < 0 || index >= getLength()) {
            throw new IndexOutOfBoundsException("Invalid index");
        }

        Node curr = head;
        for (int i = 0; i < index; i++) {
            curr = curr.next;
        }
        return curr.data;
    }

    // Вывести весь список
    public void printList() {
        Node curr = head;
        while (curr != null) {
            System.out.print(curr.data + " -> ");
            curr = curr.next;
        }
        System.out.println("null");
    }

    // Пример использования
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.append(10);
        list.append(20);
        list.append(30);
        list.printList(); // 10 -> 20 -> 30 -> null

        list.insertAtIndex(1, 15);
        list.printList(); // 10 -> 15 -> 20 -> 30 -> null

        list.deleteAtIndex(2);
        list.printList(); // 10 -> 15 -> 30 -> null

        System.out.println("Length: " + list.getLength()); // 3
        System.out.println("Exists 15? " + list.isExists(15)); // true
        System.out.println("Value at index 1: " + list.getByIndex(1)); // 15
    }
}
