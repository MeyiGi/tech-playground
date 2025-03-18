import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class CalculateTaxByType implements TaxCalculator {
    @Override
    public List<String> calculateTax(List<Product> productsList) {
        // Grouping products by type and summing up the price for each type
        Map<String, Double> typeTotalPriceMap = productsList.stream()
                .collect(Collectors.groupingBy(
                        Product::getType, 
                        Collectors.summingDouble(Product::getPrice)
                ));

        // Creating a list of strings where each string is formatted as "Type: totalTax"
        return typeTotalPriceMap.entrySet().stream()
                .map(entry -> entry.getKey() + ": " + (entry.getValue() * 0.1)) // Calculate tax (10% of total price)
                .collect(Collectors.toList());
    }
}
