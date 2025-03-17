import java.io.*;
import java.util.*;

public class Weather {
    private List<Double> temperatures = new ArrayList<>();

    public double weatherAnalysis(Statistics stat) {
        return stat.calculate(getTemperatures());
    }

    public void readDaysInfo() {
        readDaysInfo("input.txt");
    }

    public void readDaysInfo(String fileName) {
        temperatures.clear();
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(" ");
                if (parts.length == 2) {
                    try {
                        double temp = Double.parseDouble(parts[1]);
                        temperatures.add(temp);
                    } catch (NumberFormatException e) {
                        System.out.println("Маалыматты окууда ката кетти: " + line);
                    }
                }
            }
        } catch (IOException e) {
            System.out.println("Файлды окууда ката кетти: " + e.getMessage());
        }
    }

    public void saveStatistics() {
        double mean = weatherAnalysis(new MeanCalculator());
        double dispersion = weatherAnalysis(new DispersionCalculator());

        try (BufferedWriter writer = new BufferedWriter(new FileWriter("output.txt"))) {
            writer.write("mean - " + mean);
            writer.newLine();
            writer.write("dispersion - " + dispersion);
        } catch (IOException e) {
            System.out.println("Файлга сактоодо ката кетти: " + e.getMessage());
        }
    }

    public List<Double> getTemperatures() {
        return temperatures;
    }

    public void setTemperatures(List<Double> temperatures) {
        this.temperatures = temperatures;
    }
}


/*
Overriding:
---| DispersionCalculator --> calculate(List<Double> temperatures)
---| MeanCalculator --> calculate(List<Double> temperatures)

Overloading:
---| Weather --> readDaysInfo() & readDaysInfo(String fileName)
---| DayInfo --> Dayinfo() & DayInfo(LocalDate date, int temperature)
*/