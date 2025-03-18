import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class CalculateTaxByCountry implements TaxCalculator {
    @Override
    public List<String> calculateTax(List<Product> productsList) {
        // Grouping products by countryCode and summing up the price for each country
        Map<String, Double> countryTotalPriceMap = productsList.stream()
                .collect(Collectors.groupingBy(
                        Product::getCountryCode, 
                        Collectors.summingDouble(Product::getPrice)
                ));

        // Creating a list of strings where each string is formatted as "Country: totalTax"
        return countryTotalPriceMap.entrySet().stream()
                .map(entry -> entry.getKey() + ": " + (entry.getValue() * 0.1)) // Calculate tax (10% of total price)
                .collect(Collectors.toList());
    }
}