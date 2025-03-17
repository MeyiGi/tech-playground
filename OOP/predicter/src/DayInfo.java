import java.time.LocalDate;

public class DayInfo {
    private LocalDate date;
    private int temperature;

    public DayInfo() {
        super();
    }

    public DayInfo(LocalDate date, int temperature) {
        this.date = date;
        this.temperature = temperature;
    }

    public LocalDate getDate() {
        return date;
    }

    public int getTemperature() {
        return temperature;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public void setTemperature(int temperature) {
        this.temperature = temperature;
    }
}
