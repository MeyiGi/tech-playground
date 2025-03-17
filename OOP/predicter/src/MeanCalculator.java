import java.util.List;

public class MeanCalculator implements Statistics {
    @Override
    public double calculate(List<Double> temperatures) {
        double total = 0;

        for (int i = 0; i < temperatures.size(); i++) {
            total += temperatures.get(i);
        }

        return total / temperatures.size();
    }
}
