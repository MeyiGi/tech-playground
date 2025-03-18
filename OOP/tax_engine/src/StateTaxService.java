import java.util.List;
public class StateTaxService {
    public void stateTaxCalculations(TaxCalculator calculator) {
        // Step 1: Read product data from the input file
        ProductRepository.readProducts();  // Directly calling the static method
        // Step 2: Use the provided TaxCalculator to calculate taxes
        List<String> results = calculator.calculateTax(ProductRepository.getProducts());  // Accessing static method
        // step 3: Saving results in output.txt
        ProductRepository.saveTaxInfo(results);  // Calling the static method
    }
}

/*
Overriding:
a)түзүлгөн программада кайсы методдор overriding жана overloading
  принциптери колдонулуп ишке ашырылды?
    --- CalculateTaxByCountry.java | List<String> calculateTax(List<Product> productsList)
    --- CalculateTaxByType.java | List<String> calculateTax(List<Product> productsList)
    --- Product.java | String toString()

    Overloading:
    --- Product(), Product(String name, String type, String countryCode, int price)
    --- readProducts(), readProducts(String fileName)

б)полиморфизм кайсы жерде кандай түрдө колдонулду?
    Принципы полиморфизма была задействована для классов CalculateTaxByCountry где
    родителький класс TaxCalculator, благодаря этому можно вызывать
    
    TaxCalculator calculator = CalculateTaxByCountry или же CalculateTaxByType
    и когда вызываем calculator то оно будет работать для обеих не приходиться
    создавать несколько функций и можем ограничиться с одним
    """ public void stateTaxCalculations(TaxCalculator calculator) """
    а не создавать два метода как
    """ public void stateTaxCalculations(CalculateTaxByCountry calculator) """
     """ public void stateTaxCalculations(CalculateTaxByType calculator) """
 */