public class App {
    public static void main(String[] args) throws Exception {
        TaxCalculator calculator = new CalculateTaxByCountry();
        StateTaxService taxService = new StateTaxService();
        taxService.stateTaxCalculations(calculator);
    }
}
