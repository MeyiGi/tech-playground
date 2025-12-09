import java.util.List;

public class Company implements Aggreate<Employee> {
    private List<Employee> employees;

    public Company(List<Employee> employees) {
        this.employees = employees;
    }

    @Override
    public Iterator<Employee> createIterator() {
        return new EmployeesIterator(this.employees);
    }
}
