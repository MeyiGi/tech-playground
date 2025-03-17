import java.util.List;

public class DispersionCalculator implements Statistics {
    @Override
    public double calculate(List<Double> temperatures) {
        if (temperatures.isEmpty()) {
            return 0; // Если список пуст, дисперсия = 0
        }

        // 1. Найти среднее значение (mean)
        double sum = 0;
        for (double temp : temperatures) {
            sum += temp;
        }
        double mean = sum / temperatures.size();

        // 2. Найти сумму квадратов отклонений от среднего
        double varianceSum = 0;
        for (double temp : temperatures) {
            varianceSum += Math.pow(temp - mean, 2);
        }

        // 3. Найти дисперсию (делим сумму на количество элементов)
        return varianceSum / temperatures.size();
    }
}
