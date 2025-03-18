public class Product {
    private String name;
    private String type;
    private String countryCode;
    private int price;

    // Default constructor
    public Product() {
        super();
    }

    // Non-default constructor
    public Product(String name, String type, String countryCode, int price) {
        this.name = name;
        this.type = type;
        this.countryCode = countryCode;
        this.price = price;
    }

    // Getter and Setter for name
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    // Getter and Setter for type
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    // Getter and Setter for countryCode
    public String getCountryCode() {
        return countryCode;
    }

    public void setCountryCode(String countryCode) {
        this.countryCode = countryCode;
    }

    // Getter and Setter for price
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return "Product{" +
                "name='" + name + '\'' +
                ", type='" + type + '\'' +
                ", country='" + countryCode + '\'' +
                ", price=" + price +
                '}';
    }
}