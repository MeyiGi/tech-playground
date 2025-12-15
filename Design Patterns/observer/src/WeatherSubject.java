import java.util.ArrayList;
import java.util.List;

public class WeatherSubject implements Subject {
    private List<Observer> observers;
    private String weather;

    public WeatherSubject() {
        this.observers = new ArrayList<>();
    }

    @Override
    public void notifyMessage() {
        for (Observer observer : this.observers) {
            observer.update(this.weather);
        }
    }

    @Override
    public void addObserver(Observer observer) {
        this.observers.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        this.observers.remove(observer);
    }

    public void setWeather(String weather) {
        this.weather = weather;
        notifyMessage();
    }
}
