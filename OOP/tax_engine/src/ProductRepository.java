import java.util.List;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.FileWriter;

class ProductRepository {

    // Static list of products
    private static List<Product> products = new ArrayList<>();
    public static List<Product> getProducts() { return products; }
    public static void setProducts(List<Product> products) {
        ProductRepository.products = products;
    }

    // Static method to read the "input.csv" file
    public static void readProducts() {
        readProducts("input.csv");
    }

    // Static method to read from a specified CSV file
    public static void readProducts(String fileName) {
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            
            // Removed the line that skips the header
            // br.readLine();

            while ((line = br.readLine()) != null) {
                // Skip empty lines
                if (line.trim().isEmpty()) {
                    continue;
                }

                // Split the line by commas
                String[] data = line.split(",");

                // Check if the line has the correct number of fields
                if (data.length != 4) {
                    System.err.println("Skipping malformed line: " + line);
                    continue;
                }

                // Extract product details (no need for quotes)
                String name = data[0].trim();
                String type = data[1].trim();
                String country = data[2].trim();
                int price = Integer.parseInt(data[3].trim());  // Parse the price as an integer

                // Create a new Product object and add it to the list
                Product product = new Product(name, type, country, price);
                products.add(product);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (NumberFormatException e) {
            System.err.println("Invalid price format in the CSV file");
            e.printStackTrace();
        }
    }

    // Static method to save tax information into "output.txt" file
    public static void saveTaxInfo(List<String> strings) {
        // Write each string from the list to a new line in "output.txt"
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"))) {
            for (String str : strings) {
                bw.write(str + "\n");  // Write each string followed by a newline
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
