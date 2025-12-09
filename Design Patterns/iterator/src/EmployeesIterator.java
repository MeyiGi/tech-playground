import java.util.List;
import java.util.NoSuchElementException;

public class EmployeesIterator implements Iterator<Employee> {
    private List<Employee> employees;
    private int currIndex;

    public EmployeesIterator(List<Employee> employees) {
        this.employees = employees;
    }

    @Override
    public Employee next() {
        if (!haveNext()) {
            throw new NoSuchElementException();
        }

        return employees.get(currIndex++);
    }

    @Override
    public boolean haveNext() {
        return currIndex < employees.size();
    }
}
